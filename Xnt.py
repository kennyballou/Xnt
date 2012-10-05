#!/usr/bin/env python

import os
import sys

def main(target=""):
    if not os.path.exists("build.py"):
        sys.stderr.write("There was no build file")
        sys.exit(1)
    invokeBuild(target)

def invokeBuild(targetName):
    try:
        build = __import__("build", fromlist=[])
        target = getattr(build, targetName)
        target()
    except AttributeError:
        sys.stderr.write("No such target: " + targetName)
    except:
        sys.stderr.write("Something more wrong went wrong")

if __name__ == "__main__":
    main(sys.argv[1])
