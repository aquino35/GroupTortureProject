from unittest import TestCase
from GroupTortureProject.Components.Clock import clock
from GroupTortureProject.Components.Constant import const
from GroupTortureProject.Components.Gates import Gates
from GroupTortureProject.Components.Inverter import Inverter
from GroupTortureProject.Components.Mux41 import Mux
from GroupTortureProject.Components.Switch import switch
from GroupTortureProject.Components.USR import usr
from GroupTortureProject.System.digitalSystem import DigitalSystem

class Test1(TestCase):
    def test_something(self):
        self.assertEqual(True, False)

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
        muxObject.Output([[10101],[1001],[110010],[10001010],1,1])
        assert muxObject.result == [10001010], "The expected result was [10001010]"

    def test_operate(self): #testing the clck obj
        clockObject = clock("clck0", 0)
        clockObject.Output(0)
        assert clockObject.result == 0, "The expected result was zero"
        clockObject1 = clock("clck0", 1)
        clockObject1.Output(1)
        assert clockObject1.result == 1, "The expected result was one"

    def test_const(self): #testing const obj
        constantObj = const("cosnt0",133030303)
        assert constantObj.result ==133030303, "The expected result was zero"

    def test_Sys(self):
        w = clock("clk0", 1)
        a = const("Const1", 1)
        b = const("Const2", 1)
        c = Inverter("Inverter1")
        #d = switch("Switch1") #d: [a, b, b]
        e = Gates("AND1", "AND")  # Constant output object
        f = Gates("AND2", "AND")
        g = Gates("OR1", "OR")
        h = Gates("OR2", "OR")
        i = Mux("Mux1")
        j = Gates("OR3", "OR")
        k = clock("clk1", 1)
        l = usr("USR1", k.result, [1, 1, 0, 1])  # Supposed to print whats in the register
        m = Gates("NOR", "NOR")
        IO_dict = {w: [],
                   a: [],
                   b: [],
                   c: [a],
                   e: [w, a],
                   f: [b, c],
                   g: [a, f],
                   h: [e, g],
                   i: [g, h, b],
                   j: [i, h],
                   k: [], l: [e, b],
                   m: [l, w]}
        Test_Sys = DigitalSystem(IO_dict, 7)
        #print(d.__doc__)
        # print(Test_Sys.__doc__)
        # print(Test_Sys.traverse.__doc__)
        # print(Test_Sys.organize.__doc__)










