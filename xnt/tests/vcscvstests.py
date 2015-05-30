#!/usr/bin/env python
"""Test `xnt.vcs.cvs`"""

#   Xnt -- A Wrapper Build Tool
#   Copyright (C) 2014  Kenny Ballou

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed, the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from xnt.tests import assert_basic_assumptions
from xnt.tasks.vcs.cvs import __cvsco__
from xnt.tasks.vcs.cvs import __cvsupdate__
import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 6:
    import unittest2 as unittest
else:
    import unittest

# pylint: disable=R0904
class VcsCvsTests(unittest.TestCase):
    '''VCS CVS Tests'''

    def test_cvsco(self):
        '''Test CVS checkout'''
        result = __cvsco__('mytestmodule')
        assert_basic_assumptions(self, result)
        self.assertIn('module', result[0][1])
        self.assertEqual('mytestmodule', result[0][1]['module'])
        self.assertIn('rev', result[0][1])
        self.assertIsNone(result[0][1]['rev'])
        self.assertIn('dest', result[0][1])
        self.assertIsNone(result[0][1]['dest'])

    def test_cvsupdate(self):
        '''Test CVS Update'''
        result = __cvsupdate__('./')
        assert_basic_assumptions(self, result)
        self.assertIn('path', result[0][1])
        self.assertEqual('./', result[0][1]['path'])

if __name__ == "__main__":
    unittest.main()
