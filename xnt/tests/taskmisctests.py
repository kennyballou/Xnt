#!/usr/bin/env python
"""Misc Tasks Tests"""

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
from xnt.tasks import __echo__
from xnt.tasks import __call__
from xnt.tasks import __setup__
from xnt.tasks import __xntcall__
from xnt.tasks import __xnt_list_targets__
from xnt.tasks import __which__
from xnt.tasks import __in_path__
from xnt.tasks import __log__
from xnt.tasks import __expandpath__
import unittest

# pylint: disable=R0904
class TaskMiscTests(unittest.TestCase):
    """Test Misc Tasks"""

    def test_echo(self):
        """Test Echo Task"""
        result = __echo__(msg="foobar", tofile="mytestfile")
        assert_basic_assumptions(self, result)
        self.assertTrue('msg' in result[0][1])
        self.assertEqual('foobar', result[0][1]['msg'])
        self.assertTrue('tofile' in result[0][1])
        self.assertEqual('mytestfile', result[0][1]['tofile'])

    def test_log(self):
        """Test log function"""
        result = __log__(msg="testing the logging", lvl=40)
        assert_basic_assumptions(self, result)
        self.assertTrue('msg' in result[0][1])
        self.assertEqual('testing the logging', result[0][1]['msg'])
        self.assertTrue('lvl' in result[0][1])
        self.assertEqual(40, result[0][1]['lvl'])

    def test_call(self):
        """Test Call, testing redirection"""
        result = __call__(['echo', 'blah'])
        assert_basic_assumptions(self, result)
        self.assertTrue('command' in result[0][1])
        self.assertEqual(2, len(result[0][1]['command']))
        self.assertEqual('echo', result[0][1]['command'][0])
        self.assertEqual('blah', result[0][1]['command'][1])
        self.assertTrue('stdout' in result[0][1])
        self.assertIsNone(result[0][1]['stdout'])
        self.assertTrue('stderr' in result[0][1])
        self.assertIsNone(result[0][1]['stderr'])

    def test_setup_with_single_command(self):
        '''Test setup function with a single command'''
        result = __setup__(command='test')
        assert_basic_assumptions(self, result)
        self.assertTrue('commands' in result[0][1])
        self.assertEqual(1, len(result[0][1]['commands']))

    def test_setup_with_commands(self):
        '''Test setup function commands'''
        result = __setup__(commands=['build', 'test'])
        assert_basic_assumptions(self, result)
        self.assertTrue('commands' in result[0][1])
        self.assertEqual(2, len(result[0][1]['commands']))

    def test_setup_with_directory(self):
        '''Test setup function with directory'''
        result = __setup__(command='test', directory='test/')
        assert_basic_assumptions(self, result)
        self.assertTrue('directory' in result[0][1])
        self.assertEqual('test/', result[0][1]['directory'])

    def test_xntcall(self):
        """Test xntcall"""
        result = __xntcall__(buildfile='test/build.py')
        assert_basic_assumptions(self, result)
        self.assertTrue('buildfile' in result[0][1])
        self.assertEqual('test/build.py', result[0][1]['buildfile'])
        self.assertTrue('targets' in result[0][1])
        self.assertTrue('props' in result[0][1])

    def test_xnt_list_targets(self):
        '''Test xnt list targets'''
        result = __xnt_list_targets__('./build.py')
        assert_basic_assumptions(self, result)
        self.assertTrue('buildfile' in result[0][1])
        self.assertEqual('./build.py', result[0][1]['buildfile'])

    def test_expandpath(self):
        '''Test expandpath'''
        result = __expandpath__('./**.pyc')
        assert_basic_assumptions(self, result)
        self.assertTrue('path_pattern', result[0][1])
        self.assertEqual('./**.pyc', result[0][1]['path_pattern'])

    def test_which(self):
        """Test which"""
        result = __which__('python')
        assert_basic_assumptions(self, result)
        self.assertTrue('program' in result[0][1])
        self.assertEqual('python', result[0][1]['program'])

    def test_in_path(self):
        """Test in_path task"""
        result = __in_path__('python')
        assert_basic_assumptions(self, result)
        self.assertTrue('program' in result[0][1])
        self.assertEqual('python', result[0][1]['program'])

if __name__ == "__main__":
    unittest.main()
