# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:15:21 2020

@author: juang
"""
from GroupTortureProject.Components.Init import Init

class switch(Init):

    '''
    This component is a switch were it receives three inputs
    if the component like a switch is open( disconnected) or closed (Connected)
    the last input will help identify if the switch is open or closed
    For the values of input [0,1,2] the input[2] == 1 is open, however if input[2] == 0 is closed.

    If it only receives 1 input making a case of a open-closed, then only 1 output
    is only sent. The one that is closed should deliver the previous value back
    '''

    def __init__(self, name):
        super().__init__(name)
        self.memories = ()
        #self.result =0

    def Output(self, inputs):
        self.input1 = inputs[0]
        self.input2 = inputs[1]
        self.switch_state = inputs[2]
        self.result = self.memories
        self.memories = inputs

        if self.switch_state == 0:
            if self.input1 is None:
                return self.result[0]
            else:
                return self.input1
        elif self.switch_state == 1:
            if self.input2 is None:
                return self.result[1]
            else:
                return self.input2
        else:
            raise Exception("error, inputs are not valued well")

