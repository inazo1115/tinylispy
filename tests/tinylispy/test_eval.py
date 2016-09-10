# -*- coding: utf-8 -*-

from nose.tools import eq_, ok_

from tinylispy.env import Env
from tinylispy.eval import *


def test_pos0():
    actual = NIL().eval({})
    expected = NIL()
    ok_(actual, expected)


def test_pos1():
    actual = LIST(FUNCTION(fn_add),
                  NUMBER(1),
                  NUMBER(2)).eval({})
    expected = NUMBER(3)
    ok_(actual, expected)


def test_pos2():
    actual = LIST(SPECIAL_FORM(sf_if),
                  TRUE(),
                  NUMBER(10),
                  NUMBER(20)).eval({})
    expected = NUMBER(10)
    ok_(actual, expected)


def test_pos3():
    env = Env({})
    env.push({SYMBOL('foo'): NUMBER(100)})
    actual = SYMBOL('foo').eval(env)
    expected = NUMBER(100)
    ok_(actual, expected)


def test_pos4():
    env = Env({SYMBOL('if'): SPECIAL_FORM(sf_if)})
    actual = LIST(SYMBOL('if'),
                  TRUE(),
                  NUMBER(10),
                  NUMBER(20)).eval(env)
    expected = NUMBER(10)
    ok_(actual, expected)


def test_pos5():
    env = Env({SYMBOL('add'): FUNCTION(fn_add)})
    actual = LIST(SYMBOL('add'),
                  NUMBER(10),
                  NUMBER(20)).eval(env)
    expected = NUMBER(30)
    ok_(actual, expected)
