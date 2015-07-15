"""
@author Lingyan Zhou
"""
from projectkernel import User
from projectkernel import UserDataAccess

import os
import configparser
import unittest

class TestUserDataAccess(unittest.TestCase):
    def setUp(self):
        conf = configparser.ConfigParser()
        conf["id1"] = {}
        conf["id1"]["name"] = "name1"
        conf["id1"]["is admin"] = "True"
        conf["id1"]["password"] = "password1"

        conf["id2"] = {}
        conf["id2"]["name"] = "name2"
        conf["id2"]["is admin"] = "True"
        conf["id2"]["password"] = "password2"
        
        conf["id3"] = {}
        conf["id3"]["name"] = "name3"
        conf["id3"]["is admin"] = "False"
        conf["id3"]["password"] = "password3"

        with open("test.ini", "wt") as f:
            conf.write(f)

    def tearDown(self):
        os.remove("test.ini")

    def test_load(self):
        ada = UserDataAccess("test.ini")
        ada.load()
        rlist = ada.list_all()
        
        self.assertEqual(len(rlist), 3)

        a = rlist[0]
        self.assertEqual(a.get_id(), "id1")
        self.assertEqual(a.get_name(), "name1")
        self.assertTrue(a.is_admin())
        self.assertEqual(a.get_password(), "password1")

        a = rlist[1]
        self.assertEqual(a.get_id(), "id2")
        self.assertEqual(a.get_name(), "name2")
        self.assertTrue(a.is_admin())
        self.assertEqual(a.get_password(), "password2")

        a = rlist[2]
        self.assertEqual(a.get_id(), "id3")
        self.assertEqual(a.get_name(), "name3")
        self.assertFalse(a.is_admin())
        self.assertEqual(a.get_password(), "password3")

    def test_find_match(self):
        ada = UserDataAccess("test.ini")
        ada.load()
        self.assertTrue(None!=ada.find_match("id1","password1"))
        self.assertTrue(None!=ada.find_match("id2","password2"))
        self.assertTrue(None!=ada.find_match("id3","password3"))
        self.assertTrue(None==ada.find_match("id1","password2"))
        self.assertTrue(None==ada.find_match("id4","password1"))

    def test_add_save(self):
        ada = UserDataAccess("test.ini")
        r = User()
        r.set_id("id3")
        r.set_name("name3")
        r.set_is_admin(True)
        r.set_password("password3")
        self.assertTrue(ada.add(r))
        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "name = name3\n")
            self.assertEqual(f.readline(), "is admin = True\n")
            self.assertEqual(f.readline(), "password = password3\n")

    def test_add_autoid(self):
        ada = UserDataAccess("test.ini")
        ada.load()
        r = User()
        r.set_id("id3")
        r.set_name("name4")
        r.set_is_admin(False)
        r.set_password("password4")
        self.assertTrue(ada.add(r))
        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "name = name1\n")
            self.assertEqual(f.readline(), "is admin = True\n")
            self.assertEqual(f.readline(), "password = password1\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "name = name2\n")
            self.assertEqual(f.readline(), "is admin = True\n")
            self.assertEqual(f.readline(), "password = password2\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "name = name3\n")
            self.assertEqual(f.readline(), "is admin = False\n")
            self.assertEqual(f.readline(), "password = password3\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[0]\n")
            self.assertEqual(f.readline(), "name = name4\n")
            self.assertEqual(f.readline(), "is admin = False\n")
            self.assertEqual(f.readline(), "password = password4\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_add_then_list(self):
        ada = UserDataAccess("test.ini")
        ada.load()
        a = User()
        a.set_id("id4")
        a.set_name("name4")
        a.set_is_admin(False)
        a.set_password("password4")
        self.assertTrue(ada.add(a))

        allCmt = ada.list_all()
        self.assertEqual(len(allCmt), 4)
        
        lastCmt = allCmt[3]
        self.assertFalse(lastCmt is a)

        self.assertEqual(lastCmt.get_id(), "id4")
        self.assertEqual(lastCmt.get_name(), "name4")
        self.assertFalse(lastCmt.is_admin())
        self.assertEqual(lastCmt.get_password(), "password4")

    def test_delete_then_list(self):
        ada = UserDataAccess("test.ini")
        ada.load()
        ada.delete_by_id("id1")

        allCmt = ada.list_all()
        self.assertEqual(len(allCmt), 2)
        
        self.assertEqual(allCmt[0].get_id(), "id2")
        self.assertEqual(allCmt[0].get_name(), "name2")
        self.assertTrue(allCmt[0].is_admin())
        self.assertEqual(allCmt[0].get_password(), "password2")
        
        self.assertEqual(allCmt[1].get_id(), "id3")
        self.assertEqual(allCmt[1].get_name(), "name3")
        self.assertFalse(allCmt[1].is_admin())
        self.assertEqual(allCmt[1].get_password(), "password3")
    
    def test_delete_then_save(self):
        ada = UserDataAccess("test.ini")
        ada.load()
        ada.delete_by_id("id1")

        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "name = name2\n")
            self.assertEqual(f.readline(), "is admin = True\n")
            self.assertEqual(f.readline(), "password = password2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "name = name3\n")
            self.assertEqual(f.readline(), "is admin = False\n")
            self.assertEqual(f.readline(), "password = password3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_update_then_list(self):
        ada = UserDataAccess("test.ini")
        ada.load()
        a = User()
        a.set_id("id1")
        a.set_name("name0")
        a.set_is_admin(False)
        a.set_password("password0")
        self.assertTrue(ada.update(a))
        clist = ada.list_all()
        
        self.assertEqual(len(clist), 3)

        a = clist[0]
        self.assertEqual(a.get_id(), "id1")
        self.assertEqual(a.get_name(), "name0")
        self.assertFalse(a.is_admin())
        self.assertEqual(a.get_password(), "password0")

        a = clist[1]
        self.assertEqual(a.get_id(), "id2")
        self.assertEqual(a.get_name(), "name2")
        self.assertTrue(a.is_admin())

        self.assertEqual(a.get_password(), "password2")

        a = clist[2]
        self.assertEqual(a.get_id(), "id3")
        self.assertEqual(a.get_name(), "name3")
        self.assertFalse(a.is_admin())
        self.assertEqual(a.get_password(), "password3")
                    
    def test_update_then_save(self):
        ada = UserDataAccess("test.ini")
        ada.load()
        a = User()
        a.set_id("id1")
        a.set_name("name0")
        a.set_is_admin(False)
        a.set_password("password0")
        self.assertTrue(ada.update(a))
        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "name = name0\n")
            self.assertEqual(f.readline(), "is admin = False\n")
            self.assertEqual(f.readline(), "password = password0\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "name = name2\n")
            self.assertEqual(f.readline(), "is admin = True\n")
            self.assertEqual(f.readline(), "password = password2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "name = name3\n")
            self.assertEqual(f.readline(), "is admin = False\n")
            self.assertEqual(f.readline(), "password = password3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

