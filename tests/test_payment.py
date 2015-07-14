"""
@author Lingyan Zhou
"""
import projectkernel
import projectkernel.payment
from projectkernel.payment import Payment 

import unittest
import datetime

class TestPayment(unittest.TestCase):

    def test_id(self):
        p = Payment()
        p.set_id("1")
        self.assertEqual(p.get_id(), "1")
        p.set_id("2")
        self.assertEqual(p.get_id(), "2")

    def test_amount(self):
        p = Payment()
        p.set_amount(1.1)
        self.assertEqual(p.get_amount(), 1.1)
        p.set_amount(2.2)
        self.assertEqual(p.get_amount(), 2.2)

    def test_is_complete(self):
        p= Payment()
        self.assertFalse(p.is_complete())
        p.set_id("1")
        self.assertFalse(p.is_complete())
        p.set_amount(1)
        self.assertTrue(p.is_complete())
