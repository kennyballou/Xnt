#!/usr/bin/env python
__version__ = "Xnt 0.2.2"

def target(fn):
    def wrap():
        print(fn.__name__ + ":")
        return fn()
    wrap.decorator = "target"
    return wrap
