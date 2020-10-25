#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:38:35 2020

@author: osvaldo
"""

from unittest import TestCase
from GroupTortureProject.Components.clock import clock

class Testclock(TestCase):
    def test_operate(self):
        clockObject = clock("clck0", 0)
        clockObject.Output(0)
        assert clockObject.result == 0
        clockObject1 = clock("clck0", 1)
        clockObject1.Output(1)
        assert clockObject1.result == 1


