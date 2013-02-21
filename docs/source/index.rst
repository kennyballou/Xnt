.. Xnt documentation master file, created by
   sphinx-quickstart2 on Mon Oct 29 17:52:47 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Xnt's documentation!
===============================

Xnt is a high-level wrapper build tool for better managing your projects' build
process. It allows you to include multiple sub-build tools (such as: ``make``,
``ant``, ``nant`` and potentially more) in a single project while exposing a
single and simple interface.

Why you should use Xnt:

- Xnt exposes a single and simple interface for building your project

- Xnt is written in Python, making it easy to expand and extend your build
  targets

- Your build targets will be described in Python, making it much easier and
  quicker to write build files for new and existing projects

Contents:

.. toctree::
   :maxdepth: 2

   xenant
   buildfile
   taskreference
   buildreference

Motivation
==========

When writing something such as a build tool, there is always the question:
"why?". Why write yet another build tool?

Well, there are several reasons that are the backing motivation:

First, developing a variety of software, using one and only one build tool for
every project is nearly (if not entirely) impossible. There is a desire to have
a consistent build step and process when testing and deploying. Given the
environment in which the code is written is heterogeneous, having one uniform
build tool that wraps itself around the other ones (and has the ability to
expand to new ones) is ideal.

Second, short of dropping into the language the build tool was written in,
expanding some build steps is very difficult (or at least can be). Further
there can be complicated build targets that require some interesting and
potentially involved (smelly) procedures to be accomplished, that may or may
not be easy to describe in the build file or in the native language. Therefore,
having a wrapping build framework/ tool that is written in an easy to read and
write language, such as Python, these complicated steps can depend less on some
funky new build library (further adding to the dependency tree) and can become
just implementation details (assuming, of course, you buy into Xnt first).

Last, and most certainly the least, I wanted to explore the idea. I wanted to
write something that made me think about solving some of the problems
challenged by such a tool.

Installing
==========

To install, you can either install from source or use Pip.

Source
------

To install from Source (stable), run the following:

.. parsed-literal::

    curl -0 http://pypi.python.org/packages/source/X/Xnt/Xnt-|release|.tar.gz \
    > Xnt.tar.gz
    tar -xzvf Xnt.tar.gz
    cd Xnt-|release|
    python[2] setup.py install [--user]

Development Build
-----------------

To build and install from a development build(non-stable/ testing), run::

    git clone git://github.com/devnulltao/Xnt.git
    cd Xnt
    python[2] setup.py install [--user]


Or if you prefer, you can download a zip of the latest build and install; run::

    curl -0 https://github.org/devnulltao/Xnt/archive/master.zip > Xnt.zip
    unzip Xnt.zip
    cd Xnt
    python[2] setup.py install [--user]

Pip
---

To install using Pip, run::

    pip[2] install Xnt [--user]

Using `--user`
--------------

If you install using the ``--user`` option in either source or PyPi installs,
you may need to add ``~/.local/bin/`` to your ``PATH`` environment variable.

Windows
-------

If on windows, after installing you will need to edit your ``PATH`` environment
variable to include the installation location (either
``<python_install_dir>\Scripts`` or ``$HOME\AppData\Roaming\Python\Scripts``).


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
