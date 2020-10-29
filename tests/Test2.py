from unittest import TestCase
from GroupTortureProject.Components.Clock import clock
from GroupTortureProject.Components.Constant import const
from GroupTortureProject.Components.Gates import Gates
from GroupTortureProject.Components.Inverter import Inverter
from GroupTortureProject.Components.Mux41 import Mux
from GroupTortureProject.Components.Switch import switch
from GroupTortureProject.Components.USR import usr
from GroupTortureProject.System.logicCircuitSystem import LogicCircuitSystem


class Test2(TestCase):
    def test_output(self):
        andGate = Gates("AND0", "AND")
        andGate.Output([1, 0])
        assert andGate.result == 0, "The expected result was zero"

        orGate = Gates("OR0", "OR")
        orGate.Output([1, 0])
        assert orGate.result == 1, "The expected result was one"

        nandGate = Gates("NAND0", "NAND")
        nandGate.Output([1, 0])
        assert nandGate.result == 1, "The expected result was one"

        norGate = Gates("NOR0", "NOR")
        norGate.Output([1, 0])
        assert norGate.result == 0, "The expected result was zero"

        xorGate = Gates("XOR0", "XOR")
        xorGate.Output([0, 0])
        assert xorGate.result == 0, "The expected result was zero"

        clck = clock("clck0", 1)
        usrObject = usr("usr0", clck, [1, 1, 1, 1])  # usr obj
        print(usrObject.__doc__)  # printing USR documentation
        usrObject.Output([1, 1])
        print("-------------")
        print("the USR Shift", usrObject.interior_seq)
        print("The USR result is", usrObject.result)
        print("-------------")
        assert usrObject.result == 1, "The expected result was one"

        muxObject = Mux("Mux0")  # mux obj
        muxObject.Output([[10101], [1001], [110010], [10001010], 0, 1])
        assert muxObject.result == [1001], "The expected result was [10001010]"

    def test_operate(self):  # testing the clck obj
        clockObject1 = clock("clck0", 1)
        clockObject1.Output(1)
        assert clockObject1.result == 1, "The expected result was one"

    def test_const(self):  # testing const obj
        constantObj = const("cosnt0", 231312)
        assert constantObj.result == 231312, "The expected result was zero"

    def test_Sys(self):  # this test creates a textfile that Simulates the System.

        a = const("Cnst1", 0)
        b = const("Cnst2", 1)
        c = clock("clk0", 1)
        d = usr("USR1", [0, 1, 0, 0])
        e = usr("USR2", [1, 0, 1, 0])
        f = Gates("AND1", "AND")
        g = Gates("AND2", "AND")
        h = Gates("OR1", "OR")
        i = usr("USR3")
        j = Mux("Mux0")

        connection_dict = {a: [],
                           b: [],
                           c: [],
                           d: [a, a, c, b, a, b, a, c],
                           e: [b, c, a, b, a, a, a, c],
                           f: [b, d],
                           g: [c, b],
                           h: [f, g],
                           i: [a, b, c, b, a, h, b, c],
                           j: [c, a, i]}

        Test_Sys = LogicCircuitSystem(connection_dict, 7)
        print(Test_Sys.network_dict)
        # print(d.__doc__)
        # print(Test_Sys.__doc__)
        # print(Test_Sys.traverse.__doc__)
        # print(Test_Sys.organize.__doc__)
