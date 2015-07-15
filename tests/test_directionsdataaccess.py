"""
@author Lingyan Zhou
"""
import configparser
import os
from projectkernel import Directions
from projectkernel import DirectionsDataAccess

import unittest

class TestDirectionsDataAccess(unittest.TestCase):
    def setUp(self):
        conf = configparser.ConfigParser()
        conf["Area 1"] = {}
        conf["Area 1"]["Area 1"] = "You are already here"
        conf["Area 1"]["Area 2"] = "1-2"
        conf["Area 1"]["Area 3"] = "1-3"

        conf["Area 2"] = {}
        conf["Area 2"]["Area 1"] = "2-1"
        conf["Area 2"]["Area 2"] = "You are already here"
        conf["Area 2"]["Area 3"] = "2-3"

        conf["Area 3"] = {}
        conf["Area 3"]["Area 1"] = "3-1"
        conf["Area 3"]["Area 2"] = "3-2"
        conf["Area 3"]["Area 3"] = "You are already here"

        with open("test.ini", "wt") as f:
            conf.write(f)

    def tearDown(self):
        os.remove("test.ini")

    def test_all(self):
        dda = DirectionsDataAccess("test.ini")
        dda.load()
        d = dda.get()
        self.assertTrue("Area 1" in d.get_locations())
        self.assertTrue("Area 2" in d.get_locations())
        self.assertTrue("Area 3" in d.get_locations())
        self.assertEqual("You are already here", d.get_direction("Area 1", "Area 1"))
        self.assertEqual("1-2", d.get_direction("Area 1", "Area 2"))
        self.assertEqual("1-3", d.get_direction("Area 1", "Area 3"))
        self.assertEqual("2-1", d.get_direction("Area 2", "Area 1"))
        self.assertEqual("You are already here", d.get_direction("Area 2", "Area 2"))
        self.assertEqual("2-3", d.get_direction("Area 2", "Area 3"))
        self.assertEqual("3-1", d.get_direction("Area 3", "Area 1"))
        self.assertEqual("3-2", d.get_direction("Area 3", "Area 2"))
        self.assertEqual("You are already here", d.get_direction("Area 3", "Area 3"))
