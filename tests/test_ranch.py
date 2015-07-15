"""
@author Lingyan Zhou
"""
from projectkernel import Ranch 

import unittest
import datetime

class TestRanch(unittest.TestCase):
    def test_name(self):
        a = Ranch()
        a.set_name("name1")
        self.assertEqual(a.get_name(), "name1")
        a.set_name("name2")
        self.assertEqual(a.get_name(), "name2")

    def test_location(self):
        a = Ranch()
        a.set_location("loc1")
        self.assertEqual(a.get_location(), "loc1")
        a.set_location("loc2")
        self.assertEqual(a.get_location(), "loc2")

    def test_description(self):
        a = Ranch()
        a.set_description("description1")
        self.assertEqual(a.get_description(), "description1")
        a.set_description("description2")
        self.assertEqual(a.get_description(), "description2")

    def test_is_complete(self):
        a= Ranch()
        self.assertFalse(a.is_complete())
        a.set_name("name1")
        self.assertFalse(a.is_complete())
        a.set_location("location1")
        self.assertFalse(a.is_complete())
        a.set_description("description1")
        self.assertTrue(a.is_complete())
