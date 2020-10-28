#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:50:14 2020

@author: osvaldo
"""

#from Inverter import *
#from usr_prototype import *
# from clock import *
# from digitalSystem import *

#Importing the components of the digital system
from GroupTortureProject.Components.Constant import const
from GroupTortureProject.Components.Clock import clock
from GroupTortureProject.Components.Gates import Gates
from GroupTortureProject.Components.Inverter import Inverter
from GroupTortureProject.Components.Mux41 import Mux
from GroupTortureProject.Components.Switch import switch
from GroupTortureProject.Components.USR import usr

class DigitalSystem():
    """
    This class is defined as Digital System. Its job is to simulate the base that will be used to
    run all of our components and create a network System.
    """

    def __init__(self, layered_comp_list, parent_child_dict, num_of_runs):
        self.network_list = parent_child_dict  # layered component list
        self.IO_dict = layered_comp_list  # parent and child are terms associated with graphs.
        self.run_max = num_of_runs + 1
        self.textFile = open('demo.txt', 'w') # initiating textfile describing the what happens in between runs.
        self.output = []
        self.order = []
        self.visited = {}  # A dictionary that takes note of dig comps visted
        # True -> a node has been visited
        # False -> a node has not been visited
        for dig_comp in self.IO_dict.keys(): # Initiating each dig comp with the attribute visited
            self.visited[dig_comp] = False
        self.organize(self.IO_dict)
        #print(self.order)
        self.Run()

    def organize(self, IO_dict):
        """This function is used to automize the action of traversing a digital component and returning the correct order of dependancies of a directed Graph Network System.
        :parameter
        IO_dict (dictionary): dictionary that has the network of connections
        :return
        list: Containing the order of dependancies of the whole network.
        """
        for dig_comp in IO_dict.keys():
            if not self.visited[dig_comp]:
                self.traverse(dig_comp)
        return self.order

    def traverse(self, dig_comp):
        """This is a helper function used in the Organize function that goes recursively around the structure evaluating the depency of a single digital component.
        :parameter
        dig_comp (component): a component inside the network to be evaluated.
        """
        self.visited[dig_comp] = True  # base case
        for dig_comp_in in self.IO_dict[dig_comp]:  #  We traverse each node inside the connection dictionary that is given
            if not self.visited[dig_comp]:
                self.traverse(dig_comp_in)
        self.order.append(dig_comp)

    def Run(self):
        self.textFile.writelines("------------------------------------------\n")
        self.textFile.writelines("            START OF SIMULATION           \n")
        self.textFile.writelines("------------------------------------------\n")
        self.textFile.writelines("Hello Yousef :'))) \n")
        self.textFile.writelines(f'The order of the following network is:  {self.order} \n')
        self.textFile.writelines("------------------------------------------\n")
        self.textFile.writelines("------------------------------------------\n")
        self.textFile.writelines(f'Run no.{0} \n')
        self.textFile.writelines("------------------------------------------\n")
        run_count = 1
        while run_count != self.run_max:
            self.textFile.writelines("------------------------------------------\n")
            self.textFile.writelines(f'Run no.{run_count} \n')
            self.textFile.writelines("------------------------------------------\n")
            for layer in range(len(self.network_list)):
                for dig_comp in self.network_list[layer]:  # dig_comp = digital component
                    input_list = []
                    for dig_comp_in in self.IO_dict[dig_comp]: # This loops gathers the necessary inputs for the current component
                        if isinstance(dig_comp_in, usr):
                            input_list.append(dig_comp_in.output())
                            self.textFile.writelines(f'{dig_comp_in.name} registers: {dig_comp_in.interior_seq}\n')
                            self.textFile.writelines(f'{dig_comp_in.name} output: {dig_comp_in.output()}\n')
                        else:
                            input_list.append(dig_comp_in.output())
                            self.textFile.writelines(f'{dig_comp_in.name} output: {dig_comp_in.output()}\n')

                        #self.textFile.writelines(f'{dig_comp_in.name} output: {dig_comp_in.result}\n')
                    dig_comp.Output(input_list)
            run_count += 1
            self.textFile.writelines("------------------------------------------\n")
        self.textFile.writelines("------------------------------------------\n")
        self.textFile.writelines("            END OF SIMULATION             \n")
        self.textFile.writelines("------------------------------------------\n")
        self.textFile.close()

#Test_Sys = DigitalSystem(IO_dict, network_list, 2)
# Test_Sys.organize(IO_dict)
# print(Test_Sys.order)
# Test_Sys.Run()

