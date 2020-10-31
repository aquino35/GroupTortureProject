#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:25:28 2020

@author: judragon
"""
from Components.BaseComponent import BaseComponent

# Creating a class for the components: inverter
class Inverter(BaseComponent):
    """
        Description:
        This is the Inverter component class of the digital system.
        This class will take a given binary input an return the inverted value.
    """
    def __init__(self, name):
        super().__init__(name)

    def Output(self, input):
        self.checked = False
        self.checkInputErrors(input)
        self.result = int(not (input))
        return self.result

    def checkInputErrors(self, input):
        """
            Description:
            Checks if input value is binary and not any other other number (including none).
            :parameter (input): Value to be checked.
        """
        if not self.checked:
            if input == None:
                raise ValueError(f'{self.name} object can only be instantiated with a binary value')
            else:
                self.checked = True





