# -*- coding: utf-8 -*-
from Components.BaseComponent import BaseComponent
class Gates(BaseComponent):
    """
        Description:
        This is the digital gate class component of the digital system.
        Its job simulate the components:
                        AND [001]
                        OR  [011]
                        XOR [010]
                        NAND [110]
                        NOR [100]
        With the corresponding values of each one
        By using a list we can manipulate the truth table to our advantage
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
        ValueErrors || Exceptions: A Gate Object cannot have none values in the output. Also all Gate must have more
        than one binary input and more specifically 'NAND' and 'NOR' Gates must have exactly two binary inputs.
    """

    def __init__(self, name, gates):
        super().__init__(name)
        self.checked = False
        self.gates = gates
        #self.checkInputErrors(gates)
        self.InitiateGate()

    def Output(self, inputs):

        #if not self.result == None:
        self.checked = False
        self.checkInputErrors(inputs)
        # This will return the value of the desired component from the inputs placed
        result = Gates.Truth_Table[self.gates][inputs[0] + inputs[1]]
        # For the and, or , xor gates, for more than two inputs, used this lopp to calculate the
        # values
        for increased_num in range(2, len(inputs)):
            result = Gates.Truth_Table[self.gates][result + inputs[increased_num]]
        self.result = result
        return result

    def checkInputErrors(self, inputs):

        if not self.checked:
            # Checks once if the gate has the correct amount of inputs
            inputSet = set(inputs)
            if None in inputSet:
                raise ValueError("A Gate object cannot have 'None' input values")
            # elif not (1 or 0) in inputSet:
            #     print(inputs)
            #     raise ValueError("A Gate object must only have binary values")
            # elif not (1 or 0) in inputSet:
            #     raise ValueError("sdfdfd")
            length = len(inputs)
            if length == 1:
                raise Exception("A Gate object must have 2 or more inputs")
            elif length > 2 and self.gates in ["NAND", "NOR"]:
                raise Exception(f'"{self.name}", which is a {self.gates} gate, cannot receive more than two inputs.')
            else:
                self.checked = True

    # This will help initiate this class with the corresponding components and
    # Values of the truth table of each one
    @staticmethod
    def InitiateGate():
        if not hasattr(Gates, "initialized"):  # This initialization is only ran once for the class
            Gates.initialized = None
            Gates.Truth_Table = {"AND": [0, 0, 1], "OR": [0, 1, 1], "XOR": [0, 1, 0], "NAND": [1, 1, 0],
                                 "NOR": [1, 0, 0]}

    def output(self):
        return self.result