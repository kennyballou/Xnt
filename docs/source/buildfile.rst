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

.. _runningXnt:

Running Xnt
-----------

Invoking Xnt from the command line is very simple and very similar to how other
build tools are invoked (this was intentional).

.. _defaultUse:

Default Use
~~~~~~~~~~~

The most simplistic use of Xnt is as follows::

    $ xnt

This will attempt to invoke the `default` target in the current directory's
`build.py`.

.. _invokeTarget:

Invoke a Target
~~~~~~~~~~~~~~~

To invoke a particular target, use::

    $ xnt {target}

Where the value of `{target}` is dependent on your particular `build.py` file.

.. _specialTargets:

Special Targets
~~~~~~~~~~~~~~~

"Special" targets (for lack of a better name) are targets that do not exist in
the build script, but rather are a part of Xnt.

Thus far, I have only defined one "special" target, ``list-targets`` (I don't
think this name is going to change again ...).

* ``list-targets`` does exactly what the name should suggest: it prints a list
  of the targets found in the current directory's `build.py` script, along with
  any docstrings that may be defined with them.

Usage::

    $ xnt list-targets

.. _xntOptions:

Options
~~~~~~~

Xnt also has a few "options" that may be provided along with a regular targets.

Usage::

    $ xnt [options] [target]

Where options can be any and all of the following (unless otherwise specified):

* ``-v``: add verbose output to the execution of Xnt

* ``--version``: Print the version of Xnt and exit

* ``--usage``: Print version, license, usage information and quit. [I've
  debatted between putting this as a special target and leaving it as an
  option.. not sure which is better...]
