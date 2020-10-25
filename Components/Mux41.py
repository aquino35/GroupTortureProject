# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:58:59 2020

@author: juang
"""
from GroupTortureProject.Components.Init import Init


class Mux(Init):

    def __init__(self, name):
        super().__init__(name)
        self.result = 0

    def Output(self, inputs):

        self.inputs = inputs[0:4]
        self.inputs_sec = inputs[4:6]
        self.result = 0
        # since it will save all he inputs as one, the important thing is to
        # select the values inside depending on the selected input_sec
        # which will simulate as the selection of the multiplexer
        if self.inputs_sec == [0, 0]:
            self.result = self.inputs[0]

        elif self.inputs_sec == [0, 1]:
            self.result = self.inputs[1]

        elif self.inputs_sec == [1, 0]:
            self.result = self.inputs[2]

        elif self.inputs_sec == [1, 1]:
            self.result = self.inputs[3]

        return self.result

    def output(self):
        output1 = self.result
        return output1

