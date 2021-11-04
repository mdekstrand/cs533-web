import logging
import re
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx import addnodes
from docutils import nodes

_log = logging.getLogger(__name__)

_week_re = re.compile(r'^week\d+/index')
_asn_re = re.compile(r'^assignments/A\d+/index')


def eomjify_toc(app: Sphinx, env: BuildEnvironment):
    _log.info('adding emoji to TOC')

    # for name in env.titles:
    #     _log.debug('checking document %s', name)
    #     title = env.titles[name]
    #     txt = title.astext()
    #     new = None
    #     if _week_re.match(name):
    #         print('fixing week', name)
    #         new = f'🧩 {txt}'
    #     elif _asn_re.match(name):
    #         new = f'📩 {txt}'

    #     if new:
    #         nt = nodes.title()
    #         nt += nodes.Text(new)
    #         env.titles[name] = nt

    for tt in env.tocs['index'].traverse(addnodes.toctree):
        entries = tt['entries']
        for i in range(len(entries)):
            title, path = entries[i]
            print(path, str(title).encode('ascii', errors='replace'))
            if title:
                continue

            _log.debug('checking document %s', path)
            txt = env.titles[path].astext()
            new = None
            if _week_re.match(path):
                print('fixing week', path)
                new = f'🧩 {txt}'
            elif _asn_re.match(path):
                new = f'📩 {txt}'

            if new:
                entries[i] = (new, path)

