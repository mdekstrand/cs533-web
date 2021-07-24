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

_vid_root = Path('videos')


class VideoDirective(Directive):
    option_spec = {
        'id': directives.unchanged,
        'slide-id': directives.unchanged,
        'slide-auth': directives.unchanged,
        'length': directives.unchanged,
        'name': directives.path,
    }

    def run(self):
        result = []

        name = self.options.get('name', None)
        video_id = self.options.get('id', None)
        length = self.options.get('length', None)

        # tgt = nodes.target(text=name)
        # result.append(tgt)

        if video_id:
            vcc = nodes.container("", type="tabbed", new_group=False, selected=False, classes=["tabbed-container", "video"])
            title = "Video"
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
            result.append(vcc)

        slide_id = self.options.get('slide-id', None)
        if slide_id:
            slide_auth = self.options['slide-auth']
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
            result.append(scc)

        if name:
            tfile = _vid_root / f'{name}.txt'
            if tfile.exists():
                text = tfile.read_text(encoding='utf8')
                hid = nodes.container('', is_div=True, classes=['slides', 'text', 'hidden'])
                tn = nodes.Text(text)
                hid += tn
                result.append(hid)

        return result


class CourseDomain(Domain):
    name = 'res'

    def __init__(self, env: "BuildEnvironment") -> None:
        super().__init__(env)
        self.add_object_type('video', ObjType('video', ('video',)))


def setup(app: Sphinx):
    app.add_domain(CourseDomain)
    app.add_directive('video', VideoDirective)
    # app.add_role('video', AnyXRefRole(innernodeclass=nodes.inline))
