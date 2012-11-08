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

.. function:: expandpath(path)

    Return a generator for glob expansion of *path*

.. function:: cp(src,dst)

    Copy the source file or directory (*src*) to destination file or
    directory (*dst*)

.. function:: mv(src,dst)

    Move the source file or directory (*src*) to destination file or
    directory (*dst*)

.. function:: mkdir(dir,mode=0o777)

    Create a directory specified by *dir* with default mode (where supported)
    or with the specified mode

    Notice, if the directory already exists, *mkdir* will not attempt to
    creat it again (or change the mode)

.. function:: rm(*fileset)

    Attempt to remove all the directories given in fileset. Before *rm* tries
    to delete each element of fileset, it attempts to expand it first, thus
    allowing the passing of glob elements.

Archive Tasks
=============

.. function:: zip(dir,zipfilename)

    Zip the specified directory (*dir*) into the zip file specified by
    *zipfilename*

Miscellaneous Tasks
===================

.. function:: echo(msg, tofile)

    Write the given message to a file

    *echo* will handle opening and closing the file

.. function:: log(msg="", lvl=logging.INFO)

    Write the message (*msg*) to the *xnt.tasks* logger using either the
    default log level (*INFO*) or any other valid specified value

.. function:: call(command, stdout=None, stderr=None)

    Invoke the command specified, redirecting standard output and standard
    error as specified.

    *command* must be in the form of a list for :mod:`subprocess`

    *stdout* and *stderr* must be an open file handle. [However, that may
    change; I'm not sure how I feel about that yet.]

.. function:: xnt(target, path)

    Invoke the *target* of a build file in a different *path*.

    *target* is the name of the target to invoke (similar to *target* of a
    regular invocation with the small difference, however, of not allowing an
    empty target.

    *path* is the relative or full path to where the "sub" *build.py* file can
    be found.

    **Notice**: the use of this function requires fully qualified naming.
    (i.e., *xnt.tasks.xnt(target, path)*). This will remain so until a better
    name can be found for it.

Compile Tasks
=============

.. function:: setup(commands, dir="")

    Invoke Python setup.py given the list of *commands* (or options) in the
    current directory or in a different directory, specified by *dir*.

Apache Ant
----------

.. function:: ant(path="", target="")

    Invoke Apache Ant in either the current working directory or the specified
    directory using the empty (default) target or the specified target.

Gnu Make
--------

.. function:: make(path="", target="")

    Invoke Gnu Make (*make*) in either the current working directory or the
    specified directory using the empty (default) target or the specified
    target.

(.NET)Ant
---------

.. function:: nant(path="", target="")

    Invoke NAnt in either the current working directory or the specified
    directory using the empty (default) target or the specified target.

SCM Tasks
=========

Mercurial Tasks
---------------

.. function:: hgclone(url, dest=None, rev=None, branch=None)

    Clone the Mercurial repository at *url* (This can be any valid URI, Local,
    SSH, HTTP(S)...) into either the default destination or a specified
    directory (relative to the current working directory).

    *rev* and *branch* can be used to clone a specific revision or a specific
    branch of the repository, respectively.

.. function:: hgfetch(path, source='default')

    Fetch any updates from either the default source or a specified source for
    the repository specified by *path*

Git Tasks
---------

.. function:: gitclone(url, dest=None, branch=None)

    Clone the Git repository at *url* (This can be any valid URI: Local, SSH,
    Git, HTTP(S)...) into either the default destination or specified directory
    (relative to the current working directory).

.. function:: gitpull(path, source="origin", branch="master")

    Pull any updates from either the default source and/ or specified branch
    into the existing Git repository located at *path*.

CVS Tasks
---------

.. function:: cvsco(module, rev="", dest="")

    Checkout the CVS module specified by *module*; getting the HEAD revision or
    any valid revision specified by *rev* and putting it into the default
    directory or the specified directory, *dest* (relative to the current
    working directory).

.. function:: cvsupdate(path)

    Update the CVS module located at *path*.