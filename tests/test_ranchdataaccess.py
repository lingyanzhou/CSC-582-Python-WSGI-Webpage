"""
@author Lingyan Zhou
"""
import projectkernel
import projectkernel.ranch
from projectkernel.ranch import Ranch
import projectkernel.ranchdataaccess
from projectkernel.ranchdataaccess import RanchDataAccess

import os
import configparser
import unittest

class TestRanchDataAccess(unittest.TestCase):
    def setUp(self):
        conf = configparser.ConfigParser()
        conf["Ranch"] = {}
        conf["Ranch"]["name"] = "ranch name"
        conf["Ranch"]["location"] = "ranch location"
        conf["Ranch"]["description"] = "ranch description"

        with open("test.ini", "wt") as f:
            conf.write(f)

    def tearDown(self):
        os.remove("test.ini")

    def test_load(self):
        rda = RanchDataAccess("test.ini")
        rda.load()
        r = rda.get()
        
        self.assertTrue(r!= None)

        self.assertEqual(r.get_name(), "ranch name")
        self.assertEqual(r.get_location(), "ranch location")
        self.assertEqual(r.get_description(), "ranch description")

    def test_update(self):
        rda = RanchDataAccess("test.ini")
        rda.load()
        r = Ranch()
        r.set_name("ranch name 2")
        r.set_location("ranch location 2")
        r.set_description("ranch description 2")
        rda.update(r)
        
        r = rda.get()
        self.assertTrue(r!=None)

        self.assertEqual(r.get_name(), "ranch name 2")
        self.assertEqual(r.get_location(), "ranch location 2")
        self.assertEqual(r.get_description(), "ranch description 2")
                    
    def test_update_then_save(self):
        rda = RanchDataAccess("test.ini")
        rda.load()
        r = Ranch()
        r.set_name("ranch name 2")
        r.set_location("ranch location 2")
        r.set_description("ranch description 2")
        rda.update(r)
        rda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[Ranch]\n")
            self.assertEqual(f.readline(), "name = ranch name 2\n")
            self.assertEqual(f.readline(), "location = ranch location 2\n")
            self.assertEqual(f.readline(), "description = ranch description 2\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

