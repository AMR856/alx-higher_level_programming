#!/usr/bin/python3
"""My weird int class"""


class MyInt(int):
    """Here is my class"""
    def __eq__(self, other):
        """The == inverted
        Args: The second number"""
        return super().__ne__(other)

    def __ne__(self, other):
        """The != inverted
        Args: The second number"""
        return super().__eq__(other)
