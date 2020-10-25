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
        print(usrObject.result)
        assert usrObject.result == 0
