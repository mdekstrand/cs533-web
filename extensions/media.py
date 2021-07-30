"""
Sphinx extension to implement video support
"""

import warnings
from typing import NamedTuple
import re
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.roles import XRefRole
from sphinx.transforms import SphinxTransform
from sphinx.util.nodes import make_id, make_refnode
from sphinx.domains import Domain, ObjType
import srt

_vid_root = Path('videos')
_vl_re = re.compile(r'(\d+)m(\d+)s')
_pfx_re = re.compile('^(\d+-\d+\s+-\s+)?(.*)')


class Video(NamedTuple):
    id: str
    key: str
    docname: str
    module: str
    name: str
    length: str

    EMOJI = '🎥'

    @property
    def short_name(self):
        trunc = _pfx_re.match(self.name)
        return trunc.group(2)

    def label(self):
        return f'{self.EMOJI} {self.short_name}'

    def vid_length(self):
        if self.length:
            m = _vl_re.match(self.length)
            mins = float(m.group(1))
            secs = float(m.group(2))
            return mins * 60 + secs


def rst_video_tab(video_id, length=None, title='Video'):
    vcc = nodes.container("", type="tabbed", new_group=False, selected=False, classes=["tabbed-container", "video"])
    if length:
        title += f" ({length})"
    vl = nodes.rubric("Video", title, classes=["tabbed-label"])
    vcc += vl
    vc = nodes.container("", is_div=True, classes=["tabbed-content", "player"])

    vid = nodes.raw('', f"""
<div class="video-container video-embed">
<iframe src="https://boisestate.hosted.panopto.com/Panopto/Pages/Embed.aspx?id={video_id}&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>
</div>
    """.strip(), format='html')
    vc += vid
    vcc += vc
    return vcc


def rst_slide_tab(slide_id, slide_auth):
    scc = nodes.container("", type="tabbed", new_group=False, selected=False, classes=["tabbed-container", "slides"])
    sl = nodes.rubric("Slides", "Slides", classes=["tabbed-label"])
    scc += sl
    sc = nodes.container("", is_div=True, classes=["tabbed-content", "slides"])

    sid = nodes.raw('', f"""
<div class=slide-container data-id="{slide_id}" data-key={slide_auth}>
</div>
    """.strip(), format='html')
    sc += sid
    scc += sc
    return scc


class ModuleDirective(SphinxDirective):
    required_arguments = 1
    optional_arguments = 0
    has_content = False
    option_spec = {
        'playlist': directives.path
    }

    def run(self):
        name = self.arguments[0].strip()
        self.env.ref_context['res:module'] = name
        pending = nodes.pending(ModTocTransform, {
            'module': name,
            'playlist': self.options.get('playlist')
        })
        self.state.document.note_pending(pending, 500)
        return [pending]


class ModTocTransform(SphinxTransform):
    def apply(self, **kwargs):
        mod = self.startnode.details['module']
        box = nodes.container('', is_div=True, classes=['module-content'])

        table = nodes.table(classes=['colwidths-auto'])
        tg = nodes.tgroup(cols=2)
        tg += nodes.colspec(colwidth=1)
        tg += nodes.colspec(colwidth=0)
        table += tg
        head = nodes.thead()
        hrow = nodes.row()
        head += hrow
        hrow += nodes.entry('', nodes.strong('', 'Element'))
        hrow += nodes.entry('', nodes.strong('', 'Length'))
        tg += head

        tb = nodes.tbody()
        tg += tb

        tot_vid = 0.0

        for obj in self.env.domaindata['res']['objects']:
            if obj.module != mod:
                continue

            if hasattr(obj, 'vid_length'):
                vl = obj.vid_length()
                if vl:
                    tot_vid += vl

            row = nodes.row()

            l_cell = nodes.entry()
            ref = nodes.reference('', '', internal=True)
            ref['refid'] = obj.id
            ref += nodes.inline('', obj.label())
            l_cell += nodes.paragraph('', '', ref)
            row += l_cell

            len_cell = nodes.entry()
            if hasattr(obj, 'length'):
                len_cell += nodes.inline('', obj.length)
            row += len_cell
            tb += row

        box += table

        summary = nodes.paragraph()
        summary += nodes.inline('', 'This week has ')
        summary += nodes.strong('', '%dh%.0fm' % (int(tot_vid / 3600), tot_vid % 3600 / 60))
        summary += nodes.inline('', ' of video.')

        playlist = self.startnode.details.get('playlist', None)
        if playlist:
            summary += nodes.inline('', " This week's videos are available as a ")
            plref = nodes.reference('', '', classes=['panopto'])
            plref['refuri'] = playlist
            plref += nodes.inline('', 'Panopto playlist')
            summary += plref
            summary += nodes.inline('', ".")

        box += summary

        parent = self.startnode.parent
        parent.replace(self.startnode, box)


