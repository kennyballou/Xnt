#!/usr/bin/env python
"""CVS Version Control Wrapper"""

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
from xnt.tasks import __apply__
from xnt.tasks import __call__
from xnt.tasks import __which__

def __cvsco__(module, rev=None, dest=None):
    """Run CVS Checkout

    :param module: CVS Module name to checkout
    :param rev: Revision to checkout
    :param dest: Destination directory or name of checked out module
    """
    def __execute__(**kwargs):
        '''Perform CVS Checkout'''
        assert __apply__(__which__("cvs"))
        cmd = ["cvs", "co", "-P"]
        if kwargs['rev']:
            cmd.append("-r")
            cmd.append(kwargs['rev'])
        if kwargs['dest']:
            cmd.append("-d")
            cmd.append(kwargs['dest'])
        cmd.append(kwargs['module'])
        return __apply__(__call__(cmd))
    args = {'module': module, 'rev': rev, 'dest': dest,}
    return ((__execute__, args),)

def __cvsupdate__(path):
    """Run CVS Update

    :param path: Directory path to module to update
    """
    def __execute__(**kwargs):
        '''Perform CVS Update'''
        assert __apply__(__which__("cvs"))
        cwd = os.path.abspath(os.getcwd())
        os.chdir(kwargs['path'])
        cmd = ["cvs", "update"]
        __apply__(__call__(cmd))
        os.chdir(cwd)
    return ((__execute__, {'path': path,}),)
