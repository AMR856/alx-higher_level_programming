#!/usr/bin/python3
"""Making my Node class"""


class Node:
    """My Node"""
    def __init__(self, data, next_node=None):
        """The init for my Node
        
        Args:
            data: it's the data to be put in the list
            next_node: The next node
        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """The getter for my data"""
        return self.__data
    
    @data.setter
    def data(self, value):
        """The setter for my data
        
        Args: The value of the data to be put
        """
        if not isinstance(size, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """The getter for the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """The setter for my next_node
        
        Args: The next_node to be put in the list
        """
        if value == None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    def __init__(self):
        self.__head = head
    
    def __str__(self):
        current = self.head
        while (current != None):
            print(current.data)
            current = current.next
