# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 23:36:37 2020

@author: juang
"""


class BaseComponent:
    """
        Description:
        The idea of this class is to have a base component so that we can
        use to inheritance to inherit key attributes and functions that go
        inside all the components.
    """
    def __init__(self, name):
        """
            Description:
            :parameter (name) : This helps us identify each instance of the components.
        """
        self.name = name
        self.result = None

    def __repr__(self):
        """
            Description:
            Turns object reference into string name.
            @:return (name) : a string that represents the instance of each component.
        """
        return self.name

    def Output(self, output):
        """
            Description:
            :parameter (output) : A binary number or list that will feed into the System.
            :return (output) : the parameter output.
        """
        output = self.result
        return output

    def output(self):
        """
            Description:
            This function is used to represent the output of each component in the output textfile.
            @:return (output) : result of component.
        """
        output = self.result
        return output

    def checkInputErrors(self, input):
        """
            Description:
            Checks if input value is binary and not any other other number (including none).
            :parameter (input): Value to be checked.
        """
        if not self.checked:
            if not (input == 1 or input == 0) or input == None:
                raise ValueError(f'{self.name} object can only be instantiated with a binary value')
            else:
                self.checked = True




