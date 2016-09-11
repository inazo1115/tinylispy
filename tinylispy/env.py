# -*- coding: utf-8 -*-


class Env:
    def __init__(self, flame, outer=None):
        self.__flame = flame
        self.__outer = outer

    def __lookup_flame(self, symbol):
        if symbol in self.__flame:
            return self.__flame
        if self.__outer is None:
            raise Exception('Symbol {} not found.'.format(symbol))
        return self.__outer.__lookup_flame(symbol)

    def lookup(self, symbol):
        return self.__lookup_flame(symbol).get(symbol)

    def define(self, symbol, value):
        if symbol in self.__flame:
            raise Exception('{} has already defined.'.format(symbol))
        self.__flame[symbol] = value

    def update(self, symbol, value):
        flame = self.__lookup_flame(symbol)
        flame[symbol] = value

    def _dump(self):
        """
        For debug
        """
        print('>>>>>>>>')
        for k, v in self.__flame.items():
            print("{}:{}".format(str(k), str(v)))
        print('<<<<<<<<')
        if self.__outer is not None:
            self.__outer._dump()
