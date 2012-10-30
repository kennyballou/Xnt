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
be used by the ``help`` command, see [make reference]). Next, we define the
function; this function name *is* the name target. That is, the name given to
the function will be name given to the command to invoke this target. Further,
we have the docstring; (this is also used by the ``help`` command) the
docstring provides a quick description of the purpose of the target, or what
the target accomplishes when ran. Finally, we call ``mkdir`` of the
``xnt.tasks`` module. This function, if not obvious by the name, creates a
directory named 'build' (see [make reference]).
