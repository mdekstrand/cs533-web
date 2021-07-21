"""
Sphinx extension to implement video support
"""

from pathlib import Path
from sphinx.application import Sphinx
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives


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

        video_id = self.options.get('id', None)
        length = self.options.get('length', None)
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
            sc = nodes.container("", is_div=True, classes=["tabbed-content"])

            sid = nodes.raw('', f"""
<div class=slide-container>
<iframe class=slide-embed src="https://onedrive.live.com/embed?resid={slide_id}&amp;authkey={slide_auth}&amp;em=2&amp;wdAr=1.7777777777777777" frameborder="0">This is an embedded <a target="_blank" href="https://office.com">Microsoft Office</a> presentation, powered by <a target="_blank" href="https://office.com/webapps">Office</a>.</iframe>
</div>
            """.strip(), format='html')
            sc += sid
            scc += sc
            result.append(scc)

        return result


def setup(app: Sphinx):
    app.add_directive('video', VideoDirective)
