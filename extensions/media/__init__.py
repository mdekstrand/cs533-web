from sphinx.application import Sphinx

from .domain import CourseDomain
from .nav import eomjify_toc


def setup(app: Sphinx):
    app.add_domain(CourseDomain)

    # app.connect('env-updated', eomjify_toc)

    return {
        'version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
