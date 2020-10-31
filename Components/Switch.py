# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:15:21 2020

@author: juang
"""
from Components.BaseComponent import BaseComponent

class switch(BaseComponent):

    """
        Description:
        This component is a switch were it receives three inputs
        if the component like a switch is open( disconnected) or closed (Connected)
        the last input will help identify if the switch is open or closed
        For the values of input [0,1,2] the input[2] == 1 is open, however if input[2] == 0 is closed.

        If it only receives 1 input making a case of a open-closed, then only 1 output
        is only sent. The one that is closed should deliver the previous value back.
        ValueErrors: A Switch Object must have at least three inputs.

    """

    def __init__(self, name):
        super().__init__(name)
        self.memories = ()
        self.checked = False

    def Output(self, inputs):
        self.checked = False
        self.checkInputErrors(inputs)
        self.input1 = inputs[0]
        self.input2 = inputs[1]
        self.switch_state = inputs[2]
        self.flashback = self.memories
        self.memories = inputs
        if self.switch_state == 0:
            if self.input1 == None:
                self.result = self.flashback[0]
                return self.flashback[0]
            else:
                self.result = self.input1
                return self.input1
        elif self.switch_state == 1:
            if self.input2 == None:
                self.resut = self.flashback[1]
                return self.flashback[1]
            else:
                self.result = self.input2
                return self.input2
        else:
            raise ValueError("Switch state must be '0' or '1'")

    def checkInputErrors(self, inputs):
        """
            Description:
            Checks if input value is only of three inputs.
            :parameter (inputs): Values to be checked.
        """
        if not self.checked:
            length = len(inputs)
            if length < 3 or length > 3:
                raise Exception("A switch object must have only three inputs")
            else:
                self.checked = True


