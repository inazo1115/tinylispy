# -*- coding: utf-8 -*-


class Env:
    def __init__(self, global_env):
        self.__stack = []
        self.__stack.append(global_env)

    def lookup(self, symbol):
        for i in range(len(self.__stack)):
            env = self.__stack[len(self.__stack) - i - 1]
            if symbol in env:
                return env.get(symbol)
        raise Exception('Symbol not found.')

    def push(self, new_env):
        self.__stack.append(new_env)

    def pop(self):
        self.__stack.pop()
