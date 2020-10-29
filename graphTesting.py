#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:00:33 2020

@author: osvaldo
"""

# connection_dict = {a:[],b:[],c:[],d:[a,b,c,b,a],e:[b,a,c,b,a],f:[b,d],g:[e,b],h:[f,g],i:[a,b,c,b,a,h]}

connection_dict = {"a": [],
                   "d": ["a", "b", "c", "b", "a"],
                   "c": [],
                   "i": ["a", "b", "c", "b", "a", "h"],
                   "e": ["b", "a", "c", "b", "a"],
                   "f": ["b", "d"], "g": ["e", "b"],
                   "h": ["f", "g"],
                   "b": []
                   }

"""
connection_dict = {
        "A" : ["B","C"],
        "B" : ["D","E"],
        "C" : ["B", "F"],
        "D" : [],
        "E" : ["F"],
        "F" : [],
        }
"""

"""
connection_dict = {
        "1":["2","3","4"],
        "2":["6"],
        "3":["5","6"],
        "4":["5"],
        "5":["6","7"],
        "6":["7"],
        "7":[],
        }
"""

"""
connection_dict = {
        "1":[],
        "2":["1"],
        "3":["1"],
        "4":["1"],
        "5":["3","4"],
        "6":["2","3","5"],
        "7":["5","6"],
        }
"""

"""this should be in the initialize method"""
visited = {}  # A dictionary that takes note of nodes visted
# True -> a node has been visited
# False -> a node has not been visited

output = []

order = []
# records the order of the network layer

# the following loop is made to assign attributes to the nodes
for i in connection_dict.keys():
    visited[i] = False
    # We assign to every node False meaning its not visited


# print(visited)


def organize(connection_dict):
    for node in connection_dict.keys():
        if not visited[node]:
            traverse(node)
    return order


def traverse(randomNode):
    # base case:
    visited[randomNode] = True
    for node in connection_dict[randomNode]:
        if not visited[node]:
            traverse(node)
    order.append(randomNode)


print(organize(connection_dict))
"""
#THIS ONE RUNS CORRECTLY 

def Organize(randomNode):
    #base case:
    visited[randomNode] = True 
    #output.append(randomNode)

    for node in connection_dict[randomNode]:
        if not visited[node]:
            Organize(node)
    order.append(randomNode)        




 gr
Organize("7")
print(order)
#print(output)





    def organize(self,IO_dict):
        for node in IO_dict.keys():
            if not self.visited[node]:
                self.traverse(node)
        return self.order        

    def traverse(self,randomNode):
        self.visited[randomNode] = True 
        #base case
        for node in self.IO_dict[randomNode]:
            #We traverse each node inside the connection dictionary
            #that is given 
            if not self.visited[node]:
                self.traverse(node)
        self.order.append(randomNode)











"""