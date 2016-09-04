# -*- coding: utf-8 -*-

from nose.tools import eq_, ok_

from tinylispy import util


def test_car_pos0():
    eq_(0, util.car([0, 1, 2]))


def test_car_pos1():
    eq_('a', util.car(['a', 'b', 'c']))


def test_car_pos2():
    eq_(4, util.car([4]))


def test_cdr_pos0():
    eq_([1, 2], util.cdr([0, 1, 2]))


def test_cdr_pos1():
    eq_(['b', 'c'], util.cdr(['a', 'b', 'c']))


def test_cdr_pos2():
    eq_([], util.cdr([4]))


def test_cons_pos0():
    eq_([0, 1, 2], util.cons(0, [1, 2]))


def test_cons_pos1():
    eq_([0], util.cons(0, []))


def test_cons_pos2():
    eq_([0, 'a'], util.cons(0, ['a']))


def test_cons_pos3():
    eq_([[0], 1, 2], util.cons([0], [1, 2]))
