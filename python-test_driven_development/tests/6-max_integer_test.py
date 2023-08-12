#!/usr/bin/python3
"""_summary_
unittests for the function def max_integer(list=[]):
"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """_summary_
    This Class tests a function max_integer in 6-max_integer.py
    """

    @classmethod
    def setUpClass(cls):
        print("Starting Tests for 6-max_integer.py ....")

    def test_max_at_the_end(self):
        """Test the func result for a list with its max at the end"""
        self.assertEqual(max_integer([2, 3, 5, 10]), 10)

    def test_max_at_the_beginning(self):
        """Test the func result for a list with its max at the beginning"""
        self.assertEqual(max_integer([20, 18, 2, 1, 4]), 20)

    def test_max_in_the_middle(self):
        """Test the func result for a list with its max in the middle"""
        self.assertEqual(max_integer([2, 4, 10, 6, 8]), 10)

    def test_one_negative_number_in_the_list(self):
        """Test the func result for a list with one negative number"""
        self.assertEqual(max_integer([1, 2, -1, 4, 5]), 5)

    def test_only_negative_numbers_in_the_list(self):
        """Test the func result for a list with only negative numbers"""
        self.assertEqual(max_integer([-2, -4, -6, -8, -10]), -2)

    def test_list_of_one_element(self):
        """Test the func result for a list with only one element"""
        self.assertEqual(max_integer([20]), 20)

    def test_empty_list(self):
        """Test the func result for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_strings(self):
        """Test the func result for a string"""
        self.assertEqual(max_integer("AfricanLeadershipUniversity"), "y")

    def test_list_of_strings(self):
        """Test the func result for a list with strings"""
        strings = ["google", "microsoft", "neuralink", "apple", "amazon"]
        self.assertEqual(max_integer(strings), "neuralink")

    def test_empty_string(self):
        """Test the func result for an empty string"""
        self.assertEqual(max_integer(""), None)

    @classmethod
    def tearDownClass(cls):
        print("Completed tests for 6-max_integer.py !!!!!")
