#!/usr/bin/env python
"""Test `xnt.vcs.hg`"""

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
from xnt.vcs.hg import __hgclone__
from xnt.vcs.hg import __hgfetch__
import unittest

class VcsHgTests(unittest.TestCase):
    '''VCS Mercurial Tests'''

    def test_hgclone(self):
        '''Test hg clone'''
        url = 'https://vim.googlecode.com/hg'
        result = __hgclone__(url, dest='vim')
        assert_basic_assumptions(self, result)
        self.assertTrue('url' in result[0][1])
        self.assertEqual(url, result[0][1]['url'])
        self.assertTrue('dest' in result[0][1])
        self.assertEqual('vim', result[0][1]['dest'])
        self.assertTrue('rev' in result[0][1])
        self.assertIsNone(result[0][1]['rev'])
        self.assertTrue('branch' in result[0][1])
        self.assertIsNone(result[0][1]['branch'])

    def test_hgfetch(self):
        '''Test hg fetch'''
        result = __hgfetch__('./', source='upstream')
        assert_basic_assumptions(self, result)
        self.assertTrue('path' in result[0][1])
        self.assertEqual('./', result[0][1]['path'])
        self.assertTrue('source' in result[0][1])
        self.assertTrue('upstream', result[0][1]['source'])

if __name__ == "__main__":
    unittest.main()
