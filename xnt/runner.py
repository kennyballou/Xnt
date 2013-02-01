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
import logger

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s")
logger = logging.Logger(name=__name__)
logger.addHandler(logging.StreamHandler())

def main():
    start_time = time.time()
    params = list(p for p in sys.argv[1:] if p.startswith('-D'))
    flags = list(o for o in sys.argv[1:]
        if o.startswith('-') and o not in params)
    commands = list(c for c in sys.argv[1:]
        if c not in opts and c not in params)
    #run things
    elapsed_time = time.time() - start_time
    logger.info("Execution time: %.3f", elapsed_time)
    logger.info("Success" if ec == 0 else "Failure")
    from xnt.tasks import rm
    rm("build.pyc",
       "__pycache__")
    if ec != 0:
        sys.exit(ec)

if __name__ == "__main__":
    ec = main()
    if ec:
        sys.exit(ec)
