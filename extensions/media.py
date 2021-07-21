"""
Sphinx extension to implement video support
"""

from sphinx.application import Sphinx
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives


class VideoDirective(Directive):
    option_spec = {
        'id': directives.unchanged,
        'name': directives.path,
    }

    def run(self):
        result = []

        video_id = self.options['id']
        if video_id:
            vcc = nodes.container("", type="tabbed", new_group=False, selected=False, classes=["tabbed-container", "video"])
            vl = nodes.rubric("Video", "Video", classes=["tabbed-label"])
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

        return result


def setup(app: Sphinx):
    app.add_directive('video', VideoDirective)
