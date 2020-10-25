#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:38:35 2020

@author: osvaldo
"""
from unittest import TestCase
from GroupTortureProject.Components.Mux41 import Mux

#this test case still needs some work

class TestMux(TestCase):
    def test_output(self):
        muxObject = Mux("Mux0")
        muxObject.Output([110110])
        assert muxObject.result == 0
        #print(muxObject.result)



