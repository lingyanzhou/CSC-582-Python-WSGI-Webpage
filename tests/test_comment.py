"""
@author Lingyan Zhou
"""
import projectkernel
import projectkernel.comment
from projectkernel.comment import Comment 

import unittest
import datetime

class TestComment(unittest.TestCase):

    def test_user_name(self):
        c = Comment()
        c.set_user_name("Name1")
        self.assertEqual(c.get_user_name(), "Name1")
        c.set_user_name("Name2")
        self.assertEqual(c.get_user_name(), "Name2")

    def test_time(self):
        c = Comment()
        c.set_time(2016, 2, 29, 12)
        self.assertEqual(c.get_time(), datetime.datetime(2016, 2, 29, 12))
        c.set_time_by_str("02/29/16 12:00:00")
        self.assertEqual(c.get_time_as_str(), "02/29/16 12:00:00")
        with self.assertRaises(ValueError):
            c.set_time(2015, 2, 29, 12)
        with self.assertRaises(ValueError):
            c.set_time(2100, 2, 29, 12)

    def test_id(self):
        c = Comment()
        c.set_id("1")
        self.assertEqual(c.get_id(), "1")
        c.set_id("2")
        self.assertEqual(c.get_id(), "2")

    def test_message(self):
        c = Comment()
        c.set_message("message1")
        self.assertEqual(c.get_message(), "message1")
        c.set_message("message2")
        self.assertEqual(c.get_message(), "message2")

    def test_is_complete(self):
        c= Comment()
        self.assertFalse(c.is_complete())
        c.set_id("1")
        self.assertFalse(c.is_complete())
        c.set_time_now()
        self.assertFalse(c.is_complete())
        c.set_user_name("user1")
        self.assertFalse(c.is_complete())
        c.set_message("message 1")
        self.assertTrue(c.is_complete())
