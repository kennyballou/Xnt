#!/usr/bin/env python

import xnt

@xnt.target
def clean():
    """Removes Generated folders"""
    xnt.rm("Xnt.egg-info",
           "build",
           "docs/build",
           "dist",
           "README.html",
           "**/*.pyc",
           "**/**/*.pyc",
           "**__pycache__",
           "**/**/__pycache__")

@xnt.target
def build():
    return xnt.setup(["build"])

@xnt.target
def test():
    """Tests package"""
    print("Python Tests:")
    ec1 = xnt.setup(["test"])
    clean()
    print("Python2 Tests:")
    ec2 = xnt.call(["python2", "setup.py", "test"])
    clean()
    return ec1 | ec2

@xnt.target
def install():
    """Install Xnt"""
    ec = xnt.setup(["install", "--user"])
    clean()
    return ec

@xnt.target
def doc():
    """
    Create package documentation
    """
    clean()
    return xnt.setup(["build_sphinx"])
