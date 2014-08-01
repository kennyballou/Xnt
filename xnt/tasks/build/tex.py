#!/usr/bin/env python
"""LaTeX Build Module"""

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

import os
import logging
from xnt.verbose import VERBOSE

LOGGER = logging.getLogger(__name__)

def __pdflatex__(document,
                 directory=None,
                 bibtex=False,
                 makeglossary=False):
    """Generate PDF LaTeX Document

    Use `pdflatex` to build a LaTeX PDF document. Can optionally execute steps
    to properly build `bibtex` references and/ or glossaries.

    :param document: Name of tex file (with or without `.tex` extension)
    :param path: Directory of tex file, if different than current directory
    :param bibtex: Flag to or not to add bibtex. Default: False
    :param makeglossary: Flag to or not to add a glossary. Default: False
    """
    def __execute__(**kwargs):
        '''Perform pdflatex build'''
        devnull = None if VERBOSE else open(os.devnull, 'w')
        documentbase = os.path.splitext(document)[0]
        def pdf(draftmode=False):
            """Generate PDF"""
            from xnt.tasks.core_tasks import __call__, __apply__
            cmd = ["pdflatex", document, "-halt-on-error",]
            if draftmode:
                cmd.append('-draftmode')
            return __apply__(__call__(
                cmd,
                stdout=devnull,
                path=kwargs['directory']))

        def run_bibtex():
            """Generate BibTex References"""
            from xnt.tasks.core_tasks import __call__, __apply__
            return __apply__(__call__(
                ["bibtex", documentbase + ".aux"],
                stdout=devnull,
                path=kwargs['directory']))

        def makeglossaries():
            """Generate Glossary"""
            from xnt.tasks.core_tasks import __call__, __apply__
            return __apply__(__call__(
                ["makeglossaries", documentbase],
                stdout=devnull,
                path=kwargs['directory']))

        error_codes = []
        error_codes.append(pdf(draftmode=True))
        if kwargs['makeglossary']:
            error_codes.append(makeglossaries())
        if kwargs['bibtex']:
            error_codes.append(run_bibtex())
            error_codes.append(pdf(draftmode=True))
        error_codes.append(pdf(draftmode=False))
        if devnull:
            devnull.close()
        return sum(error_codes)
    args = {'texdocument': document,
            'directory': directory if directory else os.getcwd(),
            'bibtex': bibtex,
            'makeglossary': makeglossary,}
    return ((__execute__, args),)


def __clean__(directory=None, remove_pdf=False):
    """Clean up generated files of PDF compilation

    :param path: Directory of output files, if different than current directory
    :param remove_pdf: Flag to remove the PDF. Default: False
    """
    def __execute__(**kwargs):
        '''Perform clean operation'''
        from xnt.tasks.core_tasks import __run_in__
        def closure():
            '''closure around removal'''
            from xnt.tasks.core_tasks import __apply__, __remove__
            __apply__(__remove__("*.out",
                                 "*.log",
                                 "*.aux",
                                 "*.toc",
                                 "*.tol",
                                 "*.tof",
                                 "*.tot",
                                 "*.bbl",
                                 "*.blg",
                                 "*.nav",
                                 "*.snm",
                                 "*.mtc",
                                 "*.mtc0",
                                 "*.glo",
                                 "*.ist",
                                 "*.glg",
                                 "*.gls"))
            if kwargs['remove_pdf']:
                __apply__(__remove__("*.pdf"))
        return __run_in__(closure, kwargs['directory'])
    args = {'directory': directory if directory else os.getcwd(),
            'remove_pdf': remove_pdf,}
    return ((__execute__, args),)
