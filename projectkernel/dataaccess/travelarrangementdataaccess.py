"""
 @author Lingyan Zhou
"""
from ..datastructure import TravelArrangement

from .basedataaccess import BaseDataAccess

import configparser

class TravelArrangementDataAccess(BaseDataAccess):
    def __init__(self, filename):
        BaseDataAccess.__init__(self)
        self.m_config_parser = configparser.ConfigParser()
        self.m_config_file_name = filename;
        self.m_travelarrangements = []

    def load(self):
        self.m_config_parser.read(self.m_config_file_name)
        self.m_travelarrangements = list()
        for id in self.m_config_parser.sections():
            t = TravelArrangement()
            t.set_id(id)
            t.set_name(self.m_config_parser[id]["name"])
            t.set_description(self.m_config_parser[id]["description"])
            self.m_travelarrangements.append(t)

    def save(self):
        with open(self.m_config_file_name, 'wt') as f:
            self.m_config_parser.write(f);

    def list_all(self):
        return list(self.m_travelarrangements)

    def add(self, agmt):
        if not agmt.is_complete():
            return False
        
        for existing_agmt in self.m_travelarrangements:
            if agmt is existing_agmt:
                return False

        newid = agmt.get_id();
        if newid!=None and newid not in self.m_config_parser.sections():
            pass
        else :
            id = 0;
            while True:
                if str(id) not in self.m_config_parser.sections():
                    newid = str(id)
                    break
                id += 1
            agmt.set_id(newid);
            
        newagmt = TravelArrangement()
        newagmt.set_id(agmt.get_id())
        newagmt.set_name(agmt.get_name())
        newagmt.set_description(agmt.get_description())
        self.m_travelarrangements.append(newagmt)

        self.m_config_parser[newid] = {}
        self.m_config_parser[agmt.get_id()]["name"] = str(agmt.get_name())
        self.m_config_parser[agmt.get_id()]["description"] = str(agmt.get_description())

        return True;

    def update(self, agmt):
        if (self.m_config_parser.has_section(agmt.get_id())):
            for existing_agmt in self.m_travelarrangements:
                if existing_agmt.get_id()== agmt.get_id():
                    existing_agmt.set_name(agmt.get_name())
                    existing_agmt.set_description(agmt.get_description())
            self.m_config_parser[agmt.get_id()]["name"] = str(agmt.get_name())
            self.m_config_parser[agmt.get_id()]["description"] = str(agmt.get_description())
            return True
        else :
            return False
        
    def delete_by_id(self, id):
        for i in range(len(self.m_travelarrangements)):
            if self.m_travelarrangements[i].get_id()==id:
                self.m_travelarrangements.remove(self.m_travelarrangements[i])
                break
        self.m_config_parser.remove_section(id)
