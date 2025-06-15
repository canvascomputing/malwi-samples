#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TypeException(Exception):
    pass


def typesrequired(*types):
    def outer(func):
        def inner(*args):
            if len(args) != len(types):
                raise TypeException("function {0} must be called with {1} arguments".format(func.__name__, len(types)))

            for i in range(len(types)):
                if type(args[i]) is not types[i]:
                    raise TypeException("argument {0} must be of type {1}".format(i, types[i].__name__))
            result = func(*args)
            return result

        return inner

    return outer
