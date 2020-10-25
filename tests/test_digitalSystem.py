#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24  18:50:14 2020

@author: osvaldo
"""


from unittest import TestCase

#from Inverter import *
#from usr_prototype import *
# from clock import *
# from digitalSystem import *
from GroupTortureProject.Components.const import const
from GroupTortureProject.Components.clock import clock
from GroupTortureProject.Components.Gates import Gates
from GroupTortureProject.Components.Inverter import Inverter
from GroupTortureProject.Components.Mux41 import Mux
from GroupTortureProject.Components.Switch import switch
from GroupTortureProject.Components.USR import usr
from GroupTortureProject.System.digitalSystem import DigitalSystem

w = clock("clk0", 1)
a = const("Const1", 1)
b = const("Const2", 1)
c = Inverter("Inverter1")
d = switch("Switch1")
e = Gates("AND1", "AND")  # Constant output object
f = Gates("AND2", "AND")
g = Gates("OR1", "OR")
h = Gates("OR2", "OR")
i = Mux("Mux1")
j = Gates("OR3", "OR")
k = clock("clk1", 1)
l = usr("USR1",k.result,[1,1,1,1]) #Supposed to print whats in the register

IO_dict = { w:[],a:[],b:[],c: [a], e:[w, a], f:[b, c],
           g:[a,f],h:[e,g],i:[g,h,b],j:[i,h], d:[a,b,b], k:[] , l:[f,a]}

network_list = [[w],[a],[b],[c],[d],[e],[f],[g],[h],[i],[j],[k],[l]]  # Each component of the list represents a layer with the components that are inside of that layer.


#IO_dict = {a: [], b: [], c: [a, b], d: [a, a], e: [c, d], f: [e, c]}


IO_test = {"a":[],"b":[],"c":[],"d":["a","b","c","b","a"],"e":["b","a","c","b","a"],
 "f":["b","d"],"g":["e","b"],"h":["f","g"],"i":["a","b","c","b","a","h"]}


class TestDigitalSystem(TestCase):
    def test_organize(self):
        Test_Sys = DigitalSystem(IO_dict,network_list, 7)
        Test_Sys.organize(IO_dict)
        print(Test_Sys.order)

        #print(d.__doc__)
        print(Test_Sys.__doc__)
        print(Test_Sys.traverse.__doc__)
        print(Test_Sys.organize.__doc__)

        #assert Test_Sys.order == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']



        # assert Test_Sys.order == [Const1,Const2,AND1,AND2,OR1,OR2]
        # assert Test_Sys.order == [<GroupTortureProject.Components.const.const object at 0x10626adf0>, <GroupTortureProject.Components.const.const object at 0x106275040>,
        # <GroupTortureProject.Components.Gates.Gates object at 0x106275190>, <GroupTortureProject.Components.Gates.Gates object at 0x106275ee0>
        # , <GroupTortureProject.Components.Gates.Gates object at 0x106275f40>, <GroupTortureProject.Components.Gates.Gates object at 0x106275700>]
        # assert Test_Sys.order == [a.name,b.name,c.name,d.name,e.name,f.name]



