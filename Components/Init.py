# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 23:36:37 2020

@author: juang
"""


class Init:
    def __init__(self, name):
        self.name = name
        # self.__result = 0
        self.result = 0

    def __repr__(self):
        return self.name

    def Output(self,output1):
        output1 = self.result
        return output1

    def output(self):
        output1 = self.result
        return output1

