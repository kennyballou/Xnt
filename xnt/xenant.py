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
import logging

sys.path.append(os.getcwd())
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s")
logger = logging.Logger(name=__name__)
logger.addHandler(logging.StreamHandler())

def main():
    args = sys.argv[1:]
    for arg in args:
        if arg == "version":
            printVersion()
        elif arg == "help":
            printVersion()
            print("\n")
            printTargets()
        elif arg == "-v":
            logging.getLogger("xnt.tasks").setLevel(logging.INFO)
        elif arg:
            target = arg
            invokeBuild(target)
        elif not arg:
            target = "default"
            invokeBuild(target)
    from xnt.tasks import rm
    rm("build.pyc")

def invokeBuild(targetName):
    if not os.path.exists("build.py"):
        logger.error("There was no build file")
        sys.exit(1)
    try:
        build = __import__("build", fromlist=[])
        target = getattr(build, targetName)
        target()
    except AttributeError:
        logger.warning("There was no target: %s", targetName)
    except:
        logger.error(sys.exc_info()[1].message)

def printVersion():
    import xnt
    print(xnt.__version__)

def printTargets():
    if not os.path.exists("build.py"):
        logger.error("There was no build file")
        sys.exit(1)
    try:
        build = __import__("build", fromlist=[])
        for f in dir(build):
            try:
                fa = getattr(build, f)
                if fa.decorator == "target":
                    print(f + ":")
                    if fa.__doc__:
                        print(fa.__doc__)
                    print("\n")
            except AttributeError:
                pass
    except AttributeError:
        pass
    except:
        logger.error(sys.exc_info()[1].message)

if __name__ == "__main__":
    main()
