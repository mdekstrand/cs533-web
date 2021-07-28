"""
Sphinx extension to implement video support
"""

from logging import warn
from pathlib import Path
from sphinx.application import Sphinx
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from sphinx.domains import Domain, ObjType
import srt

_vid_root = Path('videos')


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


class VideoDirective(Directive):
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

    def run(self):
        result = []

        name = self.options.get('name', None)
        video_id = self.options.get('id', None)
        length = self.options.get('length', None)

        # tgt = nodes.target(text=name)
        # result.append(tgt)

        if video_id:
            result.append(rst_video_tab(video_id, length))

        slide_id = self.options.get('slide-id', None)
        if slide_id:
            slide_auth = self.options['slide-auth']
            result.append(rst_slide_tab(slide_id, slide_auth))

        alt_id = self.options.get('alt-id', None)
        if alt_id:
            result.append(rst_video_tab(alt_id, title=self.options['alt-title']))

        if self.content:
            rcc = nodes.container("", type="tabbed", new_group=False, selected=False,
                                  classes=["tabbed-container"])
            rl = nodes.rubric("Resources and Links", "Resources and Links", classes=["tabbed-label"])
            rcc += rl
            rc = nodes.container("", is_div=True, classes=["tabbed-content", "resources"])
            self.state.nested_parse(self.content, self.content_offset, rc)

            rcc += rc
            result.append(rcc)

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

        return result


class CourseDomain(Domain):
    name = 'res'
    label = 'Course'

    object_types = {
        'video': ObjType('video', 'video')
    }


def setup(app: Sphinx):
    app.add_domain(CourseDomain)
    app.add_directive('video', VideoDirective)
    # app.add_role('video', AnyXRefRole(innernodeclass=nodes.inline))
