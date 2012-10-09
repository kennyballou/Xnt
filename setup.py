#!/usr/bin/env python

import os
import shutil
from distutils.core import setup

def read(fname):
    return "\n" + open(os.path.join(os.path.dirname(__file__), fname)).read()

shutil.copy2("README.markdown", "README")

setup(
    name="Xnt",
    version="0.1.0",
    author="Kenny Ballou",
    author_email="kennethmgballou@gmail.com",
    url="https://bitbucket.org/devnulltao/xnt",
    description=("High-Level build script for doing more complex build tasks"),
    license="gpl3",
    keywords="Build Scripts",
    packages=["xnt",],
    scripts=["Xnt.py",],
    package_data={
    },
    long_description=read("README.markdown"),
    platforms=["Linux",],
)
