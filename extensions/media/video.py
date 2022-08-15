"""
Sphinx extension to implement video support
"""

from venv import create
import warnings
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import make_id
from sphinx_design.shared import create_component
import srt

_vid_root = Path('videos')


def rst_video_tab(video_id, length=None, title='Video', amara=None):
    tab = create_component('tab-item', classes=['sd-tab-item', 'video'])
    if length:
        title = title + f" ({length})"
    label = nodes.rubric("Video", title, classes=["sd-tab-label"])
    tab += label
    body = create_component('tab-content', classes=["sd-tab-content", "player"])

    vid = nodes.raw('', f"""
<div class="video-container video-embed">
<iframe src="https://boisestate.hosted.panopto.com/Panopto/Pages/Embed.aspx?id={video_id}&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>
</div>
    """.strip(), format='html')
    body += vid
    tab += body

    if amara and False:  # drop amara links
        label = nodes.paragraph("", classes=['aux-links'])
        amr = nodes.reference('', '', classes=['amara'], internal=False)
        amr['refuri'] = amara
        amr += nodes.inline('', 'Edit subtitles on Amara')
        label += amr
        body += label

    return tab


def rst_slide_tab(slide_id, slide_auth):
    tab = create_component('tab-item', classes=['sd-tab-item', 'slides'])
    label = nodes.rubric("Slides", "Slides", classes=["sd-tab-label"])
    tab += label
    body = create_component('tab-content', classes=["sd-tab-content", "slides"])

    sid = nodes.raw('', f"""
<div class=slide-container data-id="{slide_id}" data-key={slide_auth}>
</div>
    """.strip(), format='html')
    body += sid
    tab += body
    return tab


class VideoDirective(SphinxDirective):
    option_spec = {
        'id': directives.unchanged,
        'slide-id': directives.unchanged,
        'slide-auth': directives.unchanged,
        'length': directives.unchanged,
        'name': directives.path,
        'amara': directives.path,
        'alt-id': directives.unchanged,
        'alt-title': directives.unchanged,
        'alt-amara': directives.path,
    }
    has_content = True
    required_arguments = 0
    optional_arguments = 1

    def _get_video(self):
        name = self.options.get('name', None)
        if name:
            dom = self.env.get_domain('res')
            return dom.lookup_video(name)

    def _get_param(self, name, inv_name):
        res = self.options.get(name, None)
        if not res:
            vid = self._get_video()
            if vid:
                res = vid[inv_name]

        return res

    def run(self):
        result = []

        name = self.options.get('name', None)
        video_id = self._get_param('id', 'Panopto ID')
        length = self.options.get('length', None)
        key = None
        if self.arguments:
            key = self.arguments[0].strip()
        if not key:
            key = make_id(self.env, self.state.document, 'video', name)

        dom = self.env.get_domain('res')

        if video_id:
            tgt_node = nodes.target('', '', ids=[video_id])
            self.set_source_info(tgt_node)
            result.append(tgt_node)
            dom.note_video(key, video_id, name, length)
        else:
            w = self.state.reporter.error(f'Video name {name} has no video ID')
            result.append(w)

        box = create_component(
            'tab-set', classes=['sd-tab-set', 'resource', 'video']
        )
        result.append(box)

        if video_id:
            box += rst_video_tab(video_id, length, amara=self._get_param('amara', 'Amara URL'))

        slide_id = self._get_param('slide-id', 'Slide ID')
        if slide_id:
            slide_auth = self._get_param('slide-auth', 'Slide Auth')
            box += rst_slide_tab(slide_id, slide_auth)

        alt_id = self.options.get('alt-id', None)
        if alt_id:
            box += rst_video_tab(alt_id, title=self.options['alt-title'], amara=self.options.get('alt-amara', None))

        if self.content:
            res_tab = create_component('tab-item', classes=['sd-tab-item'])
            rt_label = nodes.rubric("Resources and Links", "Resources and Links", classes=["sd-tab-label"])
            res_tab += rt_label
            rt_content = create_component('tab-content', classes=['sd-tab-content', 'resources'])
            self.state.nested_parse(self.content, self.content_offset, rt_content)

            res_tab += rt_content
            box += res_tab

        if name:
            tfile = _vid_root / f'{name}.slides.txt'
            if tfile.exists():
                text = tfile.read_text(encoding='utf8')
                hid = nodes.container('', is_div=True, classes=['slides', 'text', 'hidden'])
                tn = nodes.Text(text)
                hid += tn
                result.append(hid)

            sffile = _vid_root / f'{name}.srt'
            if sffile.exists():
                subs = srt.parse(sffile.read_text(encoding='utf8'))
                hid = nodes.container('', is_div=True, classes=['captions', 'text', 'hidden'])
                kids = nodes.bullet_list()
                for sub in subs:
                    tn = nodes.Text(sub.content)
                    kids += nodes.list_item('', tn)
                hid += kids
                result.append(hid)
            else:
                w = self.state.reporter.warning(f'Video file {name}.srt does not exist')
                result.append(w)

        return result
