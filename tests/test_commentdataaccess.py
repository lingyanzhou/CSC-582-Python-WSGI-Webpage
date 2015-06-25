"""
@author Lingyan Zhou
"""
import projectkernel
import projectkernel.comment
from projectkernel.comment import Comment
import projectkernel.commentdataaccess
from projectkernel.commentdataaccess import CommentDataAccess

import os
import datetime
import configparser
import unittest

class TestCommentDataAccess(unittest.TestCase):
    def setUp(self):
        conf = configparser.ConfigParser()
        conf["id1"] = {}
        conf["id1"]["time"] = "06/10/15 12:00:00"
        conf["id1"]["user"] = "user1"
        conf["id1"]["message"] = "message1"

        conf["id2"] = {}
        conf["id2"]["time"] = "06/10/15 12:00:00"
        conf["id2"]["user"] = "user2"
        conf["id2"]["message"] = "message2"
        
        conf["id3"] = {}
        conf["id3"]["time"] = "06/11/15 12:00:00"
        conf["id3"]["user"] = "user3"
        conf["id3"]["message"] = "message3"

        with open("test.ini", "wt") as f:
            conf.write(f)

    def tearDown(self):
        os.remove("test.ini")

    def test_load(self):
        cda = CommentDataAccess("test.ini")
        cda.load()
        rlist = cda.list_all_comments()
        
        self.assertEqual(len(rlist), 3)

        c = rlist[0]
        self.assertEqual(c.get_id(), "id1")
        self.assertEqual(c.get_user_name(), "user1")
        self.assertEqual(c.get_message(), "message1")
        self.assertEqual(c.get_time(), datetime.datetime(2015, 6, 10, 12))

        c = rlist[1]
        self.assertEqual(c.get_id(), "id2")
        self.assertEqual(c.get_user_name(), "user2")
        self.assertEqual(c.get_message(), "message2")
        self.assertEqual(c.get_time(), datetime.datetime(2015, 6, 10, 12))

        c = rlist[2]
        self.assertEqual(c.get_id(), "id3")
        self.assertEqual(c.get_user_name(), "user3")
        self.assertEqual(c.get_message(), "message3")
        self.assertEqual(c.get_time(), datetime.datetime(2015, 6, 11, 12))

    def test_add_save(self):
        cda = CommentDataAccess("test.ini")
        r = Comment()
        r.set_id("id3")
        r.set_user_name("user3")
        r.set_message("message3")
        r.set_time(2015, 6, 11, 12)
        self.assertTrue(cda.add_comment(r))
        cda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "time = 06/11/15 12:00:00\n")
            self.assertEqual(f.readline(), "user = user3\n")
            self.assertEqual(f.readline(), "message = message3\n")

    def test_add_autoid(self):
        cda = CommentDataAccess("test.ini")
        cda.load()
        r = Comment()
        r.set_id("id3")
        r.set_user_name("user4")
        r.set_message("message3")
        r.set_time(2015, 6, 12, 16)
        self.assertTrue(cda.add_comment(r))
        cda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "user = user1\n")
            self.assertEqual(f.readline(), "message = message1\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "user = user2\n")
            self.assertEqual(f.readline(), "message = message2\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "time = 06/11/15 12:00:00\n")
            self.assertEqual(f.readline(), "user = user3\n")
            self.assertEqual(f.readline(), "message = message3\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[0]\n")
            self.assertEqual(f.readline(), "time = 06/12/15 16:00:00\n")
            self.assertEqual(f.readline(), "user = user4\n")
            self.assertEqual(f.readline(), "message = message3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_add_then_list(self):
        cda = CommentDataAccess("test.ini")
        cda.load()
        c = Comment()
        c.set_id("id4")
        c.set_user_name("user4")
        c.set_message("message3")
        c.set_time(2015, 6, 12, 16)
        self.assertTrue(cda.add_comment(c))

        allCmt = cda.list_all_comments()
        self.assertEqual(len(allCmt), 4)
        
        lastCmt = allCmt[3]
        self.assertFalse(lastCmt is c)

        self.assertEqual(lastCmt.get_id(), "id4")
        self.assertEqual(lastCmt.get_user_name(), "user4")
        self.assertEqual(lastCmt.get_message(), "message3")
        self.assertEqual(lastCmt.get_time_as_str(), "06/12/15 16:00:00")

    def test_delete_then_list(self):
        cda = CommentDataAccess("test.ini")
        cda.load()
        cda.delete_comment_by_id("id1")

        allCmt = cda.list_all_comments()
        self.assertEqual(len(allCmt), 2)
        
        self.assertEqual(allCmt[0].get_id(), "id2")
        self.assertEqual(allCmt[0].get_user_name(), "user2")
        self.assertEqual(allCmt[0].get_message(), "message2")
        self.assertEqual(allCmt[0].get_time_as_str(), "06/10/15 12:00:00")
        
        self.assertEqual(allCmt[1].get_id(), "id3")
        self.assertEqual(allCmt[1].get_user_name(), "user3")
        self.assertEqual(allCmt[1].get_message(), "message3")
        self.assertEqual(allCmt[1].get_time_as_str(), "06/11/15 12:00:00")
    
    def test_delete_then_save(self):
        cda = CommentDataAccess("test.ini")
        cda.load()
        cda.delete_comment_by_id("id1")

        cda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "user = user2\n")
            self.assertEqual(f.readline(), "message = message2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "time = 06/11/15 12:00:00\n")
            self.assertEqual(f.readline(), "user = user3\n")
            self.assertEqual(f.readline(), "message = message3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_update_then_list(self):
        cda = CommentDataAccess("test.ini")
        cda.load()
        c = Comment()
        c.set_id("id1")
        c.set_time(2015, 1, 1, 1)
        c.set_message("message0")
        c.set_user_name("user0")
        self.assertTrue(cda.update_comment(c))
        clist = cda.list_all_comments()
        
        self.assertEqual(len(clist), 3)

        c = clist[0]
        self.assertEqual(c.get_id(), "id1")
        self.assertEqual(c.get_user_name(), "user0")
        self.assertEqual(c.get_message(), "message0")
        self.assertEqual(c.get_time(), datetime.datetime(2015, 1, 1, 1))

        c = clist[1]
        self.assertEqual(c.get_id(), "id2")
        self.assertEqual(c.get_user_name(), "user2")
        self.assertEqual(c.get_message(), "message2")
        self.assertEqual(c.get_time(), datetime.datetime(2015, 6, 10, 12))

        c = clist[2]
        self.assertEqual(c.get_id(), "id3")
        self.assertEqual(c.get_user_name(), "user3")
        self.assertEqual(c.get_message(), "message3")
        self.assertEqual(c.get_time(), datetime.datetime(2015, 6, 11, 12))
                    
    def test_update_then_save(self):
        cda = CommentDataAccess("test.ini")
        cda.load()
        c = Comment()
        c.set_id("id1")
        c.set_time(2015, 1, 1, 1)
        c.set_message("message0")
        c.set_user_name("user0")
        self.assertTrue(cda.update_comment(c))
        cda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "time = 01/01/15 01:00:00\n")
            self.assertEqual(f.readline(), "user = user0\n")
            self.assertEqual(f.readline(), "message = message0\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "user = user2\n")
            self.assertEqual(f.readline(), "message = message2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "time = 06/11/15 12:00:00\n")
            self.assertEqual(f.readline(), "user = user3\n")
            self.assertEqual(f.readline(), "message = message3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

