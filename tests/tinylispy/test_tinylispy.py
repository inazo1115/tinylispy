# -*- coding: utf-8 -*-

from nose.tools import eq_, ok_

from tinylispy import tinylispy


def test_foo():
    eq_(3, tinylispy.add(1, 2))
