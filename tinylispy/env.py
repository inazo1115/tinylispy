# -*- coding: utf-8 -*-


class Env:
    def __init__(self, global_flame):
        self.__stack = []
        self.__stack.append(global_flame)

    def lookup(self, symbol):
        return self.__lookup_flame(symbol).get(symbol)

    def __lookup_flame(self, symbol):
        for i in range(len(self.__stack)):
            flame = self.__stack[len(self.__stack) - i - 1]
            if symbol in flame:
                return flame
        raise Exception('Symbol {} not found.'.format(symbol))

    def define(self, symbol, value):
        flame = self.__stack[len(self.__stack) - 1]
        if symbol in flame:
            raise Exception('{} has already defined.'.format(symbol))
        flame[symbol] = value

    def update(self, symbol, value):
        flame = self.__lookup_flame(symbol)
        flame[symbol] = value

    def push(self, new_flame):
        self.__stack.append(new_flame)

    def pop(self):
        self.__stack.pop()
