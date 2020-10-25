# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:54:43 2020

@author: aespi
"""
from GroupTortureProject.Components.Init import Init


class clock(Init):
    def __init__(self, name, input):
        super().__init__(name)
        self.result = input

    def Operate(self):
        self.result = int(not (self.result))
        return self.result

    def Output(self,output1):
        output1 = self.result
        return output1
    def output(self):
        final_value = self.result
        return final_value








