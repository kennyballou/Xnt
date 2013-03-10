First Build File
================

Hello World Example
-------------------

Writing your first ``build.py`` file is actually quite simple. It's just
Python!::

    #!/usr/bin/env python

    def helloworld():
        print("Hello World")

Running this, we should see something similar to::

    $ xnt helloworld
    Hello World

Adding Xnt to the Mix
---------------------

Let's start to add some of the features provided by Xnt::

    #!/usr/bin/env python

    from xnt import target #For describing targets
    import xnt             #For built-in tasks

    @target
    def init():
        """
        Initialize Project Build Directories
        """
        xnt.mkdir("build")

That may be a lot to take in initially. Let's step through it.

In the first section::

    #!/usr/bin/env python

    from xnt import target #For describing targets
    import xnt             #For built-in tasks

If you're familiar with Python, you will notice there is nothing special
happening with this file yet. We are simply defining the file as a Python file,
including the ``target`` attribute from the ``xnt`` module, and importing the
``xnt`` module.

A change from previous versions: importing ``xnt`` will now implicitly import
``xnt.tasks``.

Next, we will look at a new target::

    @target
    def init():
        """
        Initialize Project Build Directories
        """
        xnt.mkdir("build")

This is a standard definition of a Python function with a decorator.

First, the ``target`` decorator marks the function definition as a target (to
be used by the ``list-targets`` command, see :ref:`otherCommands`). Next, we
define the function; this function name *is* the name of the target. That is,
the name given to the function will be the name given to the command to invoke
this target.  Further, we have the docstring; (this is also used by the
``list-targets`` command) the docstring provides a quick description of the
purpose of the target, or what the target accomplishes when ran. Finally, we
call ``mkdir`` of the ``xnt`` (internally of the ``xnt.tasks``) module. This
function, if not obvious by the name, creates a directory named 'build' (see
:doc:`taskreference`).

Return Values
=============

The targets you define can return an error code (or '0' for success) however
you see fit. Xnt will emit 'Failure' if the status code is *not* zero and will
otherwise remain silent if the code is zero. Further, the status code returned
by your target will be returned as the exit code of Xnt when finished
executing.

*Notice*, this allows Xnt to fail fast when attempting to execute multiple
targets. That is, if you specify more than one target, Xnt will stop at the
first failure.

If you don't define a return value for a target, Xnt will assume success and
return '0'.

Examples
--------

Not defining the return value::

    @target
    def foo():
        pass

Will result in (no success message; other output may be shown)::

    ...

Returning success (no success message; other output may be shown)::

    @target
    def foo():
        return 0

Will result in::

    ...

Returning failure (not 0)::

    @target
    def foo():
        return 1

Will result in::

    ...
    Failure

Most tasks have been updated to return error codes as well so that you can
return what it returns. If you find any tasks that can be updated to behave
this way, please create an issue for it.

.. _buildProperties:

Build Properties
================

As mentioned in :ref:`xntPropertiesParameters`, Xnt can accept parameters from
the command line and pass them into the build file. Xnt doesn't necessarily
expect the dictionary (named `PROPERTIES`) to exist; but if you ever intend to
use it, it will have to be defined one way or another (either to an empty
dictionary or actually hold values). For example, to define an empty
`PROPERTIES` dictionary, one could write their build file as such::

    #!/usr/bin/env python

    from xnt import target

    PROPERTIES = {}

    @target
    def foo():
        #uses properties somehow
        return 0

The hope for this feature is that it is easy to use because it borrows syntax
from other build tools that you may already be familiar with.
