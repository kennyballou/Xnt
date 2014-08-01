#!/usr/bin/env python
"""Wrapping methods around build tools"""

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
from xnt.tasks import __apply__
from xnt.tasks import __call__
from xnt.tasks import __which__

def __ant__(target, path=None, flags=None, pkeys=None, pvalues=None):
    """Wrapper around Apache Ant

    Invoke Apache Ant in either the current working directory or the specified
    directory using the specified target, passing a list of *flags* to the
    invocation. Where *flags* is a list of valid flags for *ant*.

    `pkeys` and `pvalues` are zipped to form a key/value pair passed to Ant as
    property values

    :param target: Ant Target to execute
    :param path: Path of the Ant build file if different than current directory
    :param flags: List of flags to pass to Ant
    :param pkeys: List of keys to combine with pvalues to pass to Ant
    :param pvalues: List of values to combine with pkeys to pass to Ant
    """
    def __execute__(**kwargs):
        '''Perform execution of ant'''
        assert __apply__(__which__("ant"))
        cmd = ['ant',]
        if 'flags' in kwargs:
            for flag in kwargs['flags']:
                cmd.append(flag)
        if 'pkeys' in kwargs and 'pvalues' in kwargs:
            for param in zip(kwargs['pkeys'], kwargs['pvalues']):
                cmd.append('-D%s=%s' % param)
        cmd.append(target)
        # TODO: this will need to wait for an upstream refactor
        return __run_in(path, lambda: __apply__(__call__(cmd)))
    args = {'target': target,
            'flags': flags,
            'pkeys': pkeys,
            'pvalues': pvalues,
            'path': path,}
    return ((__execute__, args),)

def __make__(target, path=None, flags=None, pkeys=None, pvalues=None):
    """Wrapper around GNU Make

    Invoke Gnu Make (*make*) in either the current working directory or the
    specified directory using the specified target, passing a list of *flags*
    to the invocation. Where *flags* is a list of valid flags for *make*.

    `pkeys` and `pvalues` are zipped together to form a key/value pair that are
    passed to Make as property values.

    :param target: Make Target to execute
    :param path: Path of the make file if different than current directory
    :param flags: List of flags to pass to make
    :param pkeys: List of keys, zipped with pvalues, to pass to Make
    :param pvalues: List of values, zipped with pkeys, to pass to Make
    """
    def __execute__(**kwargs):
        '''Perform invocation of make'''
        assert __apply__(__which__("make"))
        cmd = ['make',]
        if 'flags' in kwargs:
            for flag in kwargs['flags']:
                cmd.append(flag)
        if 'pkeys' in kwargs and 'pvalues' in kwargs:
            for param in zip(kwargs['pkeys'], kwargs['pvalues']):
                cmd.append('%s=%s' % param)
        cmd.append(target)
        # TODO: this will need to wait for an upstream refactor
        return __run_in(path, lambda: __apply__(__call__(cmd)))
    args = {'target': target,
            'flags': flags,
            'pkeys': pkeys,
            'pvalues': pvalues,
            'path': path,}
    return ((__execute__, args),)

def __nant__(target, path=None, flags=None, pkeys=None, pvalues=None):
    """Wrapper around .NET Ant

    Invoke NAnt in either the current working directory or the specified
    directory using the specified target, passing a list of *flags* to the
    invocation. Where *flags* is a list of valid flags for *nant*.

    `pkeys` and `pvalues` are zipped together to form a key/ value pair to pass
    to NAnt as property values.

    :param target: NAnt Target to execute
    :param path: Path of NAnt build file, if different than current directory
    :param flags: List of flags to pass to NAnt
    :param pkeys: List of keys, zipped with pvalues, to pass to NAnt
    :param pvalues: List of values, zipped with pkeys, to pass to NAnt
    """
    def __execute__(**kwargs):
        '''Perform execution of ant'''
        assert __apply__(__which__("nant"))
        cmd = ['nant',]
        if 'flags' in kwargs:
            for flag in kwargs['flags']:
                cmd.append(flag)
        if 'pkeys' in kwargs and 'pvalues' in kwargs:
            for param in zip(kwargs['pkeys'], kwargs['pvalues']):
                cmd.append('-D%s=%s' % param)
        cmd.append(target)
        # TODO: this will need to wait for an upstream refactor
        return __run_in(path, lambda: __apply__(__call__(cmd)))
    args = {'target': target,
            'flags': flags,
            'pkeys': pkeys,
            'pvalues': pvalues,
            'path': path,}
    return ((__execute__, args),)

def __run_in(path, function):
    """Execute function while in a different running directory"""
    cwd = os.path.abspath(os.getcwd())
    if path and os.path.exists(path):
        os.chdir(os.path.abspath(path))
    result = function()
    if cwd:
        os.chdir(cwd)
    return result
