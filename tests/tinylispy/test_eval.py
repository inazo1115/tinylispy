# -*- coding: utf-8 -*-

from nose.tools import eq_, ok_

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
