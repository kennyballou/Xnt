#!/usr/bin/env python
"""Main xnt module

Contains definition for version (referenced from version module), license,
target decorator, and imports task methods from tasks module
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

import logging
import xnt.version
import xnt.tasks
__version__ = "Xnt " + xnt.version.__version__
__license__ = """
   Xnt -- A Wrapper Build Tool
   Copyright (C) 2012  Kenny Ballou

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

def target(*args, **kwargs):
    """Decorator function for marking a method in
       build file as a "target" method, or a method meant
       to be invoked from Xnt
    """
    def w_target(target_fn):
        """target wrapping function"""
        has_run = [False,]
        def wrap():
            """Inner wrapper function for decorator"""
            if not has_run[0] or kwargs.get('always_run', False):
                has_run[0] = True
                print(target_fn.__name__ + ":")
                return target_fn()
            return None
        wrap.decorator = "target"
        wrap.__doc__ = target_fn.__doc__
        return wrap
    if len(args) == 1 and callable(args[0]):
        return w_target(args[0])
    return w_target

def list_targets(buildfile):
    '''List targets (and doctstrings) of the provided build module

    :param buildfile: path to build file to list targets'''
    return xnt.tasks.__apply__(xnt.tasks.__xnt_list_targets__(buildfile))

def expandpath(path_pattern):
    '''return glob expansion of the given pattern

    :param path_pattern: pattern to expand
    :rtype: generator of paths
    :return: list of matching paths and/ or files'''
    return xnt.tasks.__apply__(xnt.tasks.__expandpath__(path_pattern))

#pylint: disable=C0103
def cp(srcdir=None, dstdir=None, files=None):
    '''copy srcdir or files to destdir

    Copy files or a folder to the destination

    :param srcdir: source directory or single file to copy
    :param dstdir: destination file or folder
    :param files: list of files to copy'''
    return xnt.tasks.__apply__(xnt.tasks.__copy__(srcdir, dstdir, files))

#pylint: disable=C0103
def mv(src, dst):
    '''Move src to dst

    Move (copy and remove) the source file or folder to the destination file or
    folder

    :param src: Source file or folder
    :param dst: Destination file or folder'''
    return xnt.tasks.__apply__(xnt.tasks.__move__(src, dst))

def mkdir(directory, mode=0o755):
    '''Create directory with specified mode

    :param directory: name of directory to create
    :param mode: Permission mode of new directory. Default: 755'''
    return xnt.tasks.__apply__(xnt.tasks.__mkdir__(directory, mode))

#pylint: disable=C0103
def rm(*fileset):
    '''Remove set of files

    :param fileset: list of files to remove'''
    return xnt.tasks.__apply__(xnt.tasks.__remove__(*fileset))

def create_zip(directory, zipfilename):
    '''Compress folder to create zip file

    :param directory: directory to zip
    :param zipfilename: name of resulting compression'''
    return xnt.tasks.__apply__(xnt.tasks.__zip__(directory, zipfilename))

def echo(msg, tofile):
    '''Echo a message to a file

    :param msg: content to write
    :param tofile: name of file to write message'''
    return xnt.tasks.__apply__(xnt.tasks.__echo__(msg, tofile))

def log(msg, lvl=logging.INFO):
    '''Log message with LOGGER instance

    :param msg: message to log
    :param lvl: Level of message. Default INFO'''
    return xnt.tasks.__apply__(xnt.tasks.__log__(msg, lvl))

def xntcall(buildfile, targets=None, props=None):
    '''Invoke xnt with different build file

    :param buildfile: name of build file to load
    :param targets: list of targets to invoke
    :param props: dictionary of properties to pass'''
    return xnt.tasks.__apply__(
        xnt.tasks.__xntcall__(buildfile, targets, props))

def call(command, stdout=None, stderr=None):
    '''Execute given command, redirectoring stdout and stderr

    :param command: command, in the form of a list, to execute
    :param stdout: file to write stdout
    :param stderr: file to write stderr'''
    return xnt.tasks.__apply__(xnt.tasks.__call__(command, stdout, stderr))

def setup(commands, directory=None):
    '''Invoke ``setup.py`` file in current or given directory

    :param commands: list of commands (or options) to pass
    :param directory: directory of setup file to run against'''
    return xnt.tasks.__apply__(
        xnt.tasks.__setup__(commands=commands, directory=directory))

def which(program):
    '''Return (first) path of given executale, ``program``

    :param program: program name to search'''
    return xnt.tasks.__apply__(xnt.tasks.__which__(program))

def in_path(program):
    '''Return true if program is in path, otherwise false

    :param program: program name to search
    :return: True if program in path else false'''
    return xnt.tasks.__apply__(xnt.tasks.__in_path__(program))

def gcc(src, output=None, flags=None):
    '''GCC compiler

    :param src: C source file to compile
    :param output: Optional name of object
    :param flags: list of compiler flags'''
    import xnt.tasks.build.cc
    return xnt.tasks.__apply__(xnt.tasks.build.cc.__gcc__(src, output, flags))

