#!/usr/bin/env python
"""Tests Module"""

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

def assert_basic_assumptions(testcase, result):
    '''Test function assert basic structure of task code'''
    from types import FunctionType
    testcase.assertIsNotNone(result)
    testcase.assertIsInstance(result, tuple)
    testcase.assertIsInstance(result[0], tuple)
    testcase.assertEqual(len(result[0]), 2)
    testcase.assertIsInstance(result[0][0], FunctionType)
    testcase.assertIsInstance(result[0][1], dict)
