"""
@author Lingyan Zhou
"""
import projectkernel
import projectkernel.activity
from projectkernel.activity import Activity
import projectkernel.activitydataaccess
from projectkernel.activitydataaccess import ActivityDataAccess

import os
import configparser
import unittest

class TestActivityDataAccess(unittest.TestCase):
    def setUp(self):
        conf = configparser.ConfigParser()
        conf["id1"] = {}
        conf["id1"]["info"] = "info1"

        conf["id2"] = {}
        conf["id2"]["info"] = "info2"
        
        conf["id3"] = {}
        conf["id3"]["info"] = "info3"

        with open("test.ini", "wt") as f:
            conf.write(f)

    def tearDown(self):
        os.remove("test.ini")

    def test_load(self):
        ada = ActivityDataAccess("test.ini")
        ada.load()
        rlist = ada.list_all_activities()
        
        self.assertEqual(len(rlist), 3)

        a = rlist[0]
        self.assertEqual(a.get_id(), "id1")
        self.assertEqual(a.get_info(), "info1")

        a = rlist[1]
        self.assertEqual(a.get_id(), "id2")
        self.assertEqual(a.get_info(), "info2")

        a = rlist[2]
        self.assertEqual(a.get_id(), "id3")
        self.assertEqual(a.get_info(), "info3")

    def test_add_save(self):
        ada = ActivityDataAccess("test.ini")
        r = Activity()
        r.set_id("id3")
        r.set_info("info3")
        self.assertTrue(ada.add_activity(r))
        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "info = info3\n")

    def test_add_autoid(self):
        ada = ActivityDataAccess("test.ini")
        ada.load()
        r = Activity()
        r.set_id("id3")
        r.set_info("info3")
        self.assertTrue(ada.add_activity(r))
        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "info = info1\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "info = info2\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "info = info3\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[0]\n")
            self.assertEqual(f.readline(), "info = info3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_add_then_list(self):
        ada = ActivityDataAccess("test.ini")
        ada.load()
        a = Activity()
        a.set_id("id4")
        a.set_info("info3")
        self.assertTrue(ada.add_activity(a))

        allCmt = ada.list_all_activities()
        self.assertEqual(len(allCmt), 4)
        
        lastCmt = allCmt[3]
        self.assertFalse(lastCmt is a)

        self.assertEqual(lastCmt.get_id(), "id4")
        self.assertEqual(lastCmt.get_info(), "info3")

    def test_delete_then_list(self):
        ada = ActivityDataAccess("test.ini")
        ada.load()
        ada.delete_activity_by_id("id1")

        allCmt = ada.list_all_activities()
        self.assertEqual(len(allCmt), 2)
        
        self.assertEqual(allCmt[0].get_id(), "id2")
        self.assertEqual(allCmt[0].get_info(), "info2")
        
        self.assertEqual(allCmt[1].get_id(), "id3")
        self.assertEqual(allCmt[1].get_info(), "info3")
    
    def test_delete_then_save(self):
        ada = ActivityDataAccess("test.ini")
        ada.load()
        ada.delete_activity_by_id("id1")

        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "info = info2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "info = info3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_update_then_list(self):
        ada = ActivityDataAccess("test.ini")
        ada.load()
        a = Activity()
        a.set_id("id1")
        a.set_info("info0")
        self.assertTrue(ada.update_activity(a))
        clist = ada.list_all_activities()
        
        self.assertEqual(len(clist), 3)

        a = clist[0]
        self.assertEqual(a.get_id(), "id1")
        self.assertEqual(a.get_info(), "info0")

        a = clist[1]
        self.assertEqual(a.get_id(), "id2")
        self.assertEqual(a.get_info(), "info2")

        a = clist[2]
        self.assertEqual(a.get_id(), "id3")
        self.assertEqual(a.get_info(), "info3")
                    
    def test_update_then_save(self):
        ada = ActivityDataAccess("test.ini")
        ada.load()
        a = Activity()
        a.set_id("id1")
        a.set_info("info0")
        self.assertTrue(ada.update_activity(a))
        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "info = info0\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "info = info2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "info = info3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

