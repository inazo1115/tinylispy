# -*- coding: utf-8 -*-

import re

from eval import *


def read_list(expr):
    ret = []
    rest = expr[1:]
    while True:
        x, rest = read_expr(rest)
        if isinstance(x, str):
            if x == '<empty_expr>':
                raise Exception('Miss )')
            if x == '<close_paren>':
                break
        ret.append(x)
    return LIST(*ret), rest


def read_symbol(expr):
    """
    e.g. foo
    """
    m = re.match('^[a-zA-Z_]\w*', expr)
    ret = SYMBOL(str(expr[:m.end()]))
    rest = expr[m.end():]
    return ret, rest


def read_number(expr):
    """
    e.g. 123
    """
    m = re.match('\d+', expr)
    ret = NUMBER(int(expr[:m.end()]))
    rest = expr[m.end():]
    return ret, rest


def read_string(expr):
    """
    e.g. "foo"
    """
    m = re.match('^"[a-zA-Z_]\w*"', expr)
    quoted_str = str(expr[:m.end()])
    ret = STRING(quoted_str[1:-1])
    rest = expr[m.end():]
    return ret, rest


def read_expr(expr):
    if len(expr) == 0:
        return '<empty_expr>', ''
    c = expr[0]
    if c.isalpha():
        ret, rest = read_symbol(expr)
        return ret, rest
    if c.isdigit():
        ret, rest = read_number(expr)
        return ret, rest
    if c == '"':
        ret, rest = read_string(expr)
        return ret, rest
    if c == ' ' or c == '\n':
        ret, rest = read_expr(expr[1:])
        return ret, rest
    if c == '(':
        ret, rest = read_list(expr)
        return ret, rest
    if c == ')':
        return '<close_paren>', expr[1:]
    raise Exception("Unexpected expr: '{}'".format(expr))
