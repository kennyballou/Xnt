#!/usr/bin/env python
"""Xnt Runner Script"""

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
from xnt.cmdoptions import OPTIONS
from xnt.commands import COMMANDS
from xnt.commands.target import TargetCommand

logging.basicConfig(format="%(message)s")
LOGGER = logging.Logger(name=__name__)
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.WARNING)

def main():
    """Xnt Entry Point"""
    start_time = time.time()
    params = list(p for p in sys.argv[1:] if p.startswith('-D'))
    flags = list(o for o in sys.argv[1:]
        if o.startswith('-') and o not in params)
    cmds = list(c for c in sys.argv[1:]
        if c not in flags and c not in params)
    #Loop flags and apply them
    for flag in flags:
        if flag in OPTIONS:
            OPTIONS[flag]()
        else:
            LOGGER.debug("%s is not a vaild option", flag)
    #run things
    cmd_found = False
    for cmd in cmds:
        if cmd in COMMANDS:
            cmd_found = True
            if COMMANDS[cmd].needs_build:
                command = COMMANDS[cmd](load_build())
            else:
                command = COMMANDS[cmd]()
            error_code = command.run()
    if cmd_found == False:
        command = TargetCommand(load_build())
        error_code = command.run(targets=cmds, props=params)
    elapsed_time = time.time() - start_time
    print("Execution time: %.3f", elapsed_time)
    if error_code != 0:
        LOGGER.error("Failure")
    from xnt.tasks import rm
    rm("build.pyc",
       "__pycache__")
    if error_code != 0:
        sys.exit(error_code)

def load_build(path=""):
    """Load build file

    Load the build.py and return the resulting import
    """
    if not path:
        path = os.getcwd()
    else:
        path = os.path.abspath(path)
    sys.path.append(path)
    cwd = os.getcwd()
    os.chdir(path)
    if not os.path.exists("build.py"):
        LOGGER.error("There was no build file")
        sys.exit(1)
    try:
        return __import__("build", fromlist=[])
    except ImportError:
        LOGGER.error("HOW?!")
        return None
    finally:
        sys.path.remove(path)
        del sys.modules["build"]
        os.chdir(cwd)

if __name__ == "__main__":
    main()
