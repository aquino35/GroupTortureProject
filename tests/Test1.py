from unittest import TestCase
from Components.Clock import clock
from Components.Constant import const
from Components.Gates import Gates
from Components.Inverter import Inverter
from Components.Mux41 import Mux
from Components.Switch import switch
from Components.USR import usr
from System.logicCircuitSystem import LogicCircuitSystem

class Test1(TestCase):
    """This is the first test script for our Digital System.
    Here we have various test cases for our components and System"""
    def test_output(self):
        andGate = Gates("AND0", "AND")
        andGate.Output([1, 1])
        assert andGate.result == 1 , "The expected result was one"

        orGate = Gates("OR0", "OR")
        orGate.Output([1, 1])
        assert orGate.result == 1, "The expected result was one"

        nandGate = Gates("NAND0", "NAND")
        nandGate.Output([1, 1])
        assert nandGate.result == 0, "The expected result was zero"

        norGate = Gates("NOR0", "NOR")
        norGate.Output([1, 1])
        assert norGate.result == 0 , "The expected result was zero"

        xorGate = Gates("XOR0", "XOR")
        xorGate.Output([1, 1])
        assert xorGate.result == 0, "The expected result was zero"

        # clck = clock("clck0",1)
        # usrObject = usr("usr0",[1,1,1,1]) #usr obj
        # print(usrObject.__doc__) #printing USR documentation
        # usrObject.Output([1,1])
        # print("-------------")
        # print("the USR Shift" , usrObject.interior_seq)
        # print("The USR result is", usrObject.result)
        # print("-------------")
        # assert usrObject.result == 1, "The expected result was one"

        muxObject = Mux("Mux0") #mux obj
        muxObject.Output([[10101],[1001],[110010],[10001010],1,1])
        assert muxObject.result == [10001010], "The expected result was [10001010]"

    def test_operate(self): #testing the clck obj
        clockObject = clock("clck0", 0)
        clockObject.Output(0)
        assert clockObject.result == 1, "The expected result was zero"
        clockObject1 = clock("clck0", 1)
        clockObject1.Output(1)
        assert clockObject1.result == 0, "The expected result was one"

    def test_const(self): #testing const obj
        constantObj = const("cosnt0",133030303)
        assert constantObj.result ==133030303, "The expected result was zero"

    def test_Sys(self):  # this test creates a textfile that Simulates the System.

        a = const("Cnst1", 0)
        b = const("Cnst2", 1)
        c = clock("clk0", 1)
        d = usr("USR1", [0, 0, 0, 0])
        e = usr("USR2", [1, 1, 1, 0])
        f = Gates("AND1", "AND")
        g = Gates("AND2", "AND")
        h = Gates("OR1", "OR")
        i = usr("USR3")
        # j = Mux("Mux0")
        # k = Gates("OR2", "OR")

        connection_dict = {a: [],
                           b: [],
                           c: [],
                           d: [a, b, c, b, a, a, c, c],
                           e: [b, a, c, b, a, b, a, c],
                           f: [b, a],
                           g: [a, b],
                           h: [a, c],
                           i: [a, b, a, b, a, c, b, c]}


        Test_Sys = LogicCircuitSystem(connection_dict, 7)
        print(Test_Sys.network_dict)









