"""
@author Lingyan Zhou
"""
from projectkernel import Directions

import unittest

class TestDirections(unittest.TestCase):
    def test_all(self):
        d = Directions()
        d.add_direction("loc 1", "loc 1", "direction 1")
        self.assertEqual("direction 1", d.get_direction("loc 1", "loc 1"))
        d.add_direction("loc 1", "loc 1", "direction 2")
        self.assertEqual("direction 2", d.get_direction("loc 1", "loc 1"))
        d.add_direction("loc 1", "loc 2", "direction 3")
        self.assertEqual("direction 2", d.get_direction("loc 1", "loc 1"))
        self.assertEqual("direction 3", d.get_direction("loc 1", "loc 2"))
        self.assertEqual("No route", d.get_direction("loc 2", "loc 1"))
        self.assertTrue("loc 1" in d.get_locations())
        self.assertTrue("loc 2" in d.get_locations())
        
