#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:38:35 2020

@author: osvaldo
"""
from unittest import TestCase
from GroupTortureProject.Components.clock import clock
from GroupTortureProject.Components.USR import usr

#this tester still needs some work
class Testusr(TestCase):

    def test_output(self):
        clck = clock("clck0",1)
        usrObject = usr("usr0",clck,[1,1,1,1])
        print(usrObject.__doc__) #printing USR documentation
        usrObject.Output([1,1])
        print("-------------")
        print("the USR Shift" , usrObject.interior_seq)
        print("The USR result is", usrObject.result)
        print("-------------")
        assert usrObject.result == 1

        usrObject1 = usr("usr1",clck,[0,0,0,0])
        usrObject1.Output([1,0])
        print("-------------")
        print("the USR Shift" , usrObject1.interior_seq)
        print("The USR result is", usrObject1.result)
        print("-------------")
        assert usrObject1.result == 0

        usrObject2 = usr("usr2",clck,[1,0,0,0])
        usrObject2.Output([1,1])
        print("-------------")
        print("the USR Shift" , usrObject2.interior_seq)
        print("The USR result is", usrObject2.result)
        print("-------------")
        assert usrObject2.result == 1

        # # testing illegal exception in usr exception
        # usrObject2 = usr("usr1",clck,[0,0,0,0])
        # usrObject2.Output([1,3])
        # print("the USR Shift" , usrObject2.interior_seq)
        # print("The USR result is ", usrObject2.result)
        # print("-------------")
        # assert usrObject1.result == 0
