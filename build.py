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
    error_codes = []
    print("Python Tests:")
    error_codes.append(xnt.setup(["test"]))
    clean()
    if xnt.in_path("python2"):
        print("Python2 Tests:")
        error_codes.append(xnt.call(["python2", "setup.py", "test"]))
        clean()
    return sum(error_codes)

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
    return xnt.setup(["build_sphinx"])
