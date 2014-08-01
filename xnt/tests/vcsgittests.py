#!/usr/bin/env python
"""Test `xnt.vcs.git`"""

#   Xnt -- A Wrapper Build Tool
#   Copyright (C) 2014  Kenny Ballou

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

from xnt.tests import assert_basic_assumptions
from xnt.tasks.vcs.git import __gitclone__
from xnt.tasks.vcs.git import __gitpull__
import unittest

# pylint: disable=R0904
class VcsGitTests(unittest.TestCase):
    '''Test VCS GIT'''

    def test_gitclone(self):
        '''Test GIT Clone'''
        url = 'git://github.com/devnulltao/Xnt.git'
        result = __gitclone__(url)
        assert_basic_assumptions(self, result)
        self.assertTrue('url' in result[0][1])
        self.assertTrue('dest' in result[0][1])
        self.assertTrue('branch' in result[0][1])
        self.assertEqual(url, result[0][1]['url'])
        self.assertIsNone(result[0][1]['dest'])
        self.assertIsNone(result[0][1]['branch'])

    def test_gitpull(self):
        '''Test GIT Pull'''
        result = __gitpull__('./', remote='upstream', branch='develop')
        assert_basic_assumptions(self, result)
        self.assertTrue('path' in result[0][1])
        self.assertEqual('./', result[0][1]['path'])
        self.assertTrue('remote' in result[0][1])
        self.assertEqual('upstream', result[0][1]['remote'])
        self.assertTrue('branch' in result[0][1])
        self.assertEqual('develop', result[0][1]['branch'])

if __name__ == "__main__":
    unittest.main()
