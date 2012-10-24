#!/usr/bin/env python

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
            import xnt
            print(xnt.__version__)
            sys.exit()
        elif arg:
            target = arg
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

if __name__ == "__main__":
    main()
