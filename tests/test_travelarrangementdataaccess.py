"""
@author Lingyan Zhou
"""
import projectkernel
import projectkernel.travelarrangement
from projectkernel.travelarrangement import TravelArrangement
import projectkernel.travelarrangementdataaccess
from projectkernel.travelarrangementdataaccess import TravelArrangementDataAccess

import os
import configparser
import unittest

class TestTravelArrangementDataAccess(unittest.TestCase):
    def setUp(self):
        conf = configparser.ConfigParser()
        conf["id1"] = {}
        conf["id1"]["name"] = "name 1"
        conf["id1"]["description"] = "desc 1"
        conf["id2"] = {}
        conf["id2"]["name"] = "name 2"
        conf["id2"]["description"] = "desc 2"
        conf["id3"] = {}
        conf["id3"]["name"] = "name 3"
        conf["id3"]["description"] = "desc 3"

        with open("test.ini", "wt") as f:
            conf.write(f)

    def tearDown(self):
        os.remove("test.ini")

    def test_load(self):
        tda = TravelArrangementDataAccess("test.ini")
        tda.load()
        rlist = tda.list_all()
        
        self.assertEqual(len(rlist), 3)

        a = rlist[0]
        self.assertEqual(a.get_id(), "id1")
        self.assertEqual(a.get_name(), "name 1")
        self.assertEqual(a.get_description(), "desc 1")


        a = rlist[1]
        self.assertEqual(a.get_id(), "id2")
        self.assertEqual(a.get_name(), "name 2")
        self.assertEqual(a.get_description(), "desc 2")


        a = rlist[2]
        self.assertEqual(a.get_id(), "id3")
        self.assertEqual(a.get_name(), "name 3")
        self.assertEqual(a.get_description(), "desc 3")


    def test_add_save(self):
        ada = TravelArrangementDataAccess("test.ini")
        r = TravelArrangement()
        r.set_id("id3")
        r.set_name("name 3")
        r.set_description("desc 3")

        self.assertTrue(ada.add(r))
        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "name = name 3\n")
            self.assertEqual(f.readline(), "description = desc 3\n")

    def test_add_autoid(self):
        ada = TravelArrangementDataAccess("test.ini")
        ada.load()
        r = TravelArrangement()
        r.set_id("id3")
        r.set_name("name 3")
        r.set_description("desc 3")

        self.assertTrue(ada.add(r))
        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "name = name 1\n")
            self.assertEqual(f.readline(), "description = desc 1\n")


            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "name = name 2\n")
            self.assertEqual(f.readline(), "description = desc 2\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "name = name 3\n")
            self.assertEqual(f.readline(), "description = desc 3\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[0]\n")
            self.assertEqual(f.readline(), "name = name 3\n")
            self.assertEqual(f.readline(), "description = desc 3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_add_then_list(self):
        ada = TravelArrangementDataAccess("test.ini")
        ada.load()
        a = TravelArrangement()
        a.set_id("id4")
        a.set_name("name 4")
        a.set_description("desc 4")
        self.assertTrue(ada.add(a))

        allCmt = ada.list_all()
        self.assertEqual(len(allCmt), 4)
        
        lastCmt = allCmt[3]
        self.assertFalse(lastCmt is a)

        self.assertEqual(lastCmt.get_id(), "id4")
        self.assertEqual(lastCmt.get_name(), "name 4")
        self.assertEqual(lastCmt.get_description(), "desc 4")


    def test_delete_then_list(self):
        ada = TravelArrangementDataAccess("test.ini")
        ada.load()
        ada.delete_by_id("id1")

        allCmt = ada.list_all()
        self.assertEqual(len(allCmt), 2)
        
        a = allCmt[0]
        self.assertEqual(a.get_id(), "id2")
        self.assertEqual(a.get_name(), "name 2")
        self.assertEqual(a.get_description(), "desc 2")


        a = allCmt[1]
        self.assertEqual(a.get_id(), "id3")
        self.assertEqual(a.get_name(), "name 3")
        self.assertEqual(a.get_description(), "desc 3")
        
    def test_delete_then_save(self):
        ada = TravelArrangementDataAccess("test.ini")
        ada.load()
        ada.delete_by_id("id1")

        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "name = name 2\n")
            self.assertEqual(f.readline(), "description = desc 2\n")


            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "name = name 3\n")
            self.assertEqual(f.readline(), "description = desc 3\n")


            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_update_then_list(self):
        ada = TravelArrangementDataAccess("test.ini")
        ada.load()
        a = TravelArrangement()
        a.set_id("id1")
        a.set_name("name 1.1")
        a.set_description("desc 1.1")

        self.assertTrue(ada.update(a))
        tlist = ada.list_all()
        
        self.assertEqual(len(tlist), 3)

        a = tlist[0]
        self.assertEqual(a.get_id(), "id1")
        self.assertEqual(a.get_name(), "name 1.1")
        self.assertEqual(a.get_description(), "desc 1.1")

        a = tlist[1]
        self.assertEqual(a.get_id(), "id2")
        self.assertEqual(a.get_name(), "name 2")
        self.assertEqual(a.get_description(), "desc 2")

        a = tlist[2]
        self.assertEqual(a.get_id(), "id3")
        self.assertEqual(a.get_name(), "name 3")
        self.assertEqual(a.get_description(), "desc 3")

    def test_update_then_save(self):
        ada = TravelArrangementDataAccess("test.ini")
        ada.load()
        a = TravelArrangement()
        a.set_id("id1")
        a.set_name("name 1.1")
        a.set_description("description 1.1")
        self.assertTrue(ada.update(a))
        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "name = name 1.1\n")
            self.assertEqual(f.readline(), "description = description 1.1\n")


            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "name = name 2\n")
            self.assertEqual(f.readline(), "description = desc 2\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "name = name 3\n")
            self.assertEqual(f.readline(), "description = desc 3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

