"""
Sphinx extension to implement video support
"""

from pathlib import Path
import re
import csv
from dataclasses import dataclass

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.roles import XRefRole
from sphinx.domains import Domain, ObjType
from sphinx.util.nodes import make_id, make_refnode, _make_id

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

_vl_re = re.compile(r'(\d+)m(?:(\d+)s)?')
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
        return f'{icon}\u00A0{self.title}' if icon else self.title


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
            secs = m.group(2)
            secs = float(secs) if secs else 0.0
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

    _vid_inventory = None

    def _dom_objects(self):
        return self.env.domaindata['res'].setdefault('objects', [])

    def lookup_video(self, name):
        if self._vid_inventory is None:
            path = Path('_build/inventory.csv')
            if path.exists():
                with path.open('r') as f:
                    self._vid_inventory = list(csv.DictReader(f))
            else:
                self._vid_inventory = []

        for vid in self._vid_inventory:
            if vid['Title'] == name:
                return vid

    def note_module(self, key, title, *, reset=True):
        docname = self.env.docname

        objs = self._dom_objects()

        if reset:
            objs = [o for o in objs if o.module != key]
            self.env.domaindata['res']['objects'] = objs

        mod = MediaObject(key, title, 'module', docname, key)
        objs.append(mod)

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
        # env.reporter.debug(f'searching for {type} {target} referenced from {fromdocname}')
        tgt = self._find_target(target, type)

        if not tgt:
            return None

        label = tgt.display_title
        cnode = XREF_TYPE_OVERRIDES.get(tgt.type, nodes.inline)
        content = cnode('', label)

        return make_refnode(builder, fromdocname, tgt.docname, tgt.anchor, content, tgt.name)

    def _find_target(self, target, type):
        tgt = self._find_key(target)
        if tgt is None:
            tgt = self._find_key(_make_id(f'{type}-{target}'))
        return tgt

    def _find_key(self, target):
        for candidate in self._dom_objects():
            if candidate.name == target:
                return candidate
