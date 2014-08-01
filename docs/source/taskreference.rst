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

.. _xnt.tasks.vcs.hg:

Mercurial Tasks
---------------

.. autofunction:: xnt.tasks.vcs.hg.hgclone
   :noindex:

.. autofunction:: xnt.tasks.vcs.hg.hgfetch
   :noindex:

.. _xnt.tasks.vcs.git:

Git Tasks
---------

.. autofunction:: xnt.tasks.vcs.git.gitclone
   :noindex:

.. autofunction:: xnt.tasks.vcs.git.gitpull
   :noindex:

.. _xnt.tasks.vcs.cvs:

CVS Tasks
---------

.. autofunction:: xnt.tasks.vcs.cvs.cvsco
   :noindex:

.. autofunction:: xnt.tasks.vcs.cvs.cvsupdate
   :noindex:
