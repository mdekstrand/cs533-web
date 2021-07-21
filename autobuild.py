"""
Auto-build the Jupyter book.
"""

import re
import subprocess
from livereload import Server, shell

_ignore_re = re.compile(r'^(\.[\\/])?_build[\\/]')

def rebuild():
    subprocess.run('jb build .', shell=True)

def ignore(p):
    return _ignore_re.match(p)

rebuild()
server = Server()
server.watch('.', rebuild, ignore=ignore)
server.serve(port=8000, root='_build/html/')
