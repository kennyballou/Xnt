#!/usr/bin/env python

#   Xnt -- A Wrapper Build Tool
#   Copyright (C) 2012  Kenny Ballou

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import time
import logging

logger = logging.getLogger(__name__)

def loadBuild(path=""):
    if not path:
        path = os.getcwd()
    else:
        path = os.path.abspath(path)
    sys.path.append(path)
    cwd = os.getcwd()
    os.chdir(path)
    if not os.path.exists("build.py"):
        logger.error("There was no build file")
        sys.exit(1)
    try:
        return __import__("build", fromlist=[])
    except ImportError:
        logger.error("HOW?!")
        return None
    finally:
        sys.path.remove(path)
        del sys.modules["build"]
        os.chdir(cwd)
