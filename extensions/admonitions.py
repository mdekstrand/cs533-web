"""
Sphinx extension for custom admonitions.
"""

from sphinx.application import Sphinx
from docutils import nodes
from docutils.parsers.rst.directives.admonitions import BaseAdmonition


class Draft(BaseAdmonition):
    node_class = nodes.admonition

    def run(self):
        text = '\n'.join(self.content)
        attrs = {'classes': ['warning']}
        node = nodes.admonition(text, **attrs)
        title = nodes.title('', 'Draft')
        node += title

        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


def setup(app: Sphinx):
    app.add_directive('draft', Draft)
