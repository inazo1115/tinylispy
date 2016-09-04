# -*- coding: utf-8 -*-

from typing import List, TypeVar


T = TypeVar('T')


def car(xs: List[T]) -> T:
    return xs[0]


def cdr(xs: List[T]) -> List[T]:
    return xs[1:]


def cons(x: T, xs: List[T]) -> List[T]:
    ret = [x]
    ret.extend(xs)
    return ret