def gpp(src, output=None, flags=None):
    '''G++ compiler

    :param src: C++ source file to compile
    :param output: Optional name of object
    :param flags: List of compiler flags'''
    import xnt.tasks.build.cc
    return xnt.tasks.__apply__(xnt.tasks.build.cc.__gpp__(src, output, flags))

def javac(src, flags=None):
    '''Java compiler

    :param src: Java source class
    :param flags: List of compiler flags'''
    import xnt.tasks.build.cc
    return xnt.tasks.__apply__(
        xnt.tasks.build.cc.__javac__(src, flags))

def nvcc(src, output=None, flags=None):
    '''CUDA C/C++ compiler

    :param src: CUDA source to compile
    :param output: Optional object name
    :param flags: List of compiler flags'''
    import xnt.tasks.build.cc
    return xnt.tasks.__apply__(
        xnt.tasks.build.cc.__nvcc__(src, output, flags))

#pylint: disable=W0621
def ant(target, path=None, flags=None, pkeys=None, pvalues=None):
    '''Apache Ant Build Wrapper

    :param target: target to invoke
    :param path: path to ant build
    :param flags: list of flags to pass to ant
    :param pkeys: key names for properties to pass to ant
    :param pvalues: value names for properties to pass to ant'''
    import xnt.tasks.build.make
    return xnt.tasks.__apply__(
        xnt.tasks.build.make.__ant__(target, path, flags, pkeys, pvalues))

#pylint: disable=W0621
def make(target, path=None, flags=None, pkeys=None, pvalues=None):
    '''GNU Make Build Wrapper

    :param target: target to invoke
    :param path: path to makefile
    :param flags: list of flags to pass to make
    :param pkeys: key names for properties to pass to make
    :parram pvalues: value names for properties to pass to make'''
    import xnt.tasks.build.make
    return xnt.tasks.__apply__(
        xnt.tasks.build.make.__make__(target, path, flags, pkeys, pvalues))

#pylint: disable=W0621
def nant(target, path=None, flags=None, pkeys=None, pvalues=None):
    '''.NET Ant Build Wrapper

    :param target: target to invoke
    :param path: path to ant build
    :param flags: list of flags to pass to ant
    :param pkeys: key names for properties to pass to ant
    :param pvalues: value names for properties to pass to ant'''
    import xnt.tasks.build.make
    return xnt.tasks.__apply__(
        xnt.tasks.build.make.__nant__(target, path, flags, pkeys, pvalues))

def gitclone(url, dest=None, branch=None):
    '''Git Clone

    :param url: URL to respository
    :param dest: destination directory or name of repository
    :param branch: branch name to clone'''
    import xnt.tasks.vcs.git
    return xnt.tasks.__apply__(
        xnt.tasks.vcs.git.__gitclone__(url, dest, branch))

def gitpull(path, remote=None, branch=None):
    '''Git pull

    :param path: local path to git repository
    :param remote: repository remote to pull
    :param branch: branch name to pull'''
    import xnt.tasks.vcs.git
    return xnt.tasks.__apply__(
        xnt.tasks.vcs.git.__gitpull__(path, remote, branch))

def hgclone(url, dest=None, rev=None, branch=None):
    '''HG clone

    :param url: URL to repository
    :param dest: Directory or name of repository
    :param rev: Revision to clone
    :param branch: Branch to clone'''
    import xnt.tasks.vcs.hg
    return xnt.tasks.__apply__(xnt.tasks.vcs.hg.__hgclone__(
        url,
        dest,
        rev,
        branch))

def hgfetch(path, source=None):
    '''HG Pull

    :param path: local path to repository
    :param source: remote source to pull'''
    import xnt.tasks.vcs.hg
    return xnt.tasks.__apply__(xnt.tasks.vcs.hg.__hgfetch__(path, source))

def cvsco(module, rev=None, dest=None):
    '''CVS Checkout

    :param module: CVS module to checkout
    :param rev: Revision to checkout
    :param dest: Destination directory or name'''
    import xnt.tasks.vcs.cvs
    return xnt.tasks.__apply__(xnt.tasks.vcs.cvs.__cvsco__(module, rev, dest))

def cvsupdate(path):
    '''CVS Update

    :param path: local path to csv checkout'''
    import xnt.tasks.vcs.cvs
    return xnt.tasks.__apply__(xnt.tasks.vcs.cvs.__cvsupdate__(path))

def pdflatex(document, directory=None, bibtex=False, makeglossary=False):
    '''PDFLaTeX

    :param document: name of document.tex
    :param directory: path to document
    :param bibtex: generate bibtex entries: default false
    :param makeglossary: generate glossary entries: default false'''
    import xnt.tasks.build.tex
    return xnt.tasks.__apply__(xnt.tasks.build.tex.__pdflatex__(
        document,
        directory,
        bibtex,
        makeglossary))

def latexclean(directory=None, remove_pdf=False):
    '''Clean up PDFLaTeX generated files

    :param directory: path to document
    :param remove_pdf: remove the generated pdf: default false'''
    import xnt.tasks.build.tex
    return xnt.tasks.__apply__(
        xnt.tasks.build.tex.__clean__(directory, remove_pdf))
