#!/usr/bin/python3
"""Test file for base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.Testcase):
    """Test creation of a base instance"""
    def test_no_id(self):
        x = Base()
        y = Base()
        self.assertEqual(y.id, x.id + 1)
