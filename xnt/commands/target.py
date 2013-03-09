#!/usr/bin/env python
"""(Generic) Target Xnt Command for invoking build targets"""

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
from xnt.status_codes import SUCCESS, ERROR, UNKNOWN_ERROR
import logging

LOGGER = logging.getLogger("xnt")

class TargetCommand(Command):
    """Target Command"""
    name = '<target>'
    usage = """"""
    summary = "Invokes target(s) in build.py"
    needs_build = True

    def __init__(self, build):
        """Initialization"""
        Command.__init__(self)
        self.build = build

    def run(self, targets=None, props=None): #pylint: disable-msg=W0221
        """Invoke Target Command"""
        if targets:
            for target in targets:
                error_code = self.call_target(target, props)
                if error_code:
                    return error_code
            return SUCCESS
        else:
            return self.call_target("default", props)

    def call_target(self, target_name, props):
        """Invoke build target"""
        def process_params(params, buildproperties=None):
            """Parse the passed properties and append to build properties"""
            properties = buildproperties if buildproperties is not None else {}
            for param in params:
                name, value = param[2:].split("=")
                properties[name] = value
            return properties
        def __get_properties():
            """Return the properties dictionary of the build module"""
            try:
                return getattr(self.build, "properties")
            except AttributeError:
                return None
        try:
            if props and len(props) > 0:
                setattr(self.build,
                        "properties",
                        process_params(props, __get_properties()))
            target = getattr(self.build, target_name)
            error_code = target()
            return error_code if error_code else 0
        except AttributeError:
            LOGGER.warning("There was no target: %s", target_name)
            return ERROR
        except Exception as ex:
            LOGGER.error(ex)
            return UNKNOWN_ERROR

