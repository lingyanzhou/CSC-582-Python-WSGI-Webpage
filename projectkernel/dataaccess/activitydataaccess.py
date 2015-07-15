"""
 @author Lingyan Zhou
"""
from ..datastructure import Activity

from .basedataaccess import BaseDataAccess

import configparser

class ActivityDataAccess(BaseDataAccess):
    def __init__(self, filename):
        BaseDataAccess.__init__(self)
        self.m_config_parser = configparser.ConfigParser()
        self.m_config_file_name = filename;
        self.m_activities = []

    def load(self):
        self.m_config_parser.read(self.m_config_file_name)
        self.m_activities = list()
        for id in self.m_config_parser.sections():
            c = Activity()
            c.set_id(id)
            c.set_name(self.m_config_parser[id]["name"])
            c.set_info(self.m_config_parser[id]["info"])
            self.m_activities.append(c)

    def save(self):
        with open(self.m_config_file_name, 'wt') as f:
            self.m_config_parser.write(f);

    def list_all_activities(self):
        return list(self.m_activities)

    def add_activity(self, atv):
        if not atv.is_complete():
            return False
        
        for existing_atv in self.m_activities:
            if atv is existing_atv:
                return False

        newid = atv.get_id();
        if newid!=None and newid not in self.m_config_parser.sections():
            pass
        else :
            id = 0;
            while True:
                if str(id) not in self.m_config_parser.sections():
                    newid = str(id)
                    break
                id += 1
            atv.set_id(newid);
            
        newatv = Activity()
        newatv.set_id(atv.get_id())
        newatv.set_name(atv.get_name())
        newatv.set_info(atv.get_info())
        self.m_activities.append(newatv)

        self.m_config_parser[newid] = {}
        self.m_config_parser[newid]["name"] = atv.get_name()
        self.m_config_parser[newid]["info"] = atv.get_info()

        return True;

    def update_activity(self, atv):
        if not atv.is_complete():
            return False
        elif (self.m_config_parser.has_section(atv.get_id())):
            for existing_atv in self.m_activities:
                if existing_atv.get_id()== atv.get_id():
                    existing_atv.set_name(atv.get_name())
                    existing_atv.set_info(atv.get_info())
            self.m_config_parser[atv.get_id()]["name"] = atv.get_name()
            self.m_config_parser[atv.get_id()]["info"] = atv.get_info()
            return True
        else :
            return False
        
    def delete_activity_by_id(self, id):
        for i in range(len(self.m_activities)):
            if self.m_activities[i].get_id()==id:
                self.m_activities.remove(self.m_activities[i])
                break
        self.m_config_parser.remove_section(id)
