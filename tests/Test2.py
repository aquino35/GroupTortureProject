from unittest import TestCase
from Components.Clock import clock
from Components.Constant import const
from Components.Gates import Gates
from Components.Inverter import Inverter
from Components.Mux41 import Mux
from Components.Switch import switch
from Components.USR import usr
from System.logicCircuitSystem import LogicCircuitSystem


class Test2(TestCase):
    def test_output(self):
        andGate = Gates("AND0", "AND")

        andGate.Output([1, 0])
        assert andGate.result == 0, "The expected result was zero"

        andGate.Output([1,1,1,0,1,1,1,1,1,1])
        assert andGate.result == 0, "The expected result was zero"

        andGate.Output([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
        assert andGate.result == 1, "The expected result was zero"

        orGate = Gates("OR0", "OR")

        orGate.Output([1, 0, 1,1,1,1,1,1,1])
        assert orGate.result == 1, "The expected result was one"
        orGate.Output([0,0,0,0,0,0,0,1])
        assert orGate.result == 1, "The expected result was one"

        orGate.Output([0,0,0,0,0,0,0,0])
        assert orGate.result == 0, "The expected result was zero"

        nandGate = Gates("NAND0", "NAND")
        nandGate.Output([1, 0])
        assert nandGate.result == 1, "The expected result was one"

        norGate = Gates("NOR0", "NOR")
        norGate.Output([1, 0])
        assert norGate.result == 0, "The expected result was zero"

        xorGate = Gates("XOR0", "XOR")
        xorGate.Output([0, 1]) #the only way we get a one
        assert xorGate.result == 1, "The expected result was zero"

        xorGate.Output([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        assert xorGate.result == 0, "The expected result was zero"
        xorGate.Output([0,0,0,0,0,0,0,0,0,0])
        assert xorGate.result == 0, "The expected result was zero"

        xorGate.Output([1,1,1,1,1,1,1,1,1,1])
        assert xorGate.result == 0, "The expected result was zero"

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
        switchObj.Output([101, 100, 0])
        assert switchObj.result == 101, "The expected result was 101"

        switchObj.Output([101, 100, 1])
        assert switchObj.result == 100, "The expected result was 100"

        switchObj.Output([101, None , 1])
        assert switchObj.result == 100,"The expected result was 100"

        switchObj.Output([None, None , 0])
        assert switchObj.result == 101,"The expected result was 100"

        switchObj.Output([None, None , 0])
        assert switchObj.result == None,"The expected result was 100"

        # #testing switch assertion error
        # switchObj.Output([100,200,3,0,1])  # Assertion error because of three or more inputs
        # print(switchObj.result)
        # assert switchObj.result == 1,"Expected AssertionError"

        muxObject = Mux("Mux0")  # mux obj
        muxObject.Output([[10101], [1001], [110010], [10001010], 0, 1])
        assert muxObject.result == [1001], "The expected result was [10001010]"

        # #testing assertion error
        # muxObject = Mux("Mux0")  # mux obj
        # muxObject.Output([[10101], [1001], [110010], [10001010], 4, 1])
        # assert muxObject.result == [1001], "The expected result was [10001010]"

    def test_operate(self):  # testing the clck obj
        clockObject1 = clock("clck0", 1)
        clockObject1.Output(1)
        assert clockObject1.result == 0, "The expected result was one"

    def test_const(self):  # testing const obj
        constantObj = const("cosnt0", 1)
        assert constantObj.result == 1, "The expected result was 1"

    def test_Sys(self):  # this test creates a textfile that Simulates the System.

        a = const("Cnst1", 1)
        b = const("Cnst2", 0)
        c = clock("clk0", 1)
        d = usr("USR1", [0, 1, 0, 0])
        e = usr("USR2", [1, 0, 1, 0])
        f = Gates("AND1", "AND")
        g = Gates("AND2", "AND")
        h = Gates("OR1", "OR")
        i = usr("USR3")
        j = Mux("Mux0")
        #k = Gates("OR2", "OR")

        connection_dict = {a: [],
                           b: [],
                           c: [],
                           d: [a, a, b, b, a, b, a, c],
                           e: [b, b, a, b, a, a, a, c],
                           f: [a, a],
                           g: [c, b],
                           h: [f, g],
                           i: [a, b, b, b, a, h, b, c],
                           j: [c, b ,i, g, a, b]}
                          # k:[b,i]}

        Test_Sys = LogicCircuitSystem(connection_dict, 7)
        print(Test_Sys.network_dict)
        # print(d.__doc__)
        # print(Test_Sys.__doc__)
        # print(Test_Sys.traverse.__doc__)
        # print(Test_Sys.organize.__doc__)
