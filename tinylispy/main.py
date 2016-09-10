#!/usr/bin/env python
# -*- coding: utf-8 -*-

from eval import *
from read import *
from env import Env


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


def fn_sub(env, *args):
    ret = args[0]
    for i in args[1:]:
        ret -= i.value
    return NUMBER(ret)


def fn_mul(env, *args):
    ret = 1
    for i in args:
        ret *= i.value
    return NUMBER(ret)


def fn_div(env, *args):
    ret = args[0]
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


def make_global_env():
    return Env({SYMBOL('true')    : TRUE(),
                SYMBOL('nil')     : NIL(),
                SYMBOL('if')      : SPECIAL_FORM(sf_if),
                SYMBOL('add')     : FUNCTION(fn_add),
                SYMBOL('sub')     : FUNCTION(fn_sub),
                SYMBOL('mul')     : FUNCTION(fn_mul),
                SYMBOL('div')     : FUNCTION(fn_div),
                SYMBOL('mod')     : FUNCTION(fn_mod),
                SYMBOL('minus')   : FUNCTION(fn_minus),
                SYMBOL('println') : FUNCTION(fn_println)})


if __name__ == '__main__':
    ast = read_expr('(if nil (add 1 2) (mul 3 4))')[0]
    res = ast.eval(make_global_env())
    print(res)
