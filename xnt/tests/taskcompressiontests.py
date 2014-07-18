#!/usr/bin/env python
"""Test `xnt.tasks.zip`"""

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

from xnt.tasks import __zip__
from types import FunctionType
import unittest

#pylint: disable-msg=C0103
class TaskCompressionTests(unittest.TestCase):
    """Test Cases for Compression"""
    def setUp(self):
        """Test Case Setup"""
        pass

    def tearDown(self):
        """Test Case Teardown"""
        pass

    def test_zip(self):
        """Test zip method"""
        result = __zip__(directory="testfolder", zipfilename="myzip.zip")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], tuple)
        self.assertEqual(2, len(result[0]))
        self.assertIsInstance(result[0][0], FunctionType)
        self.assertIsInstance(result[0][1], dict)
        self.assertTrue("directory" in result[0][1])
        self.assertEqual("testfolder", result[0][1]['directory'])
        self.assertTrue("zipfile" in result[0][1])
        self.assertEqual("myzip.zip", result[0][1]['zipfile'])

if __name__ == "__main__":
    unittest.main()
