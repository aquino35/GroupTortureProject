#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:38:35 2020

@author: osvaldo
"""
from GroupTortureProject.Components.Init import Init


class const(Init):
    # pass
    def __init__(self, name,result):
        super().__init__(name)
        self.result = result

    def output(self):
        output1 = self.result
        return output1

    def Output(self,output1):
        output1 = self.result
        return output1

