#!/usr/bin/env python
"""Test `xnt.tasks.rm`"""

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
from xnt.tasks.core_tasks import __remove__
import unittest

# pylint: disable=R0904
class TaskRemoveTests(unittest.TestCase):
    """Test Case for Remove"""
    def test_remove(self):
        """Test removing files and folders"""
        result = __remove__('test0', 'test1', '*swp')
        assert_basic_assumptions(self, result)
        self.assertIn('fileset', result[0][1])
        self.assertEqual(3, len(result[0][1]['fileset']))

if __name__ == "__main__":
    unittest.main()
