#!/usr/bin/env python
# -*- coding: utf-8 -*-

from eval import *
from read import *
from env import Env


if __name__ == '__main__':
    env = Env({SYMBOL('if'): SPECIAL_FORM(sf_if),
               SYMBOL('true'): TRUE()})
    print(read_expr('(if true 1 2)')[0].eval(env))
