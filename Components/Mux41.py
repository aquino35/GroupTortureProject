# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:58:59 2020

@author: juang
"""
from Components.BaseComponent import BaseComponent


class Mux(BaseComponent):
    """
        Description:
        This the Mux component class of the  digital system.
        Its objective is to return a given output depending on  the giving selection.
        ValueErrors: A MUX Object must have 6 input values and its selection has to be binary
    """

    def __init__(self, name):
        super().__init__(name)
        self.checked = False

    def Output(self, inputs):
        """
        Description:
        From the input, the values from the first postion of the list to the fourth represent the new incoming values.
        While the last two values of the list is used to select which values of the incoming list is the output


        """
        self.checked = False
        self.checkInputErrors(inputs)
        self.inputs = inputs[0:4]
        self.inputs_sec = inputs[4:6]
        # since it will save all he inputs as one, the important thing is to
        # select the values inside depending on the selected input_sec
        # which will simulate as the selection of the multiplexer
        if self.inputs_sec == [0, 0]: self.result = self.inputs[0]
        elif self.inputs_sec == [0, 1]: self.result = self.inputs[1]
        elif self.inputs_sec == [1, 0]: self.result = self.inputs[2]
        elif self.inputs_sec == [1, 1]: self.result = self.inputs[3]
        else: raise ValueError("Selection has to be binary")
        return self.result

    def checkInputErrors(self, inputs):
        if not self.checked:
            length = len(inputs)
            if length < 6 or length > 6:
                raise ValueError("A Mux object must have 6 inputs")
            else:
                self.checked = True
