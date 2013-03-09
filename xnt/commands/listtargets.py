#!/usr/bin/env python
"""List Targets Xnt Command"""

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

from xnt.basecommand import Command
from xnt.status_codes import SUCCESS, ERROR
import logging

LOGGER = logging.getLogger(__name__)

class ListTargetsCommand(Command):
    """List Targets Command"""
    name = 'list-targets'
    usage = """"""
    summary = "Prints targets in build file"
    needs_build = True

    def __init__(self, build):
        """Initialization"""
        Command.__init__(self)
        self.build = build

    def run(self, arguments=None):
        """Invoke ListTargets"""
        LOGGER.debug("build is null? %s", self.build == None)
        try:
            for attr in dir(self.build):
                LOGGER.debug("Attribute %s:", attr)
                try:
                    func = getattr(self.build, attr)
                    if func.decorator == "target":
                        print(attr + ":")
                        if func.__doc__:
                            print(func.__doc__)
                        print("\n")
                except AttributeError:
                    pass
        except AttributeError as ex:
            LOGGER.error(ex)
            return ERROR
        return SUCCESS
