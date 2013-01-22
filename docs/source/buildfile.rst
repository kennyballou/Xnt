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
    import xnt.tasks       #For built-in tasks

    @target
    def init():
        """
        Initialize Project Build Directories
        """
        xnt.tasks.mkdir("build")

That may be a lot to take in initially. Let's step through it.

In the first section::

    #!/usr/bin/env python

    from xnt import target #For describing targets
    import xnt.tasks       #For built-in tasks

If you're familiar with Python, you will notice there is nothing special
happening with this file yet. We are simply defining the file as a Python file,
including the ``target`` attribute from the ``xnt`` module, and importing the
``xnt.tasks`` module.

Next, we will look at a new target::

    @target
    def init():
        """
        Initialize Project Build Directories
        """
        xnt.tasks.mkdir("build")

This is a standard definition of a Python function with a decorator.

First, the ``target`` decorator marks the function definition as a target (to
be used by the ``list-targets`` command, see :ref:`specialTargets`). Next, we
define the function; this function name *is* the name of the target. That is,
the name given to the function will be name given to the command to invoke this
target.  Further, we have the docstring; (this is also used by the
``list-targets`` command) the docstring provides a quick description of the
purpose of the target, or what the target accomplishes when ran. Finally, we
call ``mkdir`` of the ``xnt.tasks`` module. This function, if not obvious by
the name, creates a directory named 'build' (see :doc:`taskreference`).

Return Values
=============

The targets you define can return an error code (or '0' for success) however
you see fit. Doing this will give you a status message at the end of the
invocation of Xnt that will inform you if the target ran successfully or not
given your criteria (or will just say it succeeded if you don't specify a
return value at all). For example::

    @target
    def foo():
        return 0

Will result in::

    ...
    Success

Most tasks have been updated to return error codes as well to that you can
return what it returns. If you find any tasks that can be updated to behave
this way, please create an issue for it.

.. _buildProperties:

Build Properties
================

As mentioned in :ref:`xntPropertiesParameters`, Xnt can accept parameters from
the command line and pass them into the build file. Xnt doesn't necessarily
expect the dictionary (named `properties`) to exist; but if you ever intend to
use it, it will have to be defined one way or another (either to an empty
dictionary or actually hold values). For example, to define an empty
`properties` dictionary, one could write their build file as such::

    #!/usr/bin/env python

    from xnt import target

    properties = {}

    @target
    def foo():
        #uses properties somehow
        return 0

The hope for this feature is that it is easy to use because it borrows syntax
from other build tools that you may already be familiar with.
