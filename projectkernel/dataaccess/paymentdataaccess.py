"""
 @author Lingyan Zhou
"""
from ..datastructure import Payment

from .basedataaccess import BaseDataAccess

import configparser

class PaymentDataAccess(BaseDataAccess):
    def __init__(self, filename):
        BaseDataAccess.__init__(self)
        self.m_config_parser = configparser.ConfigParser()
        self.m_config_file_name = filename;
        self.m_payments = []

    def load(self):
        self.m_config_parser.read(self.m_config_file_name)
        self.m_payments = list()
        for id in self.m_config_parser.sections():
            p = Payment()
            p.set_id(id)
            p.set_amount(float(self.m_config_parser[id]["amount"]))
            p.set_is_pending(self.m_config_parser[id]["pending"]=="True")
            p.set_user_id(self.m_config_parser[id]["user id"])
            self.m_payments.append(p)

    def save(self):
        with open(self.m_config_file_name, 'wt') as f:
            self.m_config_parser.write(f);

    def list_all(self):
        return list(self.m_payments)

    def add(self, pmt):
        if not pmt.is_complete():
            return False
        
        for existing_pmt in self.m_payments:
            if pmt is existing_pmt:
                return False

        newid = pmt.get_id();
        if newid!=None and newid not in self.m_config_parser.sections():
            pass
        else :
            id = 0;
            while True:
                if str(id) not in self.m_config_parser.sections():
                    newid = str(id)
                    break
                id += 1
            pmt.set_id(newid);
            
        newpmt = Payment()
        newpmt.set_id(pmt.get_id())
        newpmt.set_user_id(pmt.get_user_id())
        newpmt.set_is_pending(pmt.is_pending())
        newpmt.set_amount(pmt.get_amount())
        self.m_payments.append(newpmt)

        self.m_config_parser[newid] = {}
        self.m_config_parser[newid]["user id"] = pmt.get_user_id()
        self.m_config_parser[newid]["pending"] = str(pmt.is_pending())
        self.m_config_parser[newid]["amount"] = str(pmt.get_amount())

        return True;

    def update(self, pmt):
        if not pmt.is_complete():
            return False
        elif (self.m_config_parser.has_section(pmt.get_id())):
            for existing_pmt in self.m_payments:
                if existing_pmt.get_id()== pmt.get_id():
                    existing_pmt.set_user_id(pmt.get_user_id())
                    existing_pmt.set_is_pending(pmt.is_pending())
                    existing_pmt.set_amount(pmt.get_amount())
            self.m_config_parser[pmt.get_id()]["user id"] = pmt.get_user_id()
            self.m_config_parser[pmt.get_id()]["pending"] = str(pmt.is_pending())
            self.m_config_parser[pmt.get_id()]["amount"] = str(pmt.get_amount())
            return True
        else :
            return False
        
    def delete_by_id(self, id):
        for i in range(len(self.m_payments)):
            if self.m_payments[i].get_id()==id:
                self.m_payments.remove(self.m_payments[i])
                break
        self.m_config_parser.remove_section(id)
