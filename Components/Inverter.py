#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:25:28 2020

@author: judragon
"""
from GroupTortureProject.Components.Init import Init

# Creating a class for the components: inverter
class Inverter(Init):
    """
    This is the Inverter digital component. This class will take a given binary
    input an return the inverted value.
    """
    def __init__(self, name):
        super().__init__(name)

    def Output(self, input):
        self.result = int(not (input))
        return self.result
