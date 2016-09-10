# -*- coding: utf-8 -*-

from nose.tools import eq_, ok_

from tinylispy.read import *


def test_read_pos0():
    expected = read_list('(1 2 (3))')[0]
    actual = LIST(NUMBER(1), NUMBER(2), LIST(NUMBER(3)))
    eq_(actual, expected)


def test_read_pos1():
    expected = read_list('("foo" 1 2)')[0]
    actual = LIST(STRING('foo'), NUMBER(1), NUMBER(2))
    eq_(actual, expected)


def test_read_pos2():
    expected = read_list('(if true 1 2)')[0]
    actual = LIST(SYMBOL('if'), SYMBOL('true'), NUMBER(1), NUMBER(2))
    eq_(actual, expected)
