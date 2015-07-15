"""
@author Lingyan Zhou
"""
from projectkernel import RoomReservation
from projectkernel import RoomReservationDataAccess

import os
import datetime
import configparser
import unittest

class TestRoomRoomReservationDataAccess(unittest.TestCase):
    def setUp(self):
        conf = configparser.ConfigParser()
        conf["id1"] = {}
        conf["id1"]["start time"] = "06/10/15 12:00:00"
        conf["id1"]["end time"] = "06/10/15 16:00:00"
        conf["id1"]["user id"] = "user id1"
        conf["id1"]["room id"] = "room1"

        conf["id2"] = {}
        conf["id2"]["start time"] = "06/10/15 12:00:00"
        conf["id2"]["end time"] = "06/10/15 16:00:00"
        conf["id2"]["user id"] = "user id2"
        conf["id2"]["room id"] = "room2"
        
        conf["id3"] = {}
        conf["id3"]["start time"] = "06/11/15 12:00:00"
        conf["id3"]["end time"] = "06/12/15 16:00:00"
        conf["id3"]["user id"] = "user id3"
        conf["id3"]["room id"] = "room3"

        with open("test.ini", "wt") as f:
            conf.write(f)

    def tearDown(self):
        os.remove("test.ini")

    def test_load(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        rlist = rda.list_all_reservations()
        
        self.assertEqual(len(rlist), 3)

        rsv = rlist[0]
        self.assertEqual(rsv.get_id(), "id1")
        self.assertEqual(rsv.get_user_id(), "user id1")
        self.assertEqual(rsv.get_reserved_room_id(), "room1")
        self.assertEqual(rsv.get_start_time(), datetime.datetime(2015, 6, 10, 12))
        self.assertEqual(rsv.get_end_time(), datetime.datetime(2015, 6, 10, 16))        

        rsv = rlist[1]
        self.assertEqual(rsv.get_id(), "id2")
        self.assertEqual(rsv.get_user_id(), "user id2")
        self.assertEqual(rsv.get_reserved_room_id(), "room2")
        self.assertEqual(rsv.get_start_time(), datetime.datetime(2015, 6, 10, 12))
        self.assertEqual(rsv.get_end_time(), datetime.datetime(2015, 6, 10, 16))

        rsv = rlist[2]
        self.assertEqual(rsv.get_id(), "id3")
        self.assertEqual(rsv.get_user_id(), "user id3")
        self.assertEqual(rsv.get_reserved_room_id(), "room3")
        self.assertEqual(rsv.get_start_time(), datetime.datetime(2015, 6, 11, 12))
        self.assertEqual(rsv.get_end_time(), datetime.datetime(2015, 6, 12, 16))        

    def test_add_save(self):
        rda = RoomReservationDataAccess("test.ini")
        r = RoomReservation()
        r.set_id("id3")
        r.set_user_id("user id3")
        r.set_reserved_room_id("room3")
        r.set_start_time(2015, 6, 11, 12)
        r.set_end_time(2015, 6, 12, 16)
        self.assertTrue(rda.add_reservation(r))
        rda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "start time = 06/11/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/12/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id3\n")
            self.assertEqual(f.readline(), "room id = room3\n")

    def test_add_save_conflict(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        r = RoomReservation()
        r.set_id("id3")
        r.set_user_id("user id4")
        r.set_reserved_room_id("room3")
        r.set_start_time(2015, 6, 11, 12)
        r.set_end_time(2015, 6, 12, 16)
        self.assertFalse(rda.add_reservation(r))
        rda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "start time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/10/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id1\n")
            self.assertEqual(f.readline(), "room id = room1\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "start time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/10/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id2\n")
            self.assertEqual(f.readline(), "room id = room2\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "start time = 06/11/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/12/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id3\n")
            self.assertEqual(f.readline(), "room id = room3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")
        
    def test_add_autoid(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        r = RoomReservation()
        r.set_id("id3")
        r.set_user_id("user id4")
        r.set_reserved_room_id("room3")
        r.set_start_time(2015, 6, 12, 16)
        r.set_end_time(2015, 6, 12, 18)
        self.assertTrue(rda.add_reservation(r))
        rda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "start time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/10/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id1\n")
            self.assertEqual(f.readline(), "room id = room1\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "start time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/10/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id2\n")
            self.assertEqual(f.readline(), "room id = room2\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "start time = 06/11/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/12/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id3\n")
            self.assertEqual(f.readline(), "room id = room3\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[0]\n")
            self.assertEqual(f.readline(), "start time = 06/12/15 16:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/12/15 18:00:00\n")
            self.assertEqual(f.readline(), "user id = user id4\n")
            self.assertEqual(f.readline(), "room id = room3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_add_then_list(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        r = RoomReservation()
        r.set_id("id4")
        r.set_user_id("user id4")
        r.set_reserved_room_id("room3")
        r.set_start_time(2015, 6, 12, 16)
        r.set_end_time(2015, 6, 12, 18)
        self.assertTrue(rda.add_reservation(r))

        allRsv = rda.list_all_reservations()
        self.assertEqual(len(allRsv), 4)
        
        lastRsv = allRsv[3]
        self.assertFalse(lastRsv is r)

        self.assertEqual(lastRsv.get_id(), "id4")
        self.assertEqual(lastRsv.get_user_id(), "user id4")
        self.assertEqual(lastRsv.get_reserved_room_id(), "room3")
        self.assertEqual(lastRsv.get_start_time_as_str(), "06/12/15 16:00:00")
        self.assertEqual(lastRsv.get_end_time_as_str(), "06/12/15 18:00:00")

    def test_delete_then_list_1(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        rda.delete_reservation_by_id("id1")

        allRsv = rda.list_all_reservations()
        self.assertEqual(len(allRsv), 2)
        
        self.assertEqual(allRsv[0].get_id(), "id2")
        self.assertEqual(allRsv[0].get_user_id(), "user id2")
        self.assertEqual(allRsv[0].get_reserved_room_id(), "room2")
        self.assertEqual(allRsv[0].get_start_time_as_str(), "06/10/15 12:00:00")
        self.assertEqual(allRsv[0].get_end_time_as_str(), "06/10/15 16:00:00")
        
        self.assertEqual(allRsv[1].get_id(), "id3")
        self.assertEqual(allRsv[1].get_user_id(), "user id3")
        self.assertEqual(allRsv[1].get_reserved_room_id(), "room3")
        self.assertEqual(allRsv[1].get_start_time_as_str(), "06/11/15 12:00:00")
        self.assertEqual(allRsv[1].get_end_time_as_str(), "06/12/15 16:00:00")
    
    def test_delete_then_list_2(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        rda.delete_reservation_by_id("id2")

        allRsv = rda.list_all_reservations()
        self.assertEqual(len(allRsv), 2)
        
        self.assertEqual(allRsv[0].get_id(), "id1")
        self.assertEqual(allRsv[0].get_user_id(), "user id1")
        self.assertEqual(allRsv[0].get_reserved_room_id(), "room1")
        self.assertEqual(allRsv[0].get_start_time_as_str(), "06/10/15 12:00:00")
        self.assertEqual(allRsv[0].get_end_time_as_str(), "06/10/15 16:00:00")
        
        self.assertEqual(allRsv[1].get_id(), "id3")
        self.assertEqual(allRsv[1].get_user_id(), "user id3")
        self.assertEqual(allRsv[1].get_reserved_room_id(), "room3")
        self.assertEqual(allRsv[1].get_start_time_as_str(), "06/11/15 12:00:00")
        self.assertEqual(allRsv[1].get_end_time_as_str(), "06/12/15 16:00:00")

    def test_delete_then_list_3(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        rda.delete_reservation_by_id("id3")

        allRsv = rda.list_all_reservations()
        self.assertEqual(len(allRsv), 2)
        
        self.assertEqual(allRsv[0].get_id(), "id1")
        self.assertEqual(allRsv[0].get_user_id(), "user id1")
        self.assertEqual(allRsv[0].get_reserved_room_id(), "room1")
        self.assertEqual(allRsv[0].get_start_time_as_str(), "06/10/15 12:00:00")
        self.assertEqual(allRsv[0].get_end_time_as_str(), "06/10/15 16:00:00")
        
        self.assertEqual(allRsv[1].get_id(), "id2")
        self.assertEqual(allRsv[1].get_user_id(), "user id2")
        self.assertEqual(allRsv[1].get_reserved_room_id(), "room2")
        self.assertEqual(allRsv[1].get_start_time_as_str(), "06/10/15 12:00:00")
        self.assertEqual(allRsv[1].get_end_time_as_str(), "06/10/15 16:00:00")

    def test_delete_then_save_1(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        rda.delete_reservation_by_id("id1")

        rda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "start time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/10/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id2\n")
            self.assertEqual(f.readline(), "room id = room2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "start time = 06/11/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/12/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id3\n")
            self.assertEqual(f.readline(), "room id = room3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_delete_then_save_2(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        rda.delete_reservation_by_id("id2")

        rda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "start time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/10/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id1\n")
            self.assertEqual(f.readline(), "room id = room1\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "start time = 06/11/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/12/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id3\n")
            self.assertEqual(f.readline(), "room id = room3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_delete_then_save_3(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        rda.delete_reservation_by_id("id3")

        rda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "start time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/10/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id1\n")
            self.assertEqual(f.readline(), "room id = room1\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "start time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/10/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id2\n")
            self.assertEqual(f.readline(), "room id = room2\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_update_then_list(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        r = RoomReservation()
        r.set_id("id1")
        r.set_start_time(2015, 1, 1, 1)
        r.set_end_time(2015, 1, 1, 3)
        r.set_reserved_room_id("room0")
        r.set_user_id("user id0")
        rda.update_reservation(r)
        rlist = rda.list_all_reservations()
        
        self.assertEqual(len(rlist), 3)

        rsv = rlist[0]
        self.assertEqual(rsv.get_id(), "id1")
        self.assertEqual(rsv.get_user_id(), "user id0")
        self.assertEqual(rsv.get_reserved_room_id(), "room0")
        self.assertEqual(rsv.get_start_time(), datetime.datetime(2015, 1, 1, 1))
        self.assertEqual(rsv.get_end_time(), datetime.datetime(2015, 1, 1, 3))        

        rsv = rlist[1]
        self.assertEqual(rsv.get_id(), "id2")
        self.assertEqual(rsv.get_user_id(), "user id2")
        self.assertEqual(rsv.get_reserved_room_id(), "room2")
        self.assertEqual(rsv.get_start_time(), datetime.datetime(2015, 6, 10, 12))
        self.assertEqual(rsv.get_end_time(), datetime.datetime(2015, 6, 10, 16))

        rsv = rlist[2]
        self.assertEqual(rsv.get_id(), "id3")
        self.assertEqual(rsv.get_user_id(), "user id3")
        self.assertEqual(rsv.get_reserved_room_id(), "room3")
        self.assertEqual(rsv.get_start_time(), datetime.datetime(2015, 6, 11, 12))
        self.assertEqual(rsv.get_end_time(), datetime.datetime(2015, 6, 12, 16))
                    
    def test_update_then_save(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        r = RoomReservation()
        r.set_id("id1")
        r.set_start_time(2015, 1, 1, 1)
        r.set_end_time(2015, 1, 1, 3)
        r.set_reserved_room_id("room0")
        r.set_user_id("user id0")
        self.assertTrue(rda.update_reservation(r))
        rda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "start time = 01/01/15 01:00:00\n")
            self.assertEqual(f.readline(), "end time = 01/01/15 03:00:00\n")
            self.assertEqual(f.readline(), "user id = user id0\n")
            self.assertEqual(f.readline(), "room id = room0\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "start time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/10/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id2\n")
            self.assertEqual(f.readline(), "room id = room2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "start time = 06/11/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/12/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id3\n")
            self.assertEqual(f.readline(), "room id = room3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")
 
    def test_update_with_conflict_then_list(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        r = RoomReservation()
        r.set_id("id1")
        r.set_start_time(2015, 6, 11, 1)
        r.set_end_time(2015, 6, 12, 3)
        r.set_reserved_room_id("room3")
        r.set_user_id("user id1")
        self.assertFalse(rda.update_reservation(r))
        r.set_id("id4")
        r.set_start_time(2015, 6, 11, 1)
        r.set_end_time(2015, 6, 12, 3)
        r.set_reserved_room_id("room0")
        r.set_user_id("user id4")
        self.assertFalse(rda.update_reservation(r))
        r.set_id("id1")
        r.set_start_time(2015, 6, 11, 1)
        r.set_end_time(2015, 6, 12, 3)
        r.set_reserved_room_id("room0")
        r.set_user_id("user id3")
        self.assertFalse(rda.update_reservation(r))
        rlist = rda.list_all_reservations()
        
        self.assertEqual(len(rlist), 3)

        rsv = rlist[0]
        self.assertEqual(rsv.get_id(), "id1")
        self.assertEqual(rsv.get_user_id(), "user id1")
        self.assertEqual(rsv.get_reserved_room_id(), "room1")
        self.assertEqual(rsv.get_start_time(), datetime.datetime(2015, 6, 10, 12))
        self.assertEqual(rsv.get_end_time(), datetime.datetime(2015, 6, 10, 16))        

        rsv = rlist[1]
        self.assertEqual(rsv.get_id(), "id2")
        self.assertEqual(rsv.get_user_id(), "user id2")
        self.assertEqual(rsv.get_reserved_room_id(), "room2")
        self.assertEqual(rsv.get_start_time(), datetime.datetime(2015, 6, 10, 12))
        self.assertEqual(rsv.get_end_time(), datetime.datetime(2015, 6, 10, 16))

        rsv = rlist[2]
        self.assertEqual(rsv.get_id(), "id3")
        self.assertEqual(rsv.get_user_id(), "user id3")
        self.assertEqual(rsv.get_reserved_room_id(), "room3")
        self.assertEqual(rsv.get_start_time(), datetime.datetime(2015, 6, 11, 12))
        self.assertEqual(rsv.get_end_time(), datetime.datetime(2015, 6, 12, 16))

    def test_update_with_conflict_then_save(self):
        rda = RoomReservationDataAccess("test.ini")
        rda.load()
        r = RoomReservation()
        r.set_id("id1")
        r.set_start_time(2015, 6, 11, 1)
        r.set_end_time(2015, 6, 12, 3)
        r.set_reserved_room_id("room3")
        r.set_user_id("user id1")
        self.assertFalse(rda.update_reservation(r))
        r.set_id("id4")
        r.set_start_time(2015, 6, 11, 1)
        r.set_end_time(2015, 6, 12, 3)
        r.set_reserved_room_id("room0")
        r.set_user_id("user id4")
        self.assertFalse(rda.update_reservation(r))
        r.set_id("id1")
        r.set_start_time(2015, 6, 11, 1)
        r.set_end_time(2015, 6, 12, 3)
        r.set_reserved_room_id("room0")
        r.set_user_id("user id3")
        self.assertFalse(rda.update_reservation(r))
        rda.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "start time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/10/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id1\n")
            self.assertEqual(f.readline(), "room id = room1\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "start time = 06/10/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/10/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id2\n")
            self.assertEqual(f.readline(), "room id = room2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "start time = 06/11/15 12:00:00\n")
            self.assertEqual(f.readline(), "end time = 06/12/15 16:00:00\n")
            self.assertEqual(f.readline(), "user id = user id3\n")
            self.assertEqual(f.readline(), "room id = room3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")
               
