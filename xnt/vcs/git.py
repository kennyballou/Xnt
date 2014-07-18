#!/usr/bin/env python
"""Git Version Control Module"""

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

def __gitclone__(url, dest=None, branch=None):
    """Clone a repository

    :param url: URI of the repository to clone
    :param dest: Destination directory or name of the cloned repository
    :param branch: Branch to clone
    """
    def __execute__(**kwargs):
        '''Perform git clone'''
        assert __apply__(__which__("git"))
        command = ["git", "clone"]
        command = xnt.vcs.clone_options(
            command, kwargs['url'], kwargs['branch'], kwargs['dest'])
        return __apply__(__call__(command))
    args = {'url': url, 'dest': dest, 'branch': branch,}
    return ((__execute__, args),)

def __gitpull__(path, remote=None, branch=None):
    """Pull/Update a cloned repository

    :param path: Directory of the repository for which to pull and update
    :param remote: Repository's upstream source
    :param branch: Repository's upstream branch to pull from
    """
    def __execute__(**kwargs):
        '''Perform git pull'''
        assert __apply__(__which__("git"))
        cwd = os.getcwd()
        os.chdir(kwargs['path'])
        command = ["git", "pull", kwargs['remote'], kwargs['branch']]
        __apply__(__call__(command))
        os.chdir(cwd)
    args = {
        'path': path,
        'remote': remote if remote else 'origin',
        'branch': branch if branch else 'master',
    }
    return ((__execute__, args),)
