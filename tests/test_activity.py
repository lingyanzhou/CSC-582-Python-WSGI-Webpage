"""
@author Lingyan Zhou
"""
import projectkernel
import projectkernel.activity
from projectkernel.activity import Activity 

import unittest
import datetime

class TestActivity(unittest.TestCase):

    def test_id(self):
        a = Activity()
        a.set_id("1")
        self.assertEqual(a.get_id(), "1")
        a.set_id("2")
        self.assertEqual(a.get_id(), "2")

    def test_info(self):
        a = Activity()
        a.set_info("info1")
        self.assertEqual(a.get_info(), "info1")
        a.set_info("info2")
        self.assertEqual(a.get_info(), "info2")

    def test_is_complete(self):
        a= Activity()
        self.assertFalse(a.is_complete())
        a.set_id("1")
        self.assertFalse(a.is_complete())
        a.set_info("info 1")
        self.assertTrue(a.is_complete())
