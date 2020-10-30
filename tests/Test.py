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


class Test(TestCase):
    def test_output(self):

        andGate = Gates("AND0", "AND")

        andGate.Output([0, 0])
        self.assertEqual(andGate.result, 0, "The expected result is Zero")

        andGate.Output([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(andGate.result, 0, "The expected result is Zero")

        andGate.Output([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(andGate.result, 1, "The expected result is One")

        orGate = Gates("OR0", "OR")

        orGate.Output([0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1])
        self.assertEqual(orGate.result, 1, "The expected result is One")

        orGate.Output([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(orGate.result, 1, "The expected result is One")

        orGate.Output([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(orGate.result, 0, "The expected result is Zero")

        nandGate = Gates("NAND0", "NAND")
        nandGate.Output([0, 1])
        self.assertEqual(nandGate.result, 1, "The expected result is One")

        norGate = Gates("NOR0", "NOR")
        norGate.Output([1, 1])
        self.assertEqual(norGate.result, 0, "The expected result is Zero")

        xorGate = Gates("XOR0", "XOR")
        xorGate.Output([1, 0])  # the only way we get a one
        self.assertEqual(xorGate.result, 1, "The expected result is One")

        xorGate.Output([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        assert xorGate.result == 0, "The expected result was zero"

        xorGate.Output([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(xorGate.result, 0, "The expected result is Zero")

        xorGate.Output([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
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
        switchObj.Output([1111111, 000000, 0])
        self.assertEqual(switchObj.result, 1111111, "The expected result is 1111111")

        switchObj.Output([101010001, 1101101, 1])
        self.assertEqual(switchObj.result, 1101101, "The expected result is 1101101")

        switchObj.Output([1010010, None, 1])
        self.assertEqual(switchObj.result, 1101101, "The expected result is 1101101")

        switchObj.Output([None, None, 0])
        self.assertEqual(switchObj.result, 1010010, "The expected result is 1010010")

        switchObj.Output([None, None, 0])
        self.assertEqual(switchObj.result, None, "The expected result is 'none''")

        muxObject = Mux("Mux0")  # mux obj
        muxObject.Output([[10101], [1001], [110010], [10001010], 1, 1])
        self.assertEqual(muxObject.result, [10001010], "The expected result is [10001010]")

    def test_operate(self):  # testing the clck obj
        clockObject1 = clock("clck0", 1)
        clockObject1.Output(1)
        self.assertEqual(clockObject1.result, 0, "The expected result is Zero")

    def test_const(self):  # testing const obj
        constantObj = const("cosnt0", 0)
        self.assertEqual(constantObj.result, 0, "The expected result is Zero")
        constantObj = const("cosnt0", 1)
        self.assertEqual(constantObj.result, 1, "The expected result is One")

    def testraise(self):
        # testing switch value error
        with pytest.raises(ValueError):

            andGate = Gates("AND0", "AND")
            self.assertRaises(ValueError, andGate, andGate.Output([1, None])) #testing for none error

            andGate = Gates("OR0", "OR")
            self.assertRaises(ValueError, andGate, andGate.Output([1])) #testing for none error

            nandGate = Gates("NAND0", "NAND")
            self.assertRaises(ValueError, nandGate, nandGate.Output([1, 0, 1, 0])) #testing for size error

            norGate = Gates("NOR0", "NOR")
            self.assertRaises(ValueError, norGate, norGate.Output([1, 1, 1, 1, 1 , 1])) #testing for size error

            # testing for switch errors
            switchObj = switch("Switch0")
            self.assertRaises(ValueError, switchObj, switchObj.Output(
                [10100, 100101, 1566, 10010, 11010, 10101]))  # Assertion error because of three or more inputs

            # #testing Value error
            muxObject = Mux("Mux0")  # mux obj
            self.assertRaises(ValueError, muxObject, muxObject.Output(
                [[1010], [11110111], [1000101], [100010111], 2, 3]))  # Assertion error because of three or more inputs

    def test_Sys(self):  # this test creates a textfile that Simulates the System.

        a = const("Cst1", 0)
        f = Gates("AND1", "AND")
        g = Gates("OR1", "NOR")
        c = clock("clk0", 0)
        i = usr("USR3", [0, 0, 1, 0])
        d = usr("USR1", [0, 1, 0, 1])
        e = Inverter("Inv0")
        b = const("Cst2", 1)
        h = usr("USR2")
        l = const("Cst3", 1)
        j = Mux("Mux0")
        k = Gates("AND2", "AND")
        m = switch("Switch0")
        n = clock("clk1", 1)

        connection_dict = {a: [],
                           b: [],
                           c: [],
                           g: [a, c],
                           l: [],
                           e: [c, a, b],
                           i: [a, c, b, e, a, b, j, n],
                           d: [a, l, c, l, a, a, c, c],
                           e: [],
                           f: [b, c],
                           h: [e, a, c, l, b, c, e, n],
                           j: [d, i, h, e, b, l],
                           k: [j, g],
                           m: [i, d, c]
                           }
        Test_Sys = LogicCircuitSystem(connection_dict, 7)
        print(Test_Sys.network_dict)
