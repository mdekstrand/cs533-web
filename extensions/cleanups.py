from sphinx.application import Sphinx
from pydata_sphinx_theme import BootstrapHTML5Translator


def setup(app: Sphinx):
    app.set_translator('dirhtml', BootstrapHTML5Translator)
