#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:50:14 2020

@author: osvaldo
"""

class LogicCircuitSystem():
    """  This class is defined as The Logic Circuit System Simulator. Its job is to simulate a digital system that runs
    numerous amounts of connected components. The class needs a connection dictionary with the given components
    and the user wants to simulate and the number of runs the user wants it to run. The system will also take the
    connection dictionary and establish a proper order consisting on any dependency the components has.
    """

    def __init__(self, layered_comp_list, num_of_runs):
        """ INIT function: Here the System takes a layered_comp_list and establishes an order
        so then it can run depending on the nums_of_runs and the given order that the system has provided.
        :parameter IO_dict (dictionary): dictionary that has the network of connections
        :parameter num_of_runs (int): number the user wants to run the system
        """
        self.network_dict = layered_comp_list  # Adj list containing connections
        self.run_max = num_of_runs + 1
        self.textFile = open('demo.txt', 'w')  # initiating textfile describing the what happens in between runs.
        self.order = []  # output list containing order of the system
        self.visited = {}  # A dictionary that takes note of dig comps visited
        # True -> a component has been visited
        # False -> a component has not been visited
        for dig_comp in self.network_dict.keys():  # initiating each dig comp with the attribute visited
            self.visited[dig_comp] = False
        self.organize()  # the system organizes itself.
        self.ordered_network_list = self.order
        self.Run()  # run call

    def organize(self):
        """This function is used to automate the action of traversing a digital component and returning the
        correct order of dependencies of a directed Graph Network System.
        :return list: Containing the order of dependencies of the whole network.
        """
        for dig_comp in self.network_dict.keys():
            if not self.visited[dig_comp]:
                self.traverse(dig_comp)
        return self.order

    def traverse(self, dig_comp):
        """This is a helper function used in the Organize function that goes recursively around the
        network structure evaluating the dependencies of a single digital component.
        :parameter dig_comp (component): a component inside the network to be evaluated.
        """
        self.visited[dig_comp] = True  # base case
        for dig_comp_in in self.network_dict[
            dig_comp]:  # We traverse each node inside the connection dictionary that is given
            if not self.visited[dig_comp]:
                self.traverse(dig_comp_in)
        self.order.append(dig_comp)

    def Run(self):
        self.textFile.writelines(
            f'Welcome to the text file of the Digital Circuit System simulator. \n')  # start of text file
        self.textFile.writelines(f'This is a Simulation of {self.run_max - 1} runs of the System.  \n')
        self.textFile.writelines(f'\n')
        self.textFile.writelines(f'The order of the following network is: \n')  # showing order of system in text
        self.textFile.writelines(f'{self.order} \n')
        self.textFile.writelines(f'\n')
        self.textFile.writelines("-----------------------------------------------------------------------\n")
        self.textFile.writelines("                         START OF SIMULATION           \n")
        self.textFile.writelines("-----------------------------------------------------------------------\n")
        self.textFile.writelines(f'Run 0: \n')
        self.textFile.writelines(f'\n')
        for dig_comp in self.ordered_network_list:  # This nested loop gathers all initial values for the text file
            for dig_comp_in in self.network_dict[dig_comp]:
                self.textFile.writelines(f'{dig_comp_in.name} output: {dig_comp_in.output()}\n')
                self.textFile.writelines(f'\n')
        self.textFile.writelines("-----------------------------------------------------------------------\n")
        run_count = 1
        while run_count != self.run_max:
            self.textFile.writelines(f'Run: {run_count} \n')
            self.textFile.writelines(f'\n')
            for dig_comp in self.ordered_network_list:  # dig_comp = digital component
                input_list = []
                for dig_comp_in in self.network_dict[
                    dig_comp]:  # This loops gathers the necessary inputs for the current component
                    input_list.append(dig_comp_in.result)
                    self.textFile.writelines(f'{dig_comp_in.name} output: {dig_comp_in.output()}\n')
                    self.textFile.writelines(f'\n')
                dig_comp.Output(input_list)
            run_count += 1
            self.textFile.writelines("-----------------------------------------------------------------------\n")
        self.textFile.writelines("                         END OF SIMULATION             \n")
        self.textFile.writelines("-----------------------------------------------------------------------\n")
        self.textFile.close()
