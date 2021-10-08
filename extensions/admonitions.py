"""
Sphinx extension for custom admonitions.
"""

from sphinx.application import Sphinx
from docutils import nodes
from docutils.parsers.rst.directives.admonitions import BaseAdmonition, Admonition


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


class LTip(Admonition):

    def run(self):
        if 'classes' not in self.options:
            self.options['classes'] = []
        self.options['classes'].append('tip')

        return super().run()


class LNote(Admonition):

    def run(self):
        if 'classes' not in self.options:
            self.options['classes'] = []
        self.options['classes'].append('note')

        return super().run()


def setup(app: Sphinx):
    app.add_directive('draft', Draft)
    app.add_directive('ltip', LTip)
    app.add_directive('lnote', LTip)
