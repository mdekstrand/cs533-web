import warnings
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util import UnicodeDecodeErrorHandler
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import make_id
import srt


class ReadingDirective(SphinxDirective):
    option_spec = {
        'url': directives.path,
        'title': directives.unchanged,
        'length': directives.unchanged,
    }
    required_arguments = 0
    optional_arguments = 1

    def run(self):
        url = self.options.get('url', None)
        title = self.options.get('title', None)
        length = self.options.get('length', None)

        key = self.arguments[0].strip() if self.arguments else None

        if not key:
            key = make_id(self.env, self.state.document, 'reading', title)

        dom = self.env.get_domain('res')
        dom.note_reading(key, title, length)

        tgt_node = nodes.target('', '', ids=[key])
        self.set_source_info(tgt_node)

        return [tgt_node]

