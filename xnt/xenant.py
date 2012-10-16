#!/usr/bin/env python

import os
import sys

sys.path.append(os.getcwd())

def main():
    if len(sys.argv[1:]) < 1:
        target = "default"
    else:
        target = sys.argv[1]
    invokeBuild(target)

def invokeBuild(targetName):
    if not os.path.exists("build.py"):
        sys.stderr.write("There was no build file")
        sys.exit(1)
    try:
        build = __import__("build", fromlist=[])
        target = getattr(build, targetName)
        target()
    except AttributeError:
        sys.stderr.write("No such target: " + targetName)
    except:
        print(sys.exc_info())

if __name__ == "__main__":
    main()
