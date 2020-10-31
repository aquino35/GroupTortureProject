#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:38:35 2020

@author: osvaldo
"""
from Components.BaseComponent import BaseComponent


class const(BaseComponent):
    """
    This is the constant digital component. This class will take a given
    input an return the same value.
    """
    def __init__(self, name,result):
        super().__init__(name)
        self.checked = False
        self.checkInputErrors(input)
        self.result = result


    def checkInputErrors(self, input):
        # Checks once if the gate has the correct amount of inputs
        if not self.checked:
            if  input==None:
                raise Exception("A constant object can only be instantiated with the value '0' or '1'")
            else:
                self.checked = True


