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

from xnt.tests import assert_basic_assumptions
from xnt.tasks import __zip__
import unittest

# pylint: disable=R0904
class TaskCompressionTests(unittest.TestCase):
    """Test Cases for Compression"""

    def test_zip(self):
        """Test zip method"""
        result = __zip__(directory="testfolder", zipfilename="myzip.zip")
        assert_basic_assumptions(self, result)
        self.assertTrue("directory" in result[0][1])
        self.assertEqual("testfolder", result[0][1]['directory'])
        self.assertTrue("zipfile" in result[0][1])
        self.assertEqual("myzip.zip", result[0][1]['zipfile'])

if __name__ == "__main__":
    unittest.main()
