from unittest import TestCase
import pytest
from Components.Clock import clock
from Components.Constant import const
from Components.Gates import Gates
from Components.Inverter import Inverter
from Components.Mux41 import Mux
from Components.Switch import switch
from Components.USR import usr
from System.logicCircuitSystem import LogicCircuitSystem


class Test1(TestCase):
    def test_output(self):
        andGate = Gates("AND0", "AND")

        andGate.Output([1, 1])
        self.assertEqual(andGate.result, 1, "The expected result is One")

        andGate.Output([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(andGate.result, 0, "The expected result is Zero")

        andGate.Output([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(andGate.result, 1, "The expected result is One")

        orGate = Gates("OR0", "OR")

        orGate.Output([1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0])
        self.assertEqual(orGate.result, 1, "The expected result is One")

        orGate.Output([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1])
        self.assertEqual(orGate.result, 1, "The expected result is One")

        orGate.Output([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(orGate.result, 0, "The expected result is Zero")

        nandGate = Gates("NAND0", "NAND")
        nandGate.Output([1, 0])
        self.assertEqual(nandGate.result, 1, "The expected result is One")

        norGate = Gates("NOR0", "NOR")
        norGate.Output([1, 0])
        self.assertEqual(norGate.result, 0, "The expected result is Zero")

        xorGate = Gates("XOR0", "XOR")
        xorGate.Output([0, 1]) # the only way we get a one
        self.assertEqual(xorGate.result, 1, "The expected result is One")

        xorGate.Output([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        assert xorGate.result == 0, "The expected result was zero"
        xorGate.Output([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(xorGate.result, 0, "The expected result is Zero")

        xorGate.Output([1, 1, 1, 1, 1, 1, 1 , 1, 1, 1])
        self.assertEqual(xorGate.result, 0, "The expected result is Zero")

        # clck = clock("clck0", 1)
        # usrObject = usr("usr0", [1, 1, 1, 1])  # usr obj
        # print(usrObject.__doc__)  # printing USR documentation
        # usrObject.Output([1, 1])
        # print("-------------")
        # print("the USR Shift", usrObject.interior_seq)
        # print("The USR result is", usrObject.result)
        # print("-------------")
        # assert usrObject.result == 1, "The expected result was one"

        switchObj = switch("Switch0")
        switchObj.Output([101101110, 1101110000, 0])
        self.assertEqual(switchObj.result, 101101110, "The expected result is 101101110")

        switchObj.Output([10100101011, 1010111100110, 1])
        self.assertEqual(switchObj.result, 1010111100110, "The expected result is 1010111100110")

        switchObj.Output([10110, None , 1])
        self.assertEqual(switchObj.result, 1010111100110, "The expected result is 1010111100110")

        switchObj.Output([None, None , 0])
        self.assertEqual(switchObj.result, 10110, "The expected result is 10110")

        switchObj.Output([None, None , 0])
        self.assertEqual(switchObj.result, None, "The expected result is 'none''")

        muxObject = Mux("Mux0")  # mux obj
        muxObject.Output([[10101], [1001], [110010], [10001010], 0, 1])
        self.assertEqual(muxObject.result, [1001], "The expected result is [1001]")


    def test_operate(self):  # testing the clck obj
        clockObject1 = clock("clck0", 0)
        clockObject1.Output(0)
        self.assertEqual(clockObject1.result, 1, "The expected result is Zero")

    def test_const(self):  # testing const obj
        constantObj = const("cosnt0", 0)
        self.assertEqual(constantObj.result, 0, "The expected result is Zero")

    def testraise(self):

        # testing switch value error
        with pytest.raises(ValueError):

            andGate = Gates("AND0", "AND")
            self.assertRaises(ValueError, andGate, andGate.Output([None, None]))  # testing for none error

            andGate = Gates("OR0", "OR")
            self.assertRaises(ValueError, andGate, andGate.Output([0]))  # testing for none error

            nandGate = Gates("NAND0", "NAND")
            self.assertRaises(ValueError, nandGate, nandGate.Output([1, 0, 1, 0, 1, 0, 1, 0]))  # testing for size error

            norGate = Gates("NOR0", "NOR")
            self.assertRaises(ValueError, norGate, norGate.Output([0, 0, 0, 0, 0, 0, 0, 0, 0]))  # testing for size error

            #testing for switch errors
            switchObj = switch("Switch0")
            self.assertRaises(ValueError, switchObj, switchObj.Output([10145, 461.02, 1566, 1, 1]))# Assertion error because of three or more inputs
            # #testing Value error
            muxObject = Mux("Mux0")  # mux obj
            self.assertRaises(ValueError, muxObject, muxObject.Output([[18465], [18721], [120260], [10451010], 4, 6]))# Assertion error because of three or more inputs


    def test_Sys(self):  # this test creates a textfile that Simulates the System.

        a = const("Cst1", 0)
        f = Gates("AND1", "AND")
        g = Gates("OR1", "OR")
        c = clock("clk0", 0)
        i = usr("USR3", [0, 0, 1, 0])
        d = usr("USR1", [0, 1, 0, 1])
        e = clock("clk1", 0)
        b = const("Cst2", 1)
        h = usr("USR2")
        l = const("Cst3",1)
        j = Mux("Mux0")
        k = Gates("AND2", "AND")
        # k = Gates("OR2", "OR")

        connection_dict = {a: [],
                           b: [],
                           c: [],
                           g: [a, c],
                           i: [a, c, b, e, a, b, j, e],
                           d: [a, l, b, l, a, a, c, c],
                           e: [],
                           f: [b, c],
                           h: [e, a, c, l, b, c, e, e],
                           j: [i, d, h, e, b, l],
                           k: [j, f],
                           l: []}


        Test_Sys = LogicCircuitSystem(connection_dict, 7)
        print(Test_Sys.network_dict)









