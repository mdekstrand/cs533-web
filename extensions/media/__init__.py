from sphinx.application import Sphinx

from .domain import CourseDomain


def setup(app: Sphinx):
    app.add_domain(CourseDomain)

    return {
        'version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
