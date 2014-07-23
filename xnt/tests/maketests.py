#!/usr/bin/env python
"""Make (make/ant/nant) Tests Module"""

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
from xnt.build.make import __make__
from xnt.build.make import __ant__
from xnt.build.make import __nant__
import unittest

class AntTests(unittest.TestCase):
    """Test Case for Ant Build"""

    def test_default_build(self):
        """Test the default target of ant"""
        result = __ant__(target="test")
        assert_basic_assumptions(self, result)
        self.assertTrue('target' in result[0][1])
        self.assertEqual('test', result[0][1]['target'])

    def test_ant_when_given_path(self):
        """Test ant when passing given a path"""
        result = __ant__(target="test", path="some/other/path/build.xml")
        assert_basic_assumptions(self, result)
        self.assertTrue('path' in result[0][1])
        self.assertEqual('some/other/path/build.xml', result[0][1]['path'])

    def test_ant_when_given_flags(self):
        """Test passing flags to ant"""
        result = __ant__(target='test', flags=['-verbose'])
        assert_basic_assumptions(self, result)
        self.assertTrue('flags' in result[0][1])
        self.assertEqual(1, len(result[0][1]['flags']))
        self.assertEqual('-verbose', result[0][1]['flags'][0])

    def test_ant_when_given_vars(self):
        """Test passing variables to ant"""
        result = __ant__(target="test",
                         pkeys=["test_var"],
                         pvalues=["testing"])
        assert_basic_assumptions(self, result)
        self.assertTrue('pkeys' in result[0][1])
        self.assertTrue('pvalues' in result[0][1])
        self.assertEqual(1, len(result[0][1]['pkeys']))
        self.assertEqual(1, len(result[0][1]['pvalues']))
        self.assertEqual('test_var', result[0][1]['pkeys'][0])
        self.assertEqual('testing', result[0][1]['pvalues'][0])

class MakeTests(unittest.TestCase):
    """GNU Make Tests"""

    def test_default_make(self):
        """Test Default make"""
        result = __make__(target="build")
        assert_basic_assumptions(self, result)
        self.assertTrue('target' in result[0][1])
        self.assertEqual('build', result[0][1]['target'])

    def test_make_with_path(self):
        '''Test make given a path'''
        result = __make__(target="build", path="some/other/path/Makefile")
        assert_basic_assumptions(self, result)
        self.assertTrue('path' in result[0][1])
        self.assertEqual('some/other/path/Makefile', result[0][1]['path'])

    def test_passing_vars(self):
        """Test Parameter Passing with Make"""
        result = __make__(target='build',
                          pkeys=["test_var"],
                          pvalues=["testing"])
        assert_basic_assumptions(self, result)
        self.assertTrue('pkeys' in result[0][1])
        self.assertTrue('pvalues' in result[0][1])
        self.assertEqual(1, len(result[0][1]['pkeys']))
        self.assertEqual(1, len(result[0][1]['pvalues']))
        self.assertEqual('test_var', result[0][1]['pkeys'][0])
        self.assertEqual('testing', result[0][1]['pvalues'][0])

    def test_passing_flags(self):
        """Test Flag Passing with Make"""
        result = __make__(target='build', flags=['-B'])
        assert_basic_assumptions(self, result)
        self.assertTrue('flags' in result[0][1])
        self.assertEqual(1, len(result[0][1]['flags']))
        self.assertEqual('-B', result[0][1]['flags'][0])

class NAntTests(unittest.TestCase):
    """.NET Ant Tests"""

    def test_nant_with_target(self):
        """Test Deault nant"""
        result = __nant__(target='test')
        assert_basic_assumptions(self, result)
        self.assertTrue('target' in result[0][1])
        self.assertEqual('test', result[0][1]['target'])

    def test_nant_with_path(self):
        '''Test NAnt with path'''
        result = __nant__(target='test', path='some/other/path/build.xml')
        assert_basic_assumptions(self, result)
        self.assertTrue('path' in result[0][1])
        self.assertEqual('some/other/path/build.xml', result[0][1]['path'])

    def test_nant_with_parameters(self):
        '''Test NAnt with parameters'''
        result = __nant__(target="test",
                          pkeys=["test_var"],
                          pvalues=["testing"])
        assert_basic_assumptions(self, result)
        self.assertTrue('pkeys' in result[0][1])
        self.assertTrue('pvalues' in result[0][1])
        self.assertEqual(1, len(result[0][1]['pkeys']))
        self.assertEqual(1, len(result[0][1]['pvalues']))
        self.assertEqual('test_var', result[0][1]['pkeys'][0])

    def test_nant_with_flags(self):
        '''Test NAnt with flags'''
        result = __nant__(target="test", flags=["-v"])
        assert_basic_assumptions(self, result)
        self.assertTrue('flags' in result[0][1])
        self.assertEqual(1, len(result[0][1]['flags']))
        self.assertEqual('-v', result[0][1]['flags'][0])

if __name__ == '__main__':
    unittest.main()
