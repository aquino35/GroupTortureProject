# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:54:43 2020

@author: aespi
"""
from GroupTortureProject.Components.BaseComponent import BaseComponent


class clock(BaseComponent):
    """ """
    def __init__(self, name, input):
        super().__init__(name)
        # self.Output()
        self.result = input

    def Output(self,input1):
        self.result = int(not (input))
        return self.result







