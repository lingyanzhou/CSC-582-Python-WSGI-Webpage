"""
@author Lingyan Zhou
"""
from projectkernel import TravelArrangement 

import unittest
import datetime

class TestTravelArrangement(unittest.TestCase):

    def test_id(self):
        p = TravelArrangement()
        p.set_id("1")
        self.assertEqual(p.get_id(), "1")
        p.set_id("2")
        self.assertEqual(p.get_id(), "2")

    def test_name(self):
        p = TravelArrangement()
        p.set_name("name 1")
        self.assertEqual(p.get_name(), "name 1")
        p.set_name("name 2")
        self.assertEqual(p.get_name(), "name 2")

    def test_description(self):
        p = TravelArrangement()
        p.set_description("description 1")
        self.assertEqual(p.get_description(), "description 1")
        p.set_description("description 2")
        self.assertEqual(p.get_description(), "description 2")

    def test_is_complete(self):
        p= TravelArrangement()
        self.assertFalse(p.is_complete())
        p.set_id("1")
        self.assertFalse(p.is_complete())
        p.set_name("1")
        self.assertFalse(p.is_complete())
        p.set_description("1")
        self.assertTrue(p.is_complete())
