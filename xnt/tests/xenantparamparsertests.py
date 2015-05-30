#!/usr/bin/env python
'''Xenant Arg Parser Tests'''

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

from xnt.xenant import _process_params_
import unittest

# pylint: disable=R0904
class XenantParamParserTests(unittest.TestCase):
    '''xenant param proessing tests'''

    #pylint: disable=C0103
    def test_process_return_empty_when_none(self):
        '''Test process_params returns empty map when nil'''
        result = _process_params_(None)
        self.assertIsNotNone(result)
        self.assertEquals(result, {})

    #pylint: disable=C0103
    def test_process_return_empty_when_zero_elements(self):
        '''Test process_params returns empty map when zero params given'''
        result = _process_params_([])
        self.assertIsNotNone(result)
        self.assertEquals(result, {})

    #pylint: disable=C0103
    def test_process_returns_dictionary_when_params(self):
        '''Test process_params returns dictionary when given one param'''
        params = ['key=value']
        result = _process_params_(params)
        self.assertIsNotNone(result)
        self.assertIn('key', result)
        self.assertEquals('value', result['key'])

    #pylint: disable=C0103
    def test_process_returns_dictionary_when_many(self):
        '''Test process_params returns dictionary when given many params'''
        params = ['key1=value1',
                  'key2=value2',
                  'key3=value3',
                  'key4=value4',]
        result = _process_params_(params)
        self.assertIsNotNone(result)
        for i in range(len(params)):
            key = 'key%d' % (i + 1)
            value = 'value%d' % (i + 1)
            self.assertIn(key, result)
            self.assertEquals(value, result[key])
