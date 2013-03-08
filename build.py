#!/usr/bin/env python
"""Xnt Build File"""

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
    """Build Xnt"""
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
def lint():
    """pylint xnt"""
    return xnt.call(["pylint", "--rcfile=pylint.conf", "xnt"])

@xnt.target
def install():
    """Install Xnt"""
    error_code = xnt.setup(["install", "--user"])
    clean()
    return error_code

@xnt.target
def doc():
    """
    Create package documentation
    """
    clean()
    return xnt.setup(["build_sphinx"])
