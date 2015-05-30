#!/usr/bin/env python
"""Test xnt.tasks.cp"""

#   Xnt -- A Wrapper Build Tool
#   Copyright (C) 2013  Kenny Ballou

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
from xnt.tasks.core_tasks import __copy__
import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 6:
    import unittest2 as unittest
else:
    import unittest

# pylint: disable=R0904
class TaskCopyTests(unittest.TestCase):
    """Test Case for Copy Tasks Method"""

    def test_cp(self):
        """Test default use of cp"""
        result = __copy__(src="test0", dstdir="test1")
        assert_basic_assumptions(self, result)
        self.assertIn('src', result[0][1])
        self.assertEqual('test0', result[0][1]['src'])
        self.assertIn('dstdir', result[0][1])
        self.assertEqual('test1', result[0][1]['dstdir'])

    def test_cp_filelist(self):
        """Test filelist copy"""
        result = __copy__(files=['file1', 'file2', 'file3'], dstdir='test1')
        assert_basic_assumptions(self, result)
        self.assertIn('files', result[0][1])
        self.assertEqual(3, len(result[0][1]['files']))
        self.assertIn('dstdir', result[0][1])
        self.assertEqual('test1', result[0][1]['dstdir'])

if __name__ == "__main__":
    unittest.main()
