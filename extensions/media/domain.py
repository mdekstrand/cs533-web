"""
Sphinx extension to implement video support
"""

import re
from dataclasses import dataclass

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.roles import XRefRole
from sphinx.domains import Domain, ObjType
from sphinx.util.nodes import make_id, make_refnode

from .module import ModuleDirective
from .video import VideoDirective
from .reading import ReadingDirective
from .book import BookDirective


EMOJI_DEFS = {
    'module': '📅',
    'video': '🎥',
    'reading': '📃',
    'book': '📖'
}

XREF_TYPE_OVERRIDES = {
    'book': nodes.title_reference
}

_vl_re = re.compile(r'(\d+)m(\d+)s')
_rd_re = re.compile(r'(\d+)\s*words')
_pfx_re = re.compile(r'^(\d+-\d+\s+-\s+)?(.*)')


@dataclass
class MediaObject:
    name: str
    title: str
    type: str
    docname: str
    anchor: str
    module: str = None

    def astuple(self):
        """
        Convert this object into a tuple suitable for get_objects().
        """
        return (self.name, self.display_title, self.type, self.docname, self.anchor, 1)

    @property
    def display_title(self):
        icon = EMOJI_DEFS.get(self.type, None)
        return f'{icon} {self.title}' if icon else self.title


@dataclass
class Reading(MediaObject):
    length: str = None

    def read_length(self):
        if self.length:
            m = _rd_re.match(self.length)
            words = int(m.group(1))
            return words


@dataclass
class Video(MediaObject):
    length: str = None

    def vid_length(self):
        if self.length:
            m = _vl_re.match(self.length)
            mins = float(m.group(1))
            secs = float(m.group(2))
            return mins * 60 + secs


class CourseDomain(Domain):
    name = 'res'
    label = 'Course'

    object_types = {
        'module': ObjType('module', 'module'),
        'video': ObjType('video', 'video'),
        'reading': ObjType('reading', 'reading'),
        'book': ObjType('book', 'book')
    }
    directives = {
        'module': ModuleDirective,
        'reading': ReadingDirective,
        'video': VideoDirective,
        'book': BookDirective,
    }
    roles = {
        'module': XRefRole(),
        'reading': XRefRole(),
        'video': XRefRole(),
        'book': XRefRole(),
    }

    def _dom_objects(self):
        return self.env.domaindata['res'].setdefault('objects', [])

    def note_module(self, key, title):
        docname = self.env.docname
        mod = MediaObject(key, title, 'module', docname, key)
        self._dom_objects().append(mod)

    def note_reading(self, key, title, length):
        modname = self.env.ref_context.get('res:module')
        fullkey = f'{modname}:{key}' if modname else key
        docname = self.env.docname

        mod = Reading(fullkey, title, 'reading', docname, key, modname, length)
        self._dom_objects().append(mod)

    def note_video(self, key, id, name, length):
        modname = self.env.ref_context.get('res:module')
        fullkey = f'{modname}:{key}' if modname else key
        docname = self.env.docname

        if name:
            trunc = _pfx_re.match(name).group(2)
        else:
            trunc = '<untitled video>'

        mod = Video(fullkey, trunc, 'video', docname, id, modname, length)
        mod.full_name = name

        self._dom_objects().append(mod)

    def note_object(self, type, key, title, anchor=None):
        docname = self.env.docname
        if not anchor:
            anchor = key
        mod = MediaObject(key, title, type, docname, anchor)
        self._dom_objects().append(mod)

    def resolve_xref(self, env, fromdocname, builder, type, target, node, contnode):
        objects = self._dom_objects()

        tgt = None
        for candidate in objects:
            if candidate.name == target:
                tgt = candidate
                break

        if not tgt:
            return None

        label = tgt.display_title
        cnode = XREF_TYPE_OVERRIDES.get(tgt.type, nodes.inline)
        content = cnode('', label)

        return make_refnode(builder, fromdocname, tgt.docname, tgt.anchor, content, tgt.name)
