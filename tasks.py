import os
import sys
from pathlib import Path
import tarfile
import shutil

from invoke import task

BRANCH = 'archive'
CURRENT = 'F21'
BUILD_DIR = Path('_build')
FULL_DIR = BUILD_DIR / 'site'
CUR_DIR = BUILD_DIR / 'html'
CUR_DEPLOY_DIR = FULL_DIR / CURRENT


def _msg(fmt, *args):
    print(fmt % args, file=sys.stderr)


@task
def build(c, rebuild=False):
    """
    Build the current site.
    """
    if rebuild:
        c.run('jb build --all .')
    else:
        c.run('jb build .')


@task
def copy_archive(c):
    archive_path = BUILD_DIR / 'archive.tar'
    p = archive_path.as_posix()

    FULL_DIR.mkdir(exist_ok=True, parents=True)

    _msg('creating git archive')
    c.run(f'git archive -o {p} archive')

    with tarfile.open(archive_path) as tf:
        _msg('extracting %s', archive_path)
        tf.extractall(FULL_DIR)


@task(pre=[copy_archive])
def copy_root(c):
    _msg('copying static root files')
    shutil.copytree('_root', FULL_DIR, dirs_exist_ok=True)


@task(pre=[build, copy_root])
def build_site(c):
    _msg('copying current tree to site target')
    shutil.copytree(CUR_DIR, CUR_DEPLOY_DIR, dirs_exist_ok=True)
