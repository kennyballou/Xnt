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

.. _xnt.build.make.ant:
.. function:: ant(path="", target="")

    Invoke Apache Ant in either the current working directory or the specified
    directory using the empty (default) target or the specified target.

Gnu Make
--------

.. _xnt.bulid.make.make:
.. function:: make(path="", target="")

    Invoke Gnu Make (*make*) in either the current working directory or the
    specified directory using the empty (default) target or the specified
    target.

(.NET)Ant
---------

.. _xnt.build.make.nant:
.. function:: nant(path="", target="")

    Invoke NAnt in either the current working directory or the specified
    directory using the empty (default) target or the specified target.

Compiler Collection
===================

For all compilers so far, Xnt assumes they are installed and in your `$PATH`.
If they are not, an error will be thrown (by subprocess)

gcc/g++
-------

.. _xnt.build.cc.gcc:
.. function:: gcc(src, flags=None)

    Compile `src` with the `gcc` to the default `out` (:ref:`defaultOut`) of
    that source. Passing `flags` as given.

.. _xnt.build.cc.gcc_o:
.. function:: gcc_o(src, o, flags=None)

    Compile `src` with `gcc` to the out file specified by `o`. Passing `flags`
    as given.

.. _xnt.build.cc.gpp:
.. function:: gpp(src, flags=None)

    Compile `src` with `g++` to the default `out` (:ref:`defaultOut`) of that
    source. Passing `flags` as given.

.. _xnt.bulid.cc.gpp_o:
.. function:: gpp_o(src, o, flags=None)

    Compile `src` with `g++` to the out file specified by `o`. Passing `flags`
    as given.

Javac
-----

.. _xnt.build.cc.javac:
.. function:: javac(src, flags=None)

    Compile `src` with `javac` to the default out file for the source. Passing
    `flags` as given.

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

pdflatex
--------

.. _xnt.build.tex.pdflatex:
.. function:: pdflatex(document, path="./", bibtex=False, makeglossary=False)

    Use `pdflatex` to build a LaTeX PDF document. Can optionally execute steps
    to properly build in `bibtex` references and/ or glossaries.

    Where *document* is the master tex file of the document and *path* is the
    full or relative path to exectue `pdflatex` in.
