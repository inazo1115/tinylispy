#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import traceback

from env import Env
from eval import *
from read import *


def sf_if(env, *args):
    if len(args) != 3:
        raise Exception('Malformed if')
    cond = args[0].eval(env)
    if cond == TRUE():
        return args[1].eval(env)
    return args[2].eval(env)


def sf_quote(env, *args):
    if len(args) != 1:
        raise Exception('Malformed quote')
    return args[0]


def sf_lambda(env, *args):
    """
    e.g. (lambda (x y) (add x y))
    """
    return PROCEDURE(env, *args)


def sf_define(env, *args):
    if len(args) != 2:
        raise Exception('Malformed define')
    env.define(args[0], args[1].eval(env))
    return NIL()


def sf_update(env, *args):
    if len(args) != 2:
        raise Exception('Malformed update')
    env.update(args[0], args[1].eval(env))
    return NIL()


def fn_add(env, *args):
    ret = 0
    for i in args:
        ret += i.value
    return NUMBER(ret)


def fn_sub(env, *args):
    ret = args[0].value
    for i in args[1:]:
        ret -= i.value
    return NUMBER(ret)


def fn_mul(env, *args):
    ret = 1
    for i in args:
        ret *= i.value
    return NUMBER(ret)


def fn_div(env, *args):
    ret = args[0].value
    for i in args[1:]:
        ret /= i.value
    return NUMBER(ret)


def fn_mod(env, *args):
    if len(args) != 2:
        raise Exception('Malformed mod')
    return NUMBER(args[0] % args[1])


def fn_minus(env, *args):
    if len(args) != 1:
        raise Exception('Malformed minus')
    return NUMBER(-args[0])


def fn_println(env, *args):
    if len(args) != 1:
        raise Exception('Malformed println')
    print(args[0])
    return NIL()


def make_global_frame():
    return {SYMBOL('true')    : TRUE(),
            SYMBOL('nil')     : NIL(),
            SYMBOL('if')      : SPECIAL_FORM(sf_if),
            SYMBOL('quote')   : SPECIAL_FORM(sf_quote),
            SYMBOL('lambda')  : SPECIAL_FORM(sf_lambda),
            SYMBOL('define')  : SPECIAL_FORM(sf_define),
            SYMBOL('update')  : SPECIAL_FORM(sf_update),
            SYMBOL('add')     : PRIMITIVE_FUNC(fn_add),
            SYMBOL('sub')     : PRIMITIVE_FUNC(fn_sub),
            SYMBOL('mul')     : PRIMITIVE_FUNC(fn_mul),
            SYMBOL('div')     : PRIMITIVE_FUNC(fn_div),
            SYMBOL('mod')     : PRIMITIVE_FUNC(fn_mod),
            SYMBOL('minus')   : PRIMITIVE_FUNC(fn_minus),
            SYMBOL('println') : PRIMITIVE_FUNC(fn_println)}


def repl():
    env = Env(make_global_frame())
    while True:
        try:
            print('tinylispy>>> ', end='', flush=True)
            expr = sys.stdin.readline().strip()
            ast = read_expr(expr)[0]
            res = ast.eval(env)
            print(res)
        except Exception as e:
            print(str(e))
#            print(traceback.format_exc())


if __name__ == '__main__':
    repl()
