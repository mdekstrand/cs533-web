"""
Sphinx extension for custom admonitions.
"""

from sphinx.application import Sphinx
from docutils import nodes
from docutils.parsers.rst.directives.admonitions import Warning


def setup(app: Sphinx):
    app.add_directive('draft', Warning)
