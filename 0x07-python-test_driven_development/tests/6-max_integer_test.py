#!/bin/usr/python3
import unittest
"""My testing module"""

max_integer = __import__('6-max_integer').max_integer

class TestMax(unittest.TestCase):
    """A class to test some stuff"""
    def test_normal(self):
        """Testing normal condition"""
        myList = [1 , 2, 3, 4, 5]
        self.assertEqual(max_integer(myList), 5, "The Max is wrong")
    
    def test_beg(self):
        """Testing max beg"""
        myList = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(myList), 5, "The Max is wrong")
    
    def test_mid(self):
        """Testing max mid"""
        myList = [3, 4, 5, 2, 1]
        self.assertEqual(max_integer(myList), 5, "The Max is wrong")

    def test_empty(self):
        """Testing empty list condition"""
        myList =[]
        self.assertEqual(max_integer(myList), None, "It should be none")

    def test_allNegative(self):
        """Testing all negative lists"""
        myList = [-1, -2, -3, -4, -5]
        self.assertEqual(max(myList), -1, "The max is wrong")
    
    def test_weirdCombination(self):
        """Testing negative and positive values"""
        myList = [1, -2, 3, -4, 5]
        self.assertEqual(max_integer(myList), 5, "The max is wrong")
    
    def test_withZero(self):
        """Testing and the biggest is zero"""
        myList = [-1, -2, -3, -5, 0]
        self.assertEqual(max_integer(myList), 0, "The max is wrong")
    
    def test_string(self):
        """"Testing with string"""
        myString = "Hi I'm Amr"
        self.assertEqual(max_integer(myString), 'r', "The max is wrong")
    
    def test_float(self):
        """"Testing with float values"""
        myList = [1.04, -30.5, -25.8, 20.9]
        self.assertEqual(max_integer(myList), 20.9, "The max is wrong")
    
    def test_oneValue(self):
        """Testing with one value list"""
        myList = [8]
        self.assertEqual(max_integer(myList), 8, "The max is wrong")
        
if __name__ == '__main__':
    unittest.main()
