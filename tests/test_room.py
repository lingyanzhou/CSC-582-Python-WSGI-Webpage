"""
@author Lingyan Zhou
"""
import projectkernel
import projectkernel.room
from projectkernel.room import Room 

import unittest
import datetime

class TestRoom(unittest.TestCase):

    def test_id(self):
        r = Room()
        r.set_id("1")
        self.assertEqual(r.get_id(), "1")
        r.set_id("2")
        self.assertEqual(r.get_id(), "2")

    def test_info(self):
        r = Room()
        r.set_info("info1")
        self.assertEqual(r.get_info(), "info1")
        r.set_info("info2")
        self.assertEqual(r.get_info(), "info2")

    def test_name(self):
        r = Room()
        r.set_name("name1")
        self.assertEqual(r.get_name(), "name1")
        r.set_name("name2")
        self.assertEqual(r.get_name(), "name2")

    def test_is_complete(self):
        r= Room()
        self.assertFalse(r.is_complete())
        r.set_id("1")
        self.assertFalse(r.is_complete())
        r.set_name("name 1")
        self.assertFalse(r.is_complete())
        r.set_info("info 1")
        self.assertTrue(r.is_complete())
