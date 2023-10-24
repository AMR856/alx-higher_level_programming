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
        if not isinstance(value, int) and value is not None:
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
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""Defining My linked list"""


class SinglyLinkedList:
    def __init__(self):
        """The init for my list"""
        self.__head = Node(0, None)

    def __str__(self):
        """This __str__ method that will let me print the
        linked list using print
        """
        current = self.__head.next_node
        linked_list_str = ""
        while current is not None:
            linked_list_str += str(current.data) + "\n"
            current = current.next_node
        return linked_list_str.strip()

    def sorted_insert(self, value):
        """A method to add a node in a sorted linked list

        Args: The value of the added node

        """
        newNode = Node(value)
        current = self.__head
        if current.next_node is None or newNode.data < current.data:
            newNode.next_node = current.next_node
            current.next_node = newNode
        else:
            while current.next_node is not None and \
                    newNode.data > current.next_node.data:
                current = current.next_node
            newNode.next_node = current.next_node
            current.next_node = newNode
