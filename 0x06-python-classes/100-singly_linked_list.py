#!/usr/bin/python3
"""Singly Linked Lists module.
This module contains methods about the creation and handling of
SinglyLinkedList and Node objects.
"""


class Node:
    """My Node"""
    def __init__(self, data, next_node=None):
        """The init for my Node

        Args:
            data: It's the data to be put in the node
            next_node: The next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """The getter for the data in the node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int) and value is not None:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The getter and setter for the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defining My linked list"""
    def __init__(self):
        """The init for my list"""
        self.__head = None

    def __str__(self):
        """This __str__ method will let me print the linked list using print"""
        current = self.__head
        linked_list_str = ""
        while current is not None:
            linked_list_str += str(current.data) + "\n"
            current = current.next_node
        return linked_list_str.strip()

    def sorted_insert(self, value):
        """A method to add a node in a sorted linked list

        Args:
            value: The value of the added node
        """
        newNode = Node(value)
        if self.__head is None or newNode.data < self.__head.data:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            current = self.__head
            while current.next_node is not None and \
                    newNode.data > current.next_node.data:
                current = current.next_node
            newNode.next_node = current.next_node
            current.next_node = newNode
