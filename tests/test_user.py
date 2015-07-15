"""
@author Lingyan Zhou
"""
from projectkernel import User 

import unittest
import datetime

class TestUser(unittest.TestCase):

    def test_id(self):
        a = User()
        a.set_id("1")
        self.assertEqual(a.get_id(), "1")
        a.set_id("2")
        self.assertEqual(a.get_id(), "2")

    def test_password(self):
        a = User()
        a.set_password("password1")
        self.assertEqual(a.get_password(), "password1")
        a.set_password("password2")
        self.assertEqual(a.get_password(), "password2")

    def test_is_admin(self):
        a = User()
        a.set_is_admin(True)
        self.assertTrue(a.is_admin())
        a.set_is_admin(False)
        self.assertFalse(a.is_admin())

    def test_name(self):
        a = User()
        a.set_name("name1")
        self.assertEqual(a.get_name(), "name1")
        a.set_name("name2")
        self.assertEqual(a.get_name(), "name2")

    def test_is_complete(self):
        a= User()
        self.assertFalse(a.is_complete())
        a.set_id("1")
        self.assertFalse(a.is_complete())
        a.set_password("password 1")
        self.assertFalse(a.is_complete())
        a.set_is_admin(True)
        self.assertFalse(a.is_complete())
        a.set_name("name 1")
        self.assertTrue(a.is_complete())
