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

.. autofunction:: xnt.tasks.expandpath
   :noindex:

.. autofunction:: xnt.tasks.cp
   :noindex:

.. autofunction:: xnt.tasks.mv
   :noindex:

.. autofunction:: xnt.tasks.mkdir
   :noindex:

.. autofunction:: xnt.tasks.rm
   :noindex:

Archive Tasks
=============

.. autofunction:: xnt.tasks.create_zip
   :noindex:

Miscellaneous Tasks
===================

.. autofunction:: xnt.tasks.echo
   :noindex:

.. autofunction:: xnt.tasks.log
   :noindex:

.. autofunction:: xnt.tasks.call
   :noindex:

.. autofunction:: xnt.tasks.xntcall
   :noindex:

Compile Tasks
=============

.. autofunction:: xnt.tasks.setup
   :noindex:

SCM Tasks
=========

.. _xnt.vcs.hg:

Mercurial Tasks
---------------

.. autofunction:: xnt.vcs.hg.hgclone
   :noindex:

.. autofunction:: xnt.vcs.hg.hgfetch
   :noindex:

.. _xnt.vcs.git:

Git Tasks
---------

.. autofunction:: xnt.vcs.git.gitclone
   :noindex:

.. autofunction:: xnt.vcs.git.gitpull
   :noindex:

.. _xnt.vcs.cvs:

CVS Tasks
---------

.. autofunction:: xnt.vcs.cvs.cvsco
   :noindex:

.. autofunction:: xnt.vcs.cvs.cvsupdate
   :noindex:
