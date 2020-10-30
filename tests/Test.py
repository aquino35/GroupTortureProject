from unittest import TestCase
from Components.Clock import clock
from Components.Constant import const
from Components.Gates import Gates
from Components.Inverter import Inverter
from Components.Mux41 import Mux
from Components.Switch import switch
from Components.USR import usr
from System.logicCircuitSystem import LogicCircuitSystem

class Test(TestCase):
    def test_output(self):
        andGate = Gates("AND0", "AND")
        andGate.Output([1, 0])
        assert andGate.result == 0 , "The expected result was zero"

        orGate = Gates("OR0", "OR")
        orGate.Output([1, 0])
        assert orGate.result == 1, "The expected result was one"

        nandGate = Gates("NAND0", "NAND")
        nandGate.Output([1, 0])
        assert nandGate.result == 1, "The expected result was one"

        norGate = Gates("NOR0", "NOR")
        norGate.Output([1, 0])
        assert norGate.result == 0 , "The expected result was zero"

        xorGate = Gates("XOR0", "XOR")
        xorGate.Output([0,0])
        assert xorGate.result == 0, "The expected result was zero"

        clck = clock("clck0",1)
        usrObject = usr("usr0",clck,[1,1,1,1]) #usr obj
        print(usrObject.__doc__) #printing USR documentation
        usrObject.Output([1,1])
        print("-------------")
        print("the USR Shift" , usrObject.interior_seq)
        print("The USR result is", usrObject.result)
        print("-------------")
        assert usrObject.result == 1, "The expected result was one"

        muxObject = Mux("Mux0") #mux obj
        muxObject.Output([[10101],[1001],[110010],[10001010],0,1])
        assert muxObject.result == [1001], "The expected result was [10001010]"

    def test_operate(self): #testing the clck obj
        clockObject1 = clock("clck0", 1)
        clockObject1.Output(1)
        assert clockObject1.result == 1, "The expected result was one"

    def test_const(self): #testing const obj
        constantObj = const("cosnt0",231312)
        assert constantObj.result ==231312, "The expected result was zero"

    def test_Sys(self): #this test creates a textfile that Simulates the System.

        w = switch("Switch1") #d: [a, b, b]
        a = const("Const1", 0)
        b = const("Const2", 1)
        c = clock("clk0", 1)
        d = Inverter("Inv0")
        e = usr("USR1",[0, 1, 0, 1])  # Supposed to print whats in the register
        f = usr("USR2", [1,1,1,0])  # Supposed to print whats in the register
        g = Gates("OR1", "OR")
        h = Gates("AND1", "AND")
        i = Mux("Mux1")
        j = Gates("OR2", "OR")
        k = clock("clk1", 1)
        l = usr("USR3", [1, 1, 0, 1])  # Supposed to print whats in the register

        IO_dict = {
                   w: [a, b, b],
                   c: [],
                   l: [d, c, e, b, a, i, e, w],
                   d: [],
                   b: [],
                   e: [d, a, g, b, a, b, w, c],
                   f: [b, c, e , b , a, w, b, c],
                   g: [a, c],
                   h: [d, a],
                   j: [b, h],
                   k: [],
                   a: [],
                   i: [w, h, f, a],
                   }
        Test_Sys = LogicCircuitSystem(IO_dict, 7)
        print(Test_Sys.network_dict)
        #print(d.__doc__)
        # print(Test_Sys.__doc__)
        # print(Test_Sys.traverse.__doc__)
        # print(Test_Sys.organize.__doc__)









