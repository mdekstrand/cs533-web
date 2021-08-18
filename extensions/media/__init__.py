from sphinx.application import Sphinx

from .domain import CourseDomain


def setup(app: Sphinx):
    app.add_domain(CourseDomain)
