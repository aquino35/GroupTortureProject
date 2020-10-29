# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 23:36:37 2020

@author: juang
"""


class BaseComponent:
    """ The idea of this class is to have a base component so that we can use to inheritance
    to inherit key attributes and functions that go inside all the components.
    """
    def __init__(self, name):
        self.name = name
        self.result = None

    def __repr__(self):
        return self.name

    def Output(self,output1):
        output1 = self.result
        return output1

    def output(self):
        output1 = self.result
        return output1
