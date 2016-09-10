# -*- coding: utf-8 -*-

import sys
sys.path.append('./tinylispy')

from nose.tools import eq_, ok_

from tinylispy.env import Env
from tinylispy.eval import *
from tinylispy.main import *


def test_eval_pos0():
    actual = NIL().eval(Env({}))
    expected = NIL()
    eq_(actual, expected)


def test_eval_pos1():
    actual = LIST(FUNCTION(fn_add),
                  NUMBER(1),
                  NUMBER(2)).eval(Env({}))
    expected = NUMBER(3)
    eq_(actual, expected)


def test_eval_pos2():
    actual = LIST(SPECIAL_FORM(sf_if),
                  TRUE(),
                  NUMBER(10),
                  NUMBER(20)).eval(Env({}))
    expected = NUMBER(10)
    eq_(actual, expected)


def test_eval_pos3():
    env = Env({})
    env.push({SYMBOL('foo'): NUMBER(100)})
    actual = SYMBOL('foo').eval(env)
    expected = NUMBER(100)
    eq_(actual, expected)


def test_eval_pos4():
    env = Env({SYMBOL('if'): SPECIAL_FORM(sf_if)})
    actual = LIST(SYMBOL('if'),
                  TRUE(),
                  NUMBER(10),
                  NUMBER(20)).eval(env)
    expected = NUMBER(10)
    eq_(actual, expected)


def test_eval_pos5():
    env = Env({SYMBOL('add'): FUNCTION(fn_add)})
    actual = LIST(SYMBOL('add'),
                  NUMBER(10),
                  NUMBER(20)).eval(env)
    expected = NUMBER(30)
    eq_(actual, expected)
