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

from xnt.basecommand import Command, SUCCESS, ERROR
from xnt.xenant import loadBuild
import logging

logger = logging.getLogger("xnt")

class ListTargetsCommand(Command):
    name = 'list-targets'
    usege = """"""
    summary = "Prints targets in build file"

    def run(self, arguments=[]):
        build = loadBuild
        try:
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
        except Exception as ex:
            logger.error(ex)
            return ERROR
        return SUCCESS
        except Exception as ex:
            logger.error(ex)
            return ERROR
