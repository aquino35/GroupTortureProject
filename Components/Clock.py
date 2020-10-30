# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:54:43 2020

@author: aespi
"""
from Components.BaseComponent import BaseComponent


class clock(BaseComponent):
    """ """
    def __init__(self, name, input):
        super().__init__(name)
        # self.Output()
        self.result = input
        self.checked = False
        self.checkInputErrors(input)

    def Output(self,input):
        self.result = int(not (self.result))
        return self.result

    def checkInputErrors(self, input):
        # Checks once if the gate has the correct amount of inputs
        if not self.checked:
            if not (input == 1 or input == 0) or input == None:
                raise Exception("A clock object can only be instantiated with the value '0' or '1'")
            else:
                self.checked = True







