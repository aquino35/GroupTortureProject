#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:38:35 2020

@author: osvaldo
"""
from GroupTortureProject.Components.Init import Init


class const(Init):
    """
    This is the constant digital component. This class will take a given
    input an return the same value.
    """
    def __init__(self, name,result):
        super().__init__(name)
        self.result = result