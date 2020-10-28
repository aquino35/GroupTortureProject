# -*- coding: utf-8 -*-

''''
This is a class were it will get the components desired
AND [001]
OR  [011]
XOR [010]
NAND [110]
NOR [100]
With the corresponding values of each one
By using a list we can manipulate the truth talble to our advantge
In this case it will sum the values of the inputs and will give the 
result of the component using the list truth table 
Like for example:
    AND(1,1) === input1 + input2 = 2
    call the list
    AND [0 0 1]
         0 1 2
             ^
    result = 1

    or 

    XOR(1,0) === input1 + input2 = 1
    XOR [0 1 0]
         0 1 2
           ^
    result = 1
'''''
from Components.Init import Init


class Gates(Init):

    def __init__(self, name, gates):
        super().__init__(name)
        self.gates = gates
        self.InitiateGate()

    def Output(self, inputs):
        # This will return the value of the desired component from the inputs placed
        result = Gates.Truth_Table[self.gates][inputs[0] + inputs[1]]
        # For the and, or , xor gates, for more than two inputs, used this lopp to calculate the
        # values
        for increased_num in range(2, len(inputs)):
            result = Gates.Truth_Table[self.gates][result + inputs[increased_num]]
        self.result = result
        return result

    # This will help initiate this class with the corresponding components and
    # Values of the truth table of each one
    @staticmethod
    def InitiateGate():
        if not hasattr(Gates, "initialized"):  # This initialization is only ran once for the class
            Gates.initialized = None
            Gates.Truth_Table = {"AND": [0, 0, 1], "OR": [0, 1, 1], "XOR": [0, 1, 0], "NAND": [1, 1, 0],
                                 "NOR": [1, 0, 0]}

    def output(self):
        final_value = self.result
        return final_value

