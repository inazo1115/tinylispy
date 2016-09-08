# -*- coding: utf-8 -*-


class SEXPR:
    def __str__(self):
        return '{}'.format(type(self).__name__)


class LIST(SEXPR):
    def __init__(self, *lst):
        self.__lst = lst

    def eval(self, env):
        return self.__lst[0].apply(env, *self.__lst[1:])


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


class VALUE1(SEXPR):
    def __init__(self, value):
        self.__value = value

    def eval(self, env):
        return self

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return '{}:{}'.format(type(self).__name__,
                              str(self.__value))


class TRUE(VALUE0):
    pass


class NIL(VALUE0):
    pass


class NUMBER(VALUE1):
    pass


class STRING(VALUE1):
    pass


def sf_if(env, *args):
    if len(args) != 3:
        raise Exception('Malformed if')
    cond = args[0].eval(env)
    if isinstance(cond, TRUE):
        return args[1].eval(env)
    return args[2].eval(env)


def fn_add(env, *args):
    ret = 0
    for i in args:
        ret += i.value
    return NUMBER(ret)


def fn_println(env, *args):
    if len(args) != 1:
        raise Exception('Malformed println')
    print(args[0])
    return NIL()
