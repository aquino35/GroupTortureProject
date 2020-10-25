#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25  18:50:14 2020

@author: osvaldo
"""
from unittest import TestCase
from GroupTortureProject.Components.Gates import Gates


class TestGates(TestCase):

    def test_output(self):
        andGate = Gates("AND0", "AND")
        andGate.Output([1, 1])
        assert andGate.result == 1
        andGate.Output([1, 0])
        assert andGate.result == 0

        orGate = Gates("OR0", "OR")
        orGate.Output([1, 1])
        assert orGate.result == 1
        orGate.Output([1, 0])
        assert orGate.result == 1
        orGate.Output([0, 0])
        assert orGate.result == 0

        nandGate = Gates("NAND0", "NAND")
        nandGate.Output([1, 1])
        assert nandGate.result == 0
        nandGate.Output([1, 0])
        assert nandGate.result == 1

        norGate = Gates("NOR0", "NOR")
        norGate.Output([1, 1])
        assert norGate.result == 0
        norGate.Output([1, 0])
        assert norGate.result == 0
        norGate.Output([0, 0])
        assert norGate.result == 1

        xorGate = Gates("XOR0", "XOR")
        xorGate.Output([1, 1])
        assert xorGate.result == 0
        xorGate.Output([1, 0])
        assert xorGate.result == 1
        xorGate.Output([0, 0])
        assert xorGate.result == 0
        xorGate.Output([0, 1])
        assert xorGate.result == 1




    # def test_initiate_gate(self):
    #     self.fail()

    # def test_output(self):
    #     self.fail()
