"""
@author Lingyan Zhou
"""
from projectkernel import ActivityReservation

import unittest
import datetime

class TestActivityReservation(unittest.TestCase):

    def test_user_id(self):
        r = ActivityReservation()
        r.set_user_id("Name1")
        self.assertEqual(r.get_user_id(), "Name1")
        r.set_user_id("Name2")
        self.assertEqual(r.get_user_id(), "Name2")

    def test_start_time(self):
        r = ActivityReservation()
        r.set_start_time(2016, 2, 29, 12)
        self.assertEqual(r.get_start_time(), datetime.datetime(2016, 2, 29, 12))
        with self.assertRaises(ValueError):
            r.set_start_time(2015, 2, 29, 12)
        with self.assertRaises(ValueError):
            r.set_start_time(2100, 2, 29, 12)

    def test_end_time(self):
        r = ActivityReservation()
        r.set_end_time(2016, 2, 29, 12)
        self.assertEqual(r.get_end_time(), datetime.datetime(2016, 2, 29, 12))
        with self.assertRaises(ValueError):
            r.set_end_time(2015, 2, 29, 12)
        with self.assertRaises(ValueError):
            r.set_end_time(2100, 2, 29, 12)

    def test_id(self):
        r = ActivityReservation()
        r.set_id("1")
        self.assertEqual(r.get_id(), "1")
        r.set_id("2")
        self.assertEqual(r.get_id(), "2")

    def test_room_id(self):
        r = ActivityReservation()
        r.set_activity_id("1")
        self.assertEqual(r.get_activity_id(), "1")
        r.set_activity_id("2")
        self.assertEqual(r.get_activity_id(), "2")

    def test_time_is_valid(self):
        r = ActivityReservation()
        r.set_start_time(2016, 2, 29, 12)
        r.set_end_time(2016, 2, 29, 12)
        self.assertEqual(r.is_reservation_time_valid(), False)
        r.set_start_time(2016, 3, 29, 12)
        self.assertEqual(r.is_reservation_time_valid(), False)
        r.set_end_time(2016, 3, 29, 14)
        self.assertEqual(r.is_reservation_time_valid(), True)

    def test_has_expired(self):
        r = ActivityReservation()
        r.set_start_time(2099, 3, 29, 12)
        r.set_end_time(2099, 3, 29, 14)
        self.assertEqual(r.has_expired(), False)
        r.set_start_time(2000, 3, 29, 12)
        r.set_end_time(2000, 3, 29, 14)
        self.assertEqual(r.has_expired(), True)
        r.set_start_time(2000, 3, 29, 12)
        r.set_end_time(2099, 3, 29, 14)
        self.assertEqual(r.has_expired(), False)

    def test_conflict(self):
        r1 = ActivityReservation()
        r2 = ActivityReservation()
        r1.set_user_id("1")
        r2.set_user_id("2")
        r1.set_activity_id("1")
        r2.set_activity_id("2")

        r1.set_start_time(2000, 3, 29, 12)
        r1.set_end_time(2000, 3, 29, 15)
        r2.set_start_time(2000, 3, 29, 12)
        r2.set_end_time(2000, 3, 29, 15)
        self.assertEqual(r1.conflict_with(r2), False)
        self.assertEqual(r2.conflict_with(r1), False)

        r2.set_activity_id("1")
        self.assertEqual(r1.conflict_with(r2), True)
        self.assertEqual(r2.conflict_with(r1), True)

        r2.set_user_id("1")
        r2.set_activity_id("2")
        self.assertEqual(r1.conflict_with(r2), True)
        self.assertEqual(r2.conflict_with(r1), True)

        r1.set_user_id("1")
        r2.set_user_id("2")
        r1.set_activity_id("1")
        r2.set_activity_id("1")

        r2.set_start_time(2000, 3, 29, 11)
        r2.set_end_time(2000, 3, 29, 12)
        self.assertEqual(r1.conflict_with(r2), False)
        self.assertEqual(r2.conflict_with(r1), False)
        r2.set_start_time(2000, 3, 29, 11)
        r2.set_end_time(2000, 3, 29, 13)
        self.assertEqual(r1.conflict_with(r2), True)
        self.assertEqual(r2.conflict_with(r1), True)
        r2.set_start_time(2000, 3, 29, 12)
        r2.set_end_time(2000, 3, 29, 15)
        self.assertEqual(r1.conflict_with(r2), True)
        self.assertEqual(r2.conflict_with(r1), True)

        r2.set_start_time(2000, 3, 29, 14)
        r2.set_end_time(2000, 3, 29, 15)
        self.assertEqual(r1.conflict_with(r2), True)
        self.assertEqual(r2.conflict_with(r1), True)
        r2.set_start_time(2000, 3, 29, 14)
        r2.set_end_time(2000, 3, 29, 16)
        self.assertEqual(r1.conflict_with(r2), True)
        self.assertEqual(r2.conflict_with(r1), True)
        r2.set_start_time(2000, 3, 29, 15)
        r2.set_end_time(2000, 3, 29, 16)
        self.assertEqual(r1.conflict_with(r2), False)
        self.assertEqual(r2.conflict_with(r1), False)
        
