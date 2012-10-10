# Xnt #

A wrapper build tool

## Motivation ##

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
just implementation details. [awkward?]

Last, and most certainly the least, I wanted to explore the idea. I wanted to
write something that made me think about solving some of the problems
challenged by such a tool.

## What Xnt Is NOT ##

Calling Xnt simply a build tool is (grossly?) misleading. Xnt is not really a
build tool in the traditional sense. Like stated above, it is more a wrapper
around existing build tools. I didn't want to replace what some of these tools
already do really well (e.g. being able to describe how to compile an entire
large Java program in several lines of code using Ant).

## What Xnt IS ##

Xnt is a wrapping build tool, intended to be used with a multitude of sub-build
tools, even in the same project. Regardless of the language the project is
written in, Xnt should be able to suite your needs. If your language's build
tool is unable to do something concisely or cleanly, Python should help. [There
could be more here... I can't think of it though.]
