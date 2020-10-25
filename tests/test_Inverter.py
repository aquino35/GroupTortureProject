#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25  18:50:14 2020

@author: osvaldo
"""
from unittest import TestCase
from GroupTortureProject.Components.Inverter import Inverter
inverterObject = Inverter("Inverter0")
class TestInverter(TestCase):
    def test_output(self):
        inverterObject.Output(0)
        assert inverterObject.result == 1
        inverterObject.Output(1)
        assert inverterObject.result == 0

