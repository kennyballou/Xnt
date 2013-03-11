==============
Task Reference
==============

Xnt has a number of built in tasks to aid you in writing a simple build file.

Overview of Tasks
=================

* `File Tasks`_

* `Archive Tasks`_

* `Miscellaneous Tasks`_

* `Compile Tasks`_

* `SCM Tasks`_

File Tasks
==========

.. _xnt.tasks.expandpath:
.. function:: expandpath(path)

    Return a generator for glob expansion of *path*

.. _xnt.tasks.cp:
.. function:: cp(src="", dst="", files=None)

    Copy the source file or directory (*src*) OR files/folders (*files*) to
    destination file or directory (*dst*)

.. _xnt.tasks.mv:
.. function:: mv(src, dst)

    Move the source file or directory (*src*) to destination file or
    directory (*dst*)

.. _xnt.tasks.mkdir:
.. function:: mkdir(dir, mode=0o777)

    Create a directory specified by *dir* with default mode (where supported)
    or with the specified mode

    Notice, if the directory already exists, *mkdir* will not attempt to
    creat it again (or change the mode)

.. _xnt.tasks.rm:
.. function:: rm(*fileset)

    Attempt to remove all the directories given in fileset. Before *rm* tries
    to delete each element of fileset, it attempts to expand it first, thus
    allowing the passing of glob elements.

Archive Tasks
=============

.. _xnt.tasks.create_zip:
.. function:: create_zip(directory, zipfilename)

    Zip the specified *directory* into the zip file specified by *zipfilename*

Miscellaneous Tasks
===================

.. _xnt.tasks.echo:
.. function:: echo(msg, tofile)

    Write the given message to a file

    *echo* will handle opening and closing the file

.. _xnt.tasks.log:
.. function:: log(msg="", lvl=logging.INFO)

    Write the message (*msg*) to the *xnt.tasks* logger using either the
    default log level (*INFO*) or any other valid specified value

.. _xnt.tasks.call:
.. function:: call(command, stdout=None, stderr=None)

    Invoke the command specified, redirecting standard output and standard
    error as specified.

    *command* must be in the form of a list for :mod:`subprocess`

    *stdout* and *stderr* must be an open file handle. [However, that may
    change; I'm not sure how I feel about that yet.]

.. _xnt.tasks.xntcall:
.. function:: xntcall(buildfile, targets=None, props=None)

    Invoke the *target(s)* of a build file in a different *path*.

    *target* is the name of the target to invoke (similar to *target* of a
    regular invocation.

    *buildfile* is the path (relative or full) and build file to use

Compile Tasks
=============

.. _xnt.tasks.setup:
.. function:: setup(commands, directory="")

    Invoke Python setup.py given the list of *commands* (or options) in the
    current directory or in a different directory, specified by *directory*.

SCM Tasks
=========

.. _xnt.vcs.hg:

Mercurial Tasks
---------------

.. _xnt.vcs.hg.hgclone:
.. function:: hgclone(url, dest=None, rev=None, branch=None)

    Clone the Mercurial repository at *url* (This can be any valid URI, Local,
    SSH, HTTP(S)...) into either the default destination or a specified
    directory (relative to the current working directory).

    *rev* and *branch* can be used to clone a specific revision or a specific
    branch of the repository, respectively.

.. _xnt.vcs.hg.hgfetch:
.. function:: hgfetch(path, source='default')

    Fetch any updates from either the default source or a specified source for
    the repository specified by *path*

.. _xnt.vcs.git:

Git Tasks
---------

.. _xnt.vcs.git.gitclone:
.. function:: gitclone(url, dest=None, branch=None)

    Clone the Git repository at *url* (This can be any valid URI: Local, SSH,
    Git, HTTP(S)...) into either the default destination or specified directory
    (relative to the current working directory).

.. _xnt.vcs.git.gitpull:
.. function:: gitpull(path, source="origin", branch="master")

    Pull any updates from either the default source and/ or specified branch
    into the existing Git repository located at *path*.

.. _xnt.vcs.cvs:

CVS Tasks
---------

.. _xnt.vcs.cvs.cvsco:
.. function:: cvsco(module, rev="", dest="")

    Checkout the CVS module specified by *module*; getting the HEAD revision or
    any valid revision specified by *rev* and putting it into the default
    directory or the specified directory, *dest* (relative to the current
    working directory).

.. _xnt.vcs.cvs.cvsupdate:
.. function:: cvsupdate(path)

    Update the CVS module located at *path*.
