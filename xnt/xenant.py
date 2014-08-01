#!/usr/bin/env python
"""Xnt Runner Script"""

#   Xnt -- A Wrapper Build Tool
#   Copyright (C) 2013  Kenny Ballou

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
import argparse
import xnt
import xnt.verbose

logging.basicConfig(format="%(message)s")
LOGGER = logging.Logger(name=__name__)
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.WARNING)

def main():
    """Xnt Entry Point"""
    start_time = time.time()
    args = parse_args(sys.argv[1:])
    build_file = "./build.py"
    if args["verbose"]:
        xnt.verbose.VERBOSE = True
        LOGGER.setLevel(logging.INFO)
        logging.getLogger("xnt.tasks").setLevel(logging.INFO)
    if args["build-file"]:
        build_file = args["build-file"]
    if args["list-targets"]:
        error_code = xnt.list_targets(build_file)
    else:
        error_code = xnt.xntcall(build_file,
                                 args["targets"],
                                 args["properties"])
    elapsed_time = time.time() - start_time
    print("Execution time: %.3f" % elapsed_time)
    if error_code != 0:
        LOGGER.error("Failure")
    xnt.rm("build.pyc",
           "__pycache__",
           build_file + "c",
           os.path.join(os.path.dirname(build_file), "__pycache__"))
    if error_code != 0:
        sys.exit(error_code)

def parse_args(args_in):
    """Parse and group arguments"""
    parser = argparse.ArgumentParser(prog="Xnt")
    parser.add_argument("-v", "--verbose",
                        help="be verbose",
                        action="store_true",
                        dest="verbose")
    parser.add_argument(
        "--version",
        action="version",
        version=xnt.__version__,
        help="print the version information and quit")
    parser.add_argument(
        "-b", "--build-file",
        dest="build-file",
        help="use the given buildfile")
    parser.add_argument("-l", "--list-targets",
                        action="store_true",
                        dest="list-targets",
                        help="print build targets")
    # Properties Group
    params_group = parser.add_argument_group("Properties")
    params_group.add_argument(
        "-D", dest="properties", action="append",
        help="use value for gvien property")
    target_group = parser.add_argument_group("Targets")

    # Targets Group
    target_group.add_argument("targets", nargs=argparse.REMAINDER,
                              help="name(s) of targets to invoke")
    return vars(parser.parse_args(args_in))

if __name__ == "__main__":
    main()
