#!/usr/bin/env python
"""Test xnt.tasks.cp"""

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

from xnt.tasks import __copy__
from types import FunctionType
import unittest

#pylint: disable-msg=C0103
class TaskCopyTests(unittest.TestCase):
    """Test Case for Copy Tasks Method"""
    def setUp(self):
        """Test Setup"""
        pass

    def tearDown(self):
        """Test Teardown"""
        pass

    def test_cp(self):
        """Test default use of cp"""
        result = __copy__(srcdir="test0", dstdir="test1")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], tuple)
        self.assertEqual(2, len(result[0]))
        self.assertIsInstance(result[0][0], FunctionType)
        self.assertIsInstance(result[0][1], dict)
        self.assertTrue('srcdir' in result[0][1])
        self.assertEqual('test0', result[0][1]['srcdir'])
        self.assertTrue('dstdir' in result[0][1])
        self.assertEqual('test1', result[0][1]['dstdir'])

    def test_cp_filelist(self):
        """Test filelist copy"""
        result = __copy__(files=['file1', 'file2', 'file3'], dstdir='test1')
        self.assertIsNotNone(result)
        self.assertTrue('files' in result[0][1])
        self.assertEqual(3, len(result[0][1]['files']))
        self.assertTrue('dstdir' in result[0][1])
        self.assertEqual('test1', result[0][1]['dstdir'])

if __name__ == "__main__":
    unittest.main()
