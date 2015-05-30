#!/usr/bin/env python
"""Test `xnt.tasks.mkdir`"""

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
from xnt.tasks.core_tasks import __mkdir__
import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 6:
    import unittest2 as unittest
else:
    import unittest

# pylint: disable=R0904
class TaskMkdirTests(unittest.TestCase):
    """Test Cases for Mkdir"""
    def test_mkdir(self):
        """Test mkdir method"""
        result = __mkdir__("my/new/directory")
        assert_basic_assumptions(self, result)
        self.assertIn('directory', result[0][1])
        self.assertEqual('my/new/directory', result[0][1]['directory'])
        self.assertIn('mode', result[0][1])
        self.assertEqual(0o755, result[0][1]['mode'])

if __name__ == "__main__":
    unittest.main()
