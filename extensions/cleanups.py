from sphinx.application import Sphinx
from pydata_sphinx_theme import BootstrapHTML5Translator


def setup(app: Sphinx):
    app.set_translator('dirhtml', BootstrapHTML5Translator)

    return {
        'version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
