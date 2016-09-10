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
