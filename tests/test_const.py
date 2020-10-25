#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:38:35 2020

@author: osvaldo
"""
from unittest import TestCase
from GroupTortureProject.Components.const import const

class Test(TestCase):
    def test_const(self):
        constantObj = const("cosnt0",0)
        constantObj1 = const("cosnt0",1)
        assert constantObj.result ==0
        assert constantObj1.result ==1
