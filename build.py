#!/usr/bin/env python

from xnt import target
from xnt.tasks import *
import xnt.tasks

@target
def clean():
    """Removes Generated folders"""
    rm("Xnt.egg-info",
       "build",
       "docs/build",
       "dist",
       "README.html",
       "**/*.pyc",
       "**/**/*.pyc")

@target
def build():
    setup(["build"])

@target
def test():
    """Tests package"""
    print("Python Tests:")
    setup(["test"])
    clean()
    print("Python2 Tests:")
    call(["python2", "setup.py", "test"])
    clean()

@target
def install():
    """Install Xnt"""
    setup(["install", "--user"])
    clean()

@target
def doc():
    """
    Create package documentation
    """
    clean()
    setup(["build_sphinx"])
