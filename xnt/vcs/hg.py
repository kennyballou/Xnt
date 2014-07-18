#!/usr/bin/env python
"""Mercurial Version Control Module/Wrapper"""

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
import xnt.tasks
import xnt.vcs
from xnt.tasks import __apply__, __call__, __which__

def __hgclone__(url, dest=None, rev=None, branch=None):
    """Clone a Mercurial Repository

    :param url: URI of repository to clone
    :param dest: Directory or name of cloned repository
    :param rev: Revision to clone
    :param branch: Branch to clone
    """
    def __execute__(**kwargs):
        '''Perform hg clone'''
        assert __apply__(__which__("hg"))
        command = ["hg", "clone"]
        if kwargs['rev']:
            command.append("--rev")
            command.append(kwargs['rev'])
        command = xnt.vcs.clone_options(
            command, kwargs['url'], kwargs['branch'], kwargs['dest'])
        return __apply__(__call__(command))
    args = {'url': url, 'dest': dest, 'rev': rev, 'branch': branch,}
    return ((__execute__, args),)

def __hgfetch__(path, source=None):
    """Pull and Update an already cloned Mercurial Repository

    :param path: Directory to the repository for which to pull changes
    :param source: Repository's upstream source
    """
    def __execute__(**kwargs):
        '''Perform hg pull'''
        assert __apply__(__which__("hg"))
        command = ["hg", "pull", "-u", kwargs['source']]
        cwd = os.getcwd()
        os.chdir(kwargs['path'])
        __apply__(__call__(command))
        os.chdir(cwd)
    args = {'path': path, 'source': source if source else 'default',}
    return ((__execute__, args),)
