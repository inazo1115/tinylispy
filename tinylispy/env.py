# -*- coding: utf-8 -*-


class Env:
    def __init__(self, frame, outer=None):
        self.__frame = frame
        self.__outer = outer

    def __lookup_frame(self, symbol):
        if symbol in self.__frame:
            return self.__frame
        if self.__outer is None:
            raise Exception('Symbol {} not found.'.format(symbol))
        return self.__outer.__lookup_frame(symbol)

    def lookup(self, symbol):
        return self.__lookup_frame(symbol).get(symbol)

    def define(self, symbol, value):
        if symbol in self.__frame:
            raise Exception('{} has already defined.'.format(symbol))
        self.__frame[symbol] = value

    def update(self, symbol, value):
        frame = self.__lookup_frame(symbol)
        frame[symbol] = value

    def _dump(self):
        """
        For debug
        """
        print('>>>>>>>>')
        for k, v in self.__frame.items():
            print("{}:{}".format(str(k), str(v)))
        print('<<<<<<<<')
        if self.__outer is not None:
            self.__outer._dump()
