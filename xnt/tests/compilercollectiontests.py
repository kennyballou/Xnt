#!/usr/bin/env python
"""Test Common Compiler Collection"""

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
from xnt.build.cc import __gcc__
from xnt.build.cc import __gpp__
from xnt.build.cc import __nvcc__
from xnt.build.cc import __javac__
import unittest

# pylint: disable=R0904
class GccTests(unittest.TestCase):
    """Test GCC"""

    def test_gcc(self):
        """Test Default GCC"""
        result = __gcc__("hello.c")
        assert_basic_assumptions(self, result)
        self.assertTrue("infile" in result[0][1])
        self.assertTrue('flags' in result[0][1])

    def test_gcc_with_output(self):
        """Test GCC with output"""
        result = __gcc__("hello.c", output="hello")
        assert_basic_assumptions(self, result)
        self.assertTrue("infile" in result[0][1])
        self.assertTrue("outfile" in result[0][1])
        self.assertTrue('flags' in result[0][1])

# pylint: disable=R0904
class GppTests(unittest.TestCase):
    """Test G++ (C++ GCC)"""

    def test_gpp(self):
        """Test Default G++"""
        result = __gpp__("hello.cpp")
        assert_basic_assumptions(self, result)
        self.assertTrue("infile" in result[0][1])
        self.assertTrue('flags' in result[0][1])

    def test_gpp_with_output(self):
        """Test G++ with output"""
        result = __gpp__("hello.cpp", output="hello")
        assert_basic_assumptions(self, result)
        self.assertTrue("infile" in result[0][1])
        self.assertTrue("outfile" in result[0][1])
        self.assertTrue('flags' in result[0][1])

# pylint: disable=R0904
class NvccTests(unittest.TestCase):
    """Test NVCC"""

    def test_nvcc(self):
        """Test Default NVCC"""
        result = __nvcc__("hello.cu")
        assert_basic_assumptions(self, result)
        self.assertTrue("infile" in result[0][1])
        self.assertTrue('flags' in result[0][1])

    def test_nvcc_with_output(self):
        """Test Named Output NVCC"""
        result = __nvcc__("hello.cu", output="hello")
        assert_basic_assumptions(self, result)
        self.assertTrue("infile" in result[0][1])
        self.assertTrue("outfile" in result[0][1])
        self.assertTrue('flags' in result[0][1])

# pylint: disable=R0904
class JavacTests(unittest.TestCase):
    """Test Javac"""

    def test_javac(self):
        """Test Default Javac"""
        result = __javac__("HelloWorld.java")
        assert_basic_assumptions(self, result)
        self.assertTrue("sourcefiles" in result[0][1])
        self.assertTrue('flags' in result[0][1])

if __name__ == "__main__":
    unittest.main()