class VideoDirective(SphinxDirective):
    option_spec = {
        'id': directives.unchanged,
        'slide-id': directives.unchanged,
        'slide-auth': directives.unchanged,
        'length': directives.unchanged,
        'name': directives.path,
        'alt-id': directives.unchanged,
        'alt-title': directives.unchanged,
    }
    has_content = True
    required_arguments = 0
    optional_arguments = 1

    def run(self):
        result = []

        modname = self.env.ref_context.get('res:module')
        name = self.options.get('name', None)
        video_id = self.options.get('id', None)
        length = self.options.get('length', None)
        if self.arguments:
            key = self.arguments[0].strip()
        else:
            key = name
        fullkey = f'{modname}:{key}' if modname else key
        target = video_id if video_id else fullkey

        tgt_node = nodes.target('', '', ids=[target])
        self.set_source_info(tgt_node)
        result.append(tgt_node)
        vid_obj = Video(video_id, fullkey, self.env.docname, modname, name, length)
        objects = self.env.domaindata['res'].setdefault('objects', [])
        objects.append(vid_obj)

        box = nodes.container('', classes=["resource", "video"])
        result.append(box)

        if video_id:
            box += rst_video_tab(video_id, length)
        else:
            warnings.warn('no video ID specified')

        slide_id = self.options.get('slide-id', None)
        if slide_id:
            slide_auth = self.options['slide-auth']
            box += rst_slide_tab(slide_id, slide_auth)

        alt_id = self.options.get('alt-id', None)
        if alt_id:
            box += rst_video_tab(alt_id, title=self.options['alt-title'])

        if self.content:
            rcc = nodes.container("", type="tabbed", new_group=False, selected=False,
                                  classes=["tabbed-container"])
            rl = nodes.rubric("Resources and Links", "Resources and Links", classes=["tabbed-label"])
            rcc += rl
            rc = nodes.container("", is_div=True, classes=["tabbed-content", "resources"])
            self.state.nested_parse(self.content, self.content_offset, rc)

            rcc += rc
            box += rcc

        if name:
            tfile = _vid_root / f'{name}.slides.txt'
            if tfile.exists():
                text = tfile.read_text(encoding='utf8')
                hid = nodes.container('', is_div=True, classes=['slides', 'text', 'hidden'])
                tn = nodes.Text(text)
                hid += tn
                box += hid

            sffile = _vid_root / f'{name}.srt'
            if sffile.exists():
                subs = srt.parse(sffile.read_text(encoding='utf8'))
                hid = nodes.container('', is_div=True, classes=['captions', 'text', 'hidden'])
                kids = nodes.bullet_list()
                for sub in subs:
                    tn = nodes.Text(sub.content)
                    kids += nodes.list_item('', tn)
                hid += kids
                box += hid

        return result


class CourseDomain(Domain):
    name = 'res'
    label = 'Course'

    object_types = {
        'video': ObjType('video', 'video')
    }
    directives = {
        'module': ModuleDirective,
        'video': VideoDirective,
    }
    roles = {
        'video': XRefRole()
    }

    def resolve_xref(self, env, fromdocname, builder, type, target, node, contnode):
        objects = env.domaindata['res'].get('objects', [])

        tgt = None
        for candidate in objects:
            if candidate.key == target:
                tgt = candidate

        if not tgt:
            return None

        label = tgt.label()
        content = nodes.inline('', label)

        return make_refnode(builder, fromdocname, tgt.docname, tgt.id, content, tgt.name)


def setup(app: Sphinx):
    app.add_domain(CourseDomain)

    # app.add_directive('video', VideoDirective)
    # app.add_role('video', AnyXRefRole(innernodeclass=nodes.inline))
