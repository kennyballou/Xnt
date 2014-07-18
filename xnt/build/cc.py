#!/usr/bin/env python
"""Common Compilers

Definition of commonly used compilers
"""

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
from xnt.tasks import __apply__
from xnt.tasks import __call__
from xnt.tasks import __which__

LOGGER = logging.getLogger(__name__)

def __gcc__(src, output=None, flags=None):
    """gcc compiler

    :param src: C source file to compile
    :param output: Output filename
    :param flags: List of flags to pass onto the compiler
    """
    def __compile__(**kwargs):
        '''Perform GCC compilation'''
        assert __apply__(__which__("gcc"))
        cmd = ["gcc", kwargs['infile']]
        if kwargs.get('flags', None):
            for flag in kwargs['flags']:
                cmd.append(flag)
        if kwargs.get('outfile', None):
            cmd.append('-o')
            cmd.append(kwargs['outfile'])
        return __apply__(__call__(cmd))
    args = {'infile': src, 'outfile': output, 'flags': flags,}
    return ((__compile__, args),)

def __gpp__(src, output=None, flags=None):
    """g++ compiler, non-named output file

    :param src: C++ source file to compile
    :param output: Output filename
    :param flags: List of flags to pass onto the compiler
    """
    def __compile__(**kwargs):
        '''Perform G++ compilation'''
        assert __apply__(__which__("g++"))
        cmd = ["g++", kwargs['outfile'],]
        if kwargs.get('flags', None):
            for flag in kwargs['flags']:
                cmd.append(flag)
        if kwargs.get('outfile', None):
            cmd.append('-o')
            cmd.append(kwargs['outfile'])
        return __apply__(__call__(cmd))
    args = {'infile': src, 'outfile': output, 'flags': flags,}
    return ((__compile__, args),)

def __javac__(src, flags=None):
    """Javac: compile Java programs

    :param src: Java source file to compile with default `javac`
    :param flags: List of flags to pass onto the compiler
    """
    def __compile__(**kwargs):
        '''Perform javac compilation'''
        assert __apply__(__which__("javac"))
        cmd = ['javac', kwargs['sourcefiles'],]
        if kwargs.get('flags', None):
            for flag in kwargs['flags']:
                cmd.append(flag)
        return __apply__(__call__(cmd))
    return ((__compile__, {'sourcefiles': src, 'flags': flags,}),)

def __nvcc__(src, output=None, flags=None):
    """NVCC: compile CUDA C/C++ programs

    :param src: CUDA source file to compile
    :param output: Output filename
    :param flags: List of flags to pass onto the compiler
    """
    def __compile__(**kwargs):
        '''Perform NVCC compilation'''
        assert __apply__(__call__('nvcc'))
        cmd = ['nvcc', kwargs['infile'],]
        if kwargs.get('flags', None):
            for flag in kwargs['flags']:
                cmd.append(flag)
        if kwargs.get('outfile', None):
            cmd.append('-o')
            cmd.append(kwargs['outfile'])
        return __apply__(__call__(cmd))
    args = {'infile': src, 'outfile': output, 'flags': flags,}
    return ((__compile__, args),)
