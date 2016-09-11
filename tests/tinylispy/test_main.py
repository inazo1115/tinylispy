# -*- coding: utf-8 -*-

import sys
sys.path.append('./tinylispy')

from nose.tools import eq_, ok_

from tinylispy.env import Env
from tinylispy.eval import *
from tinylispy.main import *
from tinylispy.read import *


def test_main_pos0():
    env = Env({SYMBOL('if'): SPECIAL_FORM(sf_if),
               SYMBOL('true'): TRUE()})
    actual = read_expr('(if true 1 2)')[0].eval(env)
    expected = NUMBER(1)
    eq_(actual, expected)


def test_main_pos1():
    env = Env(make_global_flame())
    actual = read_expr('((lambda (x) (add x x)) 10)')[0].eval(env)
    expected = NUMBER(20)
    eq_(actual, expected)


def test_main_pos2():
    env = Env(make_global_flame())
    actual = read_expr('((lambda (x y) (add x y)) 10 20)')[0].eval(env)
    expected = NUMBER(30)
    eq_(actual, expected)


def test_main_pos3():
    env = Env(make_global_flame())
    make_counter = """
    ((lambda ()
             (define counter
                     ((lambda (x)
                              (lambda () (update x (add x 1))
                                         x))
                              0))
             (counter)
             (counter)
             (counter)
    ))"""
    actual = read_expr(make_counter)[0].eval(env)
    expected = NUMBER(3)
    eq_(actual, expected)


def test_main_pos4():
    env = Env(make_global_flame())
    make_counter = """
    ((lambda ()
             (define counter
                     ((lambda (x)
                              (lambda () (update x (add x 1))
                                         x))
                              0))
             (counter)
             (counter)
             (counter)
             (counter)
             (counter)
    ))"""
    actual = read_expr(make_counter)[0].eval(env)
    expected = NUMBER(5)
    eq_(actual, expected)
