"""
@author Lingyan Zhou
"""
import projectkernel
import projectkernel.room
from projectkernel.room import Room
import projectkernel.roomdataaccess
from projectkernel.roomdataaccess import RoomDataAccess

import os
import configparser
import unittest

class TestRoomDataAccess(unittest.TestCase):
    def setUp(self):
        conf = configparser.ConfigParser()
        conf["id1"] = {}
        conf["id1"]["name"] = "name1"
        conf["id1"]["info"] = "info1"

        conf["id2"] = {}
        conf["id2"]["name"] = "name2"
        conf["id2"]["info"] = "info2"
        
        conf["id3"] = {}
        conf["id3"]["name"] = "name3"
        conf["id3"]["info"] = "info3"

        with open("test.ini", "wt") as f:
            conf.write(f)

    def tearDown(self):
        os.remove("test.ini")

    def test_load(self):
        rda = RoomDataAccess("test.ini")
        rda.load()
        rlist = rda.list_all()
        
        self.assertEqual(len(rlist), 3)

        r = rlist[0]
        self.assertEqual(r.get_id(), "id1")
        self.assertEqual(r.get_name(), "name1")
        self.assertEqual(r.get_info(), "info1")

        r = rlist[1]
        self.assertEqual(r.get_id(), "id2")
        self.assertEqual(r.get_name(), "name2")
        self.assertEqual(r.get_info(), "info2")

        r = rlist[2]
        self.assertEqual(r.get_id(), "id3")
        self.assertEqual(r.get_name(), "name3")
        self.assertEqual(r.get_info(), "info3")

    def test_add_save(self):
        rda = RoomDataAccess("test.ini")
        r = Room()
        r.set_id("id3")
        r.set_name("name3")
        r.set_info("info3")
        self.assertTrue(rda.add(r))
        rda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "name = name3\n")
            self.assertEqual(f.readline(), "info = info3\n")

    def test_add_autoid(self):
        rda = RoomDataAccess("test.ini")
        rda.load()
        r = Room()
        r.set_id("id3")
        r.set_name("name3")
        r.set_info("info3")
        self.assertTrue(rda.add(r))
        rda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "name = name1\n")
            self.assertEqual(f.readline(), "info = info1\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "name = name2\n")
            self.assertEqual(f.readline(), "info = info2\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "name = name3\n")
            self.assertEqual(f.readline(), "info = info3\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[0]\n")
            self.assertEqual(f.readline(), "name = name3\n")
            self.assertEqual(f.readline(), "info = info3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_add_then_list(self):
        rda = RoomDataAccess("test.ini")
        rda.load()
        r = Room()
        r.set_id("id4")
        r.set_name("name3")
        r.set_info("info3")
        self.assertTrue(rda.add(r))

        allRoom = rda.list_all()
        self.assertEqual(len(allRoom), 4)
        
        lastRoom = allRoom[3]
        self.assertFalse(lastRoom is r)

        self.assertEqual(lastRoom.get_id(), "id4")
        self.assertEqual(lastRoom.get_name(), "name3")
        self.assertEqual(lastRoom.get_info(), "info3")

    def test_delete_then_list(self):
        rda = RoomDataAccess("test.ini")
        rda.load()
        rda.delete_by_id("id1")

        allCmt = rda.list_all()
        self.assertEqual(len(allCmt), 2)
        
        self.assertEqual(allCmt[0].get_id(), "id2")
        self.assertEqual(allCmt[0].get_name(), "name2")
        self.assertEqual(allCmt[0].get_info(), "info2")
        
        self.assertEqual(allCmt[1].get_id(), "id3")
        self.assertEqual(allCmt[1].get_name(), "name3")
        self.assertEqual(allCmt[1].get_info(), "info3")
    
    def test_delete_then_save(self):
        rda = RoomDataAccess("test.ini")
        rda.load()
        rda.delete_by_id("id1")

        rda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "name = name2\n")
            self.assertEqual(f.readline(), "info = info2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "name = name3\n")
            self.assertEqual(f.readline(), "info = info3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_update_then_list(self):
        rda = RoomDataAccess("test.ini")
        rda.load()
        r = Room()
        r.set_id("id1")
        r.set_name("name0")
        r.set_info("info0")
        self.assertTrue(rda.update(r))
        rlist = rda.list_all()
        
        self.assertEqual(len(rlist), 3)

        r = rlist[0]
        self.assertEqual(r.get_id(), "id1")
        self.assertEqual(r.get_name(), "name0")
        self.assertEqual(r.get_info(), "info0")

        r = rlist[1]
        self.assertEqual(r.get_id(), "id2")
        self.assertEqual(r.get_name(), "name2")
        self.assertEqual(r.get_info(), "info2")

        r = rlist[2]
        self.assertEqual(r.get_id(), "id3")
        self.assertEqual(r.get_name(), "name3")
        self.assertEqual(r.get_info(), "info3")
                    
    def test_update_then_save(self):
        rda = RoomDataAccess("test.ini")
        rda.load()
        r = Room()
        r.set_id("id1")
        r.set_name("name0")
        r.set_info("info0")
        self.assertTrue(rda.update(r))
        rda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "name = name0\n")
            self.assertEqual(f.readline(), "info = info0\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "name = name2\n")
            self.assertEqual(f.readline(), "info = info2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "name = name3\n")
            self.assertEqual(f.readline(), "info = info3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

