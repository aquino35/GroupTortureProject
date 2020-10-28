#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:38:35 2020

@author: osvaldo
"""
from unittest import TestCase
from GroupTortureProject.Components.Mux41 import Mux



class TestMux(TestCase):
    def test_output(self):
        muxObject = Mux("Mux0")
        muxObject.Output([1,1,0,1,1,0])
        assert muxObject.result == 0

        muxObject1 = Mux("Mux1")
        muxObject1.Output([1,1,0,1,0,1])
        print( "the mux1 result is" ,muxObject1.result)
        assert muxObject1.result == 1

        muxObject2 = Mux("Mux2")
        muxObject2.Output([1,1,1,1,1,1])
        print( "the mux2 result is" , muxObject2.result)
        assert muxObject2.result == 1

        muxObject2 = Mux("Mux2")
        muxObject2.Output([0,0,1,1,0,0])
        print( "the mux2 result is" , muxObject2.result)
        assert muxObject2.result == 0
        #print(muxObject.result)



