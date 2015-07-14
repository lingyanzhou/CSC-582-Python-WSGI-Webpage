"""
@author Lingyan Zhou
"""
import projectkernel
import projectkernel.payment
from projectkernel.payment import Payment
import projectkernel.paymentdataaccess
from projectkernel.paymentdataaccess import PaymentDataAccess

import os
import configparser
import unittest

class TestPaymentDataAccess(unittest.TestCase):
    def setUp(self):
        conf = configparser.ConfigParser()
        conf["id1"] = {}
        conf["id1"]["amount"] = "1.1"

        conf["id2"] = {}
        conf["id2"]["amount"] = "2.2"
        
        conf["id3"] = {}
        conf["id3"]["amount"] = "3.3"

        with open("test.ini", "wt") as f:
            conf.write(f)

    def tearDown(self):
        os.remove("test.ini")

    def test_load(self):
        ada = PaymentDataAccess("test.ini")
        ada.load()
        rlist = ada.list_all()
        
        self.assertEqual(len(rlist), 3)

        a = rlist[0]
        self.assertEqual(a.get_id(), "id1")
        self.assertEqual(a.get_amount(), 1.1)

        a = rlist[1]
        self.assertEqual(a.get_id(), "id2")
        self.assertEqual(a.get_amount(), 2.2)

        a = rlist[2]
        self.assertEqual(a.get_id(), "id3")
        self.assertEqual(a.get_amount(), 3.3)

    def test_add_save(self):
        ada = PaymentDataAccess("test.ini")
        r = Payment()
        r.set_id("id3")
        r.set_amount(3.3)
        self.assertTrue(ada.add(r))
        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "amount = 3.3\n")

    def test_add_autoid(self):
        ada = PaymentDataAccess("test.ini")
        ada.load()
        r = Payment()
        r.set_id("id3")
        r.set_amount(3.3)
        self.assertTrue(ada.add(r))
        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "amount = 1.1\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "amount = 2.2\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "amount = 3.3\n")

            self.assertEqual(f.readline(), "\n")
            
            self.assertEqual(f.readline(), "[0]\n")
            self.assertEqual(f.readline(), "amount = 3.3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_add_then_list(self):
        ada = PaymentDataAccess("test.ini")
        ada.load()
        a = Payment()
        a.set_id("id4")
        a.set_amount(4.4)
        self.assertTrue(ada.add(a))

        allCmt = ada.list_all()
        self.assertEqual(len(allCmt), 4)
        
        lastCmt = allCmt[3]
        self.assertFalse(lastCmt is a)

        self.assertEqual(lastCmt.get_id(), "id4")
        self.assertEqual(lastCmt.get_amount(), 4.4)

    def test_delete_then_list(self):
        ada = PaymentDataAccess("test.ini")
        ada.load()
        ada.delete_by_id("id1")

        allCmt = ada.list_all()
        self.assertEqual(len(allCmt), 2)
        
        self.assertEqual(allCmt[0].get_id(), "id2")
        self.assertEqual(allCmt[0].get_amount(), 2.2)
        
        self.assertEqual(allCmt[1].get_id(), "id3")
        self.assertEqual(allCmt[1].get_amount(), 3.3)
    
    def test_delete_then_save(self):
        ada = PaymentDataAccess("test.ini")
        ada.load()
        ada.delete_by_id("id1")

        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "amount = 2.2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "amount = 3.3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

    def test_update_then_list(self):
        ada = PaymentDataAccess("test.ini")
        ada.load()
        a = Payment()
        a.set_id("id1")
        a.set_amount(1.2)
        self.assertTrue(ada.update(a))
        clist = ada.list_all()
        
        self.assertEqual(len(clist), 3)

        a = clist[0]
        self.assertEqual(a.get_id(), "id1")
        self.assertEqual(a.get_amount(), 1.2)

        a = clist[1]
        self.assertEqual(a.get_id(), "id2")
        self.assertEqual(a.get_amount(), 2.2)

        a = clist[2]
        self.assertEqual(a.get_id(), "id3")
        self.assertEqual(a.get_amount(), 3.3)
                    
    def test_update_then_save(self):
        ada = PaymentDataAccess("test.ini")
        ada.load()
        a = Payment()
        a.set_id("id1")
        a.set_amount(1.2)
        self.assertTrue(ada.update(a))
        ada.save()

        with open("test.ini", "rt") as f:
            self.assertEqual(f.readline(), "[id1]\n")
            self.assertEqual(f.readline(), "amount = 1.2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id2]\n")
            self.assertEqual(f.readline(), "amount = 2.2\n")

            self.assertEqual(f.readline(), "\n")

            self.assertEqual(f.readline(), "[id3]\n")
            self.assertEqual(f.readline(), "amount = 3.3\n")

            self.assertEqual(f.readline(), "\n")
            self.assertEqual(f.readline(), "")

