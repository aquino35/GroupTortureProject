#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:25:28 2020

@author: judragon
"""
from GroupTortureProject.Components.Init import Init

# Creating a class for the components: inverter
class Inverter(Init):
    def __init__(self, name):
        super().__init__(name)
        self.result = None

    def Output(self, input):
        self.result = int(not (input))
        return self.result

    def output(self):
        output1 = self.result
        return output1
