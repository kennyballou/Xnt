#!/usr/bin/env python
"""Tex Tests Module"""

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
from xnt.build.tex import __pdflatex__
from xnt.build.tex import __clean__
import unittest

class TexTests(unittest.TestCase):
    """Test Case for TeX Document Building"""

    def test_pdflatex_build(self):
        """Test default pdflatex build"""
        result = __pdflatex__('test.tex', directory='tex')
        assert_basic_assumptions(self, result)
        self.assertTrue('texdocument' in result[0][1])
        self.assertEqual('test.tex', result[0][1]['texdocument'])
        self.assertTrue('directory' in result[0][1])
        self.assertTrue('bibtex' in result[0][1])
        self.assertFalse(result[0][1]['bibtex'])
        self.assertTrue('makeglossary' in result[0][1])
        self.assertFalse(result[0][1]['makeglossary'])

    def test_pdflatex_with_bibtex(self):
        """Test pdflatex with bibtex"""
        result = __pdflatex__('test.tex', bibtex=True)
        assert_basic_assumptions(self, result)
        self.assertTrue(result[0][1]['bibtex'])

    def test_pdflatex_with_glossary(self):
        """Test pdflatex with glossary output"""
        result = __pdflatex__("test.tex", makeglossary=True)
        assert_basic_assumptions(self, result)
        self.assertTrue(result[0][1]['makeglossary'])

    def test_tex_clean(self):
        """Test the default clean method removes generated files except pdf"""
        result = __clean__(directory='tex')
        assert_basic_assumptions(self, result)
        self.assertTrue('directory' in result[0][1])
        self.assertEqual('tex', result[0][1]['directory'])
        self.assertTrue('remove_pdf' in result[0][1])
        self.assertFalse(result[0][1]['remove_pdf'])

    def test_tex_clean_include_pdf(self):
        """Test Clean; including PDF"""
        result = __clean__(directory='tex', remove_pdf=True)
        assert_basic_assumptions(self, result)
        self.assertTrue(result[0][1]['remove_pdf'])

if __name__ == '__main__':
    unittest.main()
