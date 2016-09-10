# -*- coding: utf-8 -*-


class SEXPR:
    def __str__(self):
        return '{}'.format(type(self).__name__)


class LIST(SEXPR):
    def __init__(self, *lst):
        self.__lst = lst

    def eval(self, env):
        return self.__lst[0].eval(env).apply(env, *self.__lst[1:])

    def __eq__(self, other):
        return self.__lst == other.__lst

    def __hash__(self):
        return hash(self.__lst)

    def __str__(self):
        return '{}:[{}]'.format(type(self).__name__,
                                str(','.join(str(x) for x in list(self.__lst))))


class SPECIAL_FORM(SEXPR):
    def __init__(self, proc):
        self.__proc = proc

    def eval(self, env):
        return self

    def apply(self, env, *args):
        return self.__proc(env, *args)


class FUNCTION(SEXPR):
    def __init__(self, func):
        self.__func = func

    def eval(self, env):
        return self

    def apply(self, env, *args):
        args = [x.eval(env) for x in args]
        return self.__func(env, *args)


class VALUE0(SEXPR):
    def __init__(self):
        pass

    def eval(self, env):
        return self

    def __eq__(self, other):
        return type(self) == type(other)

    def __ne__(self, other):
        return type(self) != type(other)


class VALUE1(SEXPR):
    def __init__(self, value):
        self.__value = value

    def eval(self, env):
        return self

    @property
    def value(self):
        return self.__value

    def __eq__(self, other):
        return self.__value == other.__value

    def __ne__(self, other):
        return self.__value != other.__value

    def __hash__(self):
        return hash(self.__value)

    def __str__(self):
        return '{}:{}'.format(type(self).__name__,
                              str(self.__value))


class SYMBOL(VALUE1):
    def eval(self, env):
        return env.lookup(self)


class TRUE(VALUE0):
    pass


class NIL(VALUE0):
    pass


class NUMBER(VALUE1):
    pass


class STRING(VALUE1):
    pass
