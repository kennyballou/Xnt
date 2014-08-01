#!/usr/bin/env python
"""Common Tasks Module

Defines a set of operations that are common enough but also are tedious to
define
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
import sys
import subprocess
import shutil
import zipfile
import contextlib
import glob
import logging
from xnt.status_codes import ERROR, SUCCESS, UNKNOWN_ERROR

LOGGER = logging.getLogger(__name__)

#File associated tasks
def __expandpath__(path_pattern):
    """Return a glob expansion generator of *path_pattern*

    :param path_pattern: pattern to expand
    :rtype: generator of strings
    :return: List of paths and/ or files
    """
    def __execute__(**kwargs):
        return glob.iglob(kwargs['path_pattern'])
    return ((__execute__, {'path_pattern': path_pattern}),)

def __copy__(srcdir=None, dstdir=None, files=None):
    """Copy `srcdir` to `dstdir` or copy `files` to `dstdir`

    Copy a file or folder to a different file/folder
    If no `srcdir` file is specified, will attempt to copy `files` to `dstdir`

    *Notice*, elements of `files` will not be expanded before copying.

    :param srcdir: source directory or file
    :param dstdir: destination file or folder (in the case of `files`)
    :param files: list of files (strings) to copy to `src`
    """
    def __execute__(**kwargs):
        """Perform copy"""
        assert 'dstdir' in kwargs
        if 'srcdir' in kwargs:
            shutil.copytree(kwargs['srcdir'], kwargs['dstdir'])
        elif 'files' in kwargs:
            for srcfile in kwargs['files']:
                shutil.copy(srcfile, kwargs['dstdir'])
    return (
        (__execute__, {'srcdir': srcdir, 'dstdir': dstdir, 'files': files,}),
    )

def __move__(src, dst):
    """Move `src` to `dst`

    Move (copy and remove) the source file or directory (*src*) to the
    destination file or directory (*dst*)

    :param src: Source file or folder to move
    :param dst: Destination file or folder
    """
    def __execute__(**kwargs):
        '''Perform move'''
        LOGGER.info("Moving %s to %s", kwargs['src'], kwargs['dst'])
        shutil.move(kwargs['src'], kwargs['dst'])
    args = {'src': src, 'dst': dst,}
    return ((__execute__, args),)

def __mkdir__(directory, mode=0o755):
    """Make a directory with mode

    Create a directory specified by *dir* with default mode (where supported)
    or with the specified *mode*

    *Notice*, if the directory already exists, *mkdir* will log a warning and
    return

    :param directory: New directory to create
    :param mode: Mode to create the directory (where supported). Default: `777`
    """
    def __execute__(**kwargs):
        '''Perform directory creation'''
        if os.path.exists(directory):
            LOGGER.warning(
                "Given directory (%s) already exists",
                kwargs['directory'])
            return
        LOGGER.info(
            "Making directory %s with mode %o",
            kwargs['directory'],
            kwargs['mode'])
        try:
            os.mkdir(kwargs['directory'], kwargs['mode'])
        except IOError as io_error:
            LOGGER.error(io_error)
        except:
            raise
    return ((__execute__, {'directory': directory, 'mode': mode,}),)

def __remove__(*fileset):
    """Remove a set of files

    Attempt to remove all the directories given by the fileset. Before *rm*
    tries to delete each element of *fileset*, it attempts to expand it first
    using glob expansion (:func:`xnt.tasks.expandpath`), thus allowing the
    passing of glob elements

    :param fileset: List of files to remove
    """
    def __execute__(**kwargs):
        '''Perform file/ folder removal'''
        try:
            for glob_set in kwargs['fileset']:
                for file_to_delete in __apply__(__expandpath__(glob_set)):
                    if not os.path.exists(file_to_delete):
                        continue
                    LOGGER.info("Removing %s", file_to_delete)
                    if os.path.isdir(file_to_delete):
                        shutil.rmtree(file_to_delete)
                    else:
                        os.remove(file_to_delete)
        except OSError as os_error:
            LOGGER.error(os_error)
        except:
            raise
    args = {'fileset': fileset,}
    return ((__execute__, args),)

def __zip__(directory, zipfilename):
    """Compress (Zip) folder

    Zip the specified *directory* into the zip file named *zipfilename*

    :param directory: Directory to zip
    :param zipfilename: Name of resulting compression
    """
    def __execute__(**kwargs):
        '''Perform zip'''
        assert os.path.isdir(kwargs['directory']) and kwargs['zipfile']
        LOGGER.info("Zipping %s as %s", kwargs['directory'], kwargs['zipfile'])
        with contextlib.closing(zipfile.ZipFile(
            kwargs['zipfile'],
            "w",
            zipfile.ZIP_DEFLATED)) as zip_file:
            for paths in os.walk(kwargs['directory']):
                for file_name in paths[2]:
                    absfn = os.path.join(paths[0], file_name)
                    zip_file_name = absfn[len(directory) + len(os.sep):]
                    zip_file.write(absfn, zip_file_name)
    return ((__execute__, {'directory': directory, 'zipfile': zipfilename,}),)

#Misc Tasks
def __echo__(msg, tofile):
    """Write a string to file

    Write the given *msg* to a file named *tofile*

    *Notice*, `echo` will overwrite the file if it already exists

    :param msg: Message to write to file
    :param tofile: file to which the message is written
    """
    def __execute__(**kwargs):
        '''Perform echo to file'''
        with open(kwargs['tofile'], "w") as file_to_write:
            file_to_write.write(kwargs['msg'])
    return ((__execute__, {'msg': msg, 'tofile': tofile,}),)

def __log__(msg, lvl=logging.INFO):
    """Log *msg* using tasks global logger

    Emit the message (*msg*) to the *xnt.tasks* logger using either the default
    log level (*INFO*) or any valid specified value of `logging` module

    :param msg: Message to log
    :param lvl: Log Level of message. Default `INFO`
    """
    def __execute__(**kwargs):
        '''Perform logging operation'''
        LOGGER.log(kwargs['lvl'], kwargs['msg'])
    return ((__execute__, {'msg': msg, 'lvl': lvl,}),)

def __load_build__(buildfile="./build.py"):
    """Load build file
    Load the build.py and return the resulting import
    """
    path = os.path.dirname(buildfile)
    build = os.path.basename(buildfile)
    buildmodule = os.path.splitext(build)[0]
    if not path:
        path = os.getcwd()
    else:
        path = os.path.abspath(path)
    sys.path.append(path)
    cwd = os.getcwd()
    os.chdir(path)
    if not os.path.exists(build):
        LOGGER.error("There was no build file")
        sys.exit(1)
    try:
        return __import__(buildmodule, fromlist=[])
    except ImportError:
        LOGGER.error("HOW?!")
        return None
    finally:
        sys.path.remove(path)
        del sys.modules[buildmodule]
        os.chdir(cwd)

def __xntcall__(buildfile, targets=None, props=None):
    """Invoke xnt on another build file in a different directory

    :param: path - to the build file (including build file)
    :param: targets - list of targets to execute
    :param: props - dictionary of properties to pass to the build module
    """
    def __execute__(**kwargs):
        '''Perform xntcall'''
        def invoke_build(build, targets=None, props=None):
            """Invoke Build with `targets` passing `props`"""
            def call_target(target_name, props):
                """Call target on build module"""
                def process_params(params, existing_props=None):
                    """Parse and separate properties"""
                    properties = existing_props if existing_props else {}
                    for param in params:
                        name, value = param.split("=")
                        properties[name] = value
                    return properties
                def __get_properties():
                    """Return the properties dictionary of the build module"""
                    try:
                        return getattr(build, "PROPERTIES")
                    except AttributeError:
                        LOGGER.warning("Build file specifies no properties")
                        return None
                try:
                    if props and len(props) > 0:
                        setattr(build,
                                "PROPERTIES",
                                process_params(props, __get_properties()))
                    target = getattr(build, target_name)
                    error_code = target()
                    return error_code if error_code else SUCCESS
                except AttributeError:
                    LOGGER.error("There was no target: %s", target_name)
                    return ERROR
                except Exception as ex:
                    LOGGER.critical(ex)
                    return UNKNOWN_ERROR
            if not targets:
                targets = ['default',]
            for target in targets:
                error_code = call_target(target, props)
                if error_code:
                    return error_code
            return SUCCESS

        build = __load_build__(kwargs['buildfile'])
        path = os.path.dirname(kwargs['buildfile'])
        cwd = os.getcwd()
        os.chdir(path)
        error_code = invoke_build(
            build,
            targets=kwargs['targets'],
            props=kwargs['props'])
        os.chdir(cwd)
        return error_code
    args = {'buildfile': buildfile, 'targets': targets, 'props': props, }
    return ((__execute__, args),)

def __xnt_list_targets__(buildfile):
    '''List targets (and doctstrings) of the provided build module'''
    def __execute__(**kwargs):
        '''Perform listing'''
        try:
            for attr in dir(kwargs['build']):
                try:
                    func = getattr(kwargs['build'], attr)
                    if func.decorator == "target":
                        print(attr + ":")
                        if func.__doc__:
                            print(func.__doc__)
                        print("")
                except AttributeError:
                    pass
        except AttributeError as ex:
            LOGGER.error(ex)
            return ERROR
        return SUCCESS
    args = {'buildfile': buildfile,}
    return ((__execute__, args),)

def __call__(command, stdout=None, stderr=None):
    """ Execute the given command, redirecting stdout and stderr
    to optionally given files

    :param: command - list of command and arguments
    :param: stdout - file to redirect standard output to, if given
    :param: stderr - file to redirect standard error to, if given
    :return: the error code of the subbed out call, `$?`
    """
    def __execute__(**kwargs):
        '''Perform subprocess call'''
        return subprocess.call(
            args=kwargs['command'],
            stdout=kwargs['stdout'], stderr=kwargs['stderr'])
    args = {'command': command, 'stdout': stdout, 'stderr': stderr,}
    return ((__execute__, args),)

def __setup__(command=None, commands=None, directory=None):
    """Invoke the ``setup.py`` file in the current or specified directory

    :param: command - a single command to run
    :param: commands - list of commands and options to run/ append
    :param: dir - (optional) directory to run from
    :return: the error code of the execution, `$?`
    """
    def __execute__(**kwargs):
        '''Perform python setup.py commands'''
        cmd = [sys.executable, "setup.py",]
        for command in kwargs['commands']:
            cmd.append(command)
        cwd = os.getcwd()
        if kwargs['directory']:
            os.chdir(kwargs['directory'])
        error_code = __apply__(__call__(cmd))
        os.chdir(cwd)
        return error_code
    if not commands:
        commands = []
    if command:
        commands.append(command)
    assert len(commands) > 0
    args = {'commands': commands, 'directory': directory,}
    return ((__execute__, args),)

def __which__(program):
    """Similar to Linux/Unix `which`: return (first) path of executable

    :param program: program name to search for in PATH
    :return: Return the PATH of `program` or None
    """
    def __execute__(**kwargs):
        '''Perform which lookup'''
        def is_exe(fpath):
            """Determine if argument exists and is executable"""
            return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

        fpath = os.path.split(kwargs['program'])
        if fpath[0]:
            if is_exe(kwargs['program']):
                return kwargs['program']
        else:
            for path in os.environ["PATH"].split(os.pathsep):
                path = path.strip('"')
                exe_file = os.path.join(path, kwargs['program'])
                if is_exe(exe_file):
                    return exe_file
        return None

    return ((__execute__, {'program': program,}),)

def __in_path__(program):
    """Return boolean result if program is in PATH environment variable

    :param program: Program name to search for in PATH
    :return: Return the PATH of `program` or None
    """
    def __execute__(**kwargs):
        '''Perform which test'''
        return __apply__(__which__(kwargs['program']))
    return ((__execute__, {'program': program,}),)

# pylint: disable=W0142
def __apply__(func_tuple):
    '''Execute function tuple'''
    error_codes = []
    for statement in func_tuple:
        func = statement[0]
        args = statement[1]
        error_codes.append(func(**args))
    if error_codes:
        return error_codes[-1]
    return None
