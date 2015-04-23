#!/usr/bin/env python
"""Test `xnt.tasks.mv`"""

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
from xnt.tasks.core_tasks import __move__
import unittest

# pylint: disable=R0904
class TaskMoveTests(unittest.TestCase):
    """Test cases for move"""
    def test_move(self):
        """Test Moving files and folders"""
        result = __move__('test0', 'test1')
        assert_basic_assumptions(self, result)
        self.assertIn('src', result[0][1])
        self.assertIn('dst', result[0][1])
        self.assertEqual('test0', result[0][1]['src'])
        self.assertEqual('test1', result[0][1]['dst'])

if __name__ == "__main__":
    unittest.main()
