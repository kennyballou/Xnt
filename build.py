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
       "**/**/*.pyc",
       "**__pycache__")

@target
def build():
    return setup(["build"])

@target
def test():
    """Tests package"""
    print("Python Tests:")
    ec1 = setup(["test"])
    clean()
    print("Python2 Tests:")
    ec2 = call(["python2", "setup.py", "test"])
    clean()
    return ec1 | ec2

@target
def install():
    """Install Xnt"""
    ec = setup(["install", "--user"])
    clean()
    return ec

@target
def doc():
    """
    Create package documentation
    """
    clean()
    return setup(["build_sphinx"])
