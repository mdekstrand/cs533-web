import re
import warnings
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util import UnicodeDecodeErrorHandler
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import make_id
import srt


class BookDirective(SphinxDirective):
    option_spec = {
        'title': directives.path,
        'author': directives.unchanged,
        'publisher': directives.unchanged,
        'isbn': directives.path,
        'edition': directives.unchanged,
    }
    required_arguments = 1
    optional_arguments = 1
    has_content = True

    def run(self):
        key = self.arguments[0].strip()
        title = self.options['title']
        edition = self.options.get('edition', None)
        author = self.options['author']
        publisher = self.options['publisher']
        isbn = self.options.get('isbn', None)

        anchor = f'book-{key}'
        dom = self.env.get_domain('res')
        dom.note_object('book', key, title, anchor)

        box = nodes.container('', is_div=True, classes=['book'])

        # Link target
        tgt_node = nodes.target('', '', ids=[anchor])
        self.set_source_info(tgt_node)
        box += tgt_node

        # Render the citation
        cite = nodes.paragraph('', classes=['book', 'citation'])
        cite += nodes.title_reference('', title)
        if edition:
            cite += nodes.inline('', ', ' + edition)
        cite += nodes.inline('', ' by ')
        cite += nodes.inline('', author)
        cite += nodes.inline('', ' (')
        cite += nodes.inline('', publisher)
        if isbn:
            cite += nodes.inline('', ', ISBN ')
            cite += nodes.inline('', isbn)
        cite += nodes.inline('', ').')
        box += cite

        # parse content
        if self.content:
            notes = nodes.container('', is_div=True)
            self.state.nested_parse(self.content, self.content_offset, notes)
            box += notes

        return [box]

