===============
Build Reference
===============

Xnt has several "build" modules to aid you in your compliation and project/
sub-project build steps

Overview
========

* `Make`_

* `Compiler Collection`_

* `Tex`_

Make
====

Apache Ant
----------

.. autofunction:: xnt.build.make.ant
   :noindex:


Gnu Make
--------

.. autofunction:: xnt.build.make.make
   :noindex:

(.NET)Ant
---------

.. autofunction:: xnt.build.make.nant
   :noindex:

Compiler Collection
===================

For all compilers so far, Xnt assumes they are installed and in your `$PATH`.
If they are not, an error will be thrown (by subprocess)

gcc/g++
-------

.. autofunction:: xnt.build.cc.gcc
   :noindex:

.. autofunction:: xnt.build.cc.gcc_o
   :noindex:

.. autofunction:: xnt.build.cc.gpp
   :noindex:

.. autofunction:: xnt.build.cc.gpp_o
   :noindex:

Javac
-----

.. autofunction:: xnt.build.cc.javac
   :noindex:


NVCC
----

.. autofunction:: xnt.build.cc.nvcc
   :noindex:

.. autofunction:: xnt.build.cc.nvcc_o
   :noindex:

Notes
-----

.. _defaultOut:

Default out
~~~~~~~~~~~

Most, if not all, compilers have a default name given to compiled binaries when
no output file name is given. For example, `gcc` will give code with a `main`
method a name of `a.out` or `%.o` for objects, and so on. `javac` defaults to
`<class-name>.class`.

.. _recompile:

Recompile
~~~~~~~~~

At the current moment, all compile wrappers do not do "smart" checks for
compilation. That is, *all* compile steps will `rebuild` regardless if the
binary file is modified later than the source file. This would be a nice
feature, but I fear it would be too expensive (complicated) and out of the
scope of this project to implement correctly.

Tex
===

Building LaTeX documents can be confusing and sometimes tricky to do correctly.

.. autofunction:: xnt.build.tex.pdflatex
   :noindex:

.. autofunction:: xnt.build.tex.clean
   :noindex:
