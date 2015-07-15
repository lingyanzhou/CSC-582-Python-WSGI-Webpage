"""
 @author Lingyan Zhou
"""
from ..datastructure import Room

from .basedataaccess import BaseDataAccess

import configparser

class RoomDataAccess(BaseDataAccess):
    def __init__(self, filename):
        BaseDataAccess.__init__(self)
        self.m_config_parser = configparser.ConfigParser()
        self.m_config_file_name = filename;
        self.m_rooms = []

    def load(self):
        self.m_config_parser.read(self.m_config_file_name)
        self.m_rooms = list()
        for id in self.m_config_parser.sections():
            c = Room()
            c.set_id(id)
            c.set_name(self.m_config_parser[id]["name"])
            c.set_info(self.m_config_parser[id]["info"])
            self.m_rooms.append(c)

    def save(self):
        with open(self.m_config_file_name, 'wt') as f:
            self.m_config_parser.write(f);

    def list_all(self):
        return list(self.m_rooms)

    def add(self, rm):
        if not rm.is_complete():
            return False
        
        for existing_room in self.m_rooms:
            if rm is existing_room:
                return False

        newid = rm.get_id();
        if newid!=None and newid not in self.m_config_parser.sections():
            pass
        else :
            id = 0;
            while True:
                if str(id) not in self.m_config_parser.sections():
                    newid = str(id)
                    break
                id += 1
            rm.set_id(newid);
            
        newroom = Room()
        newroom.set_id(rm.get_id())
        newroom.set_name(rm.get_name())
        newroom.set_info(rm.get_info())
        self.m_rooms.append(newroom)

        self.m_config_parser[newid] = {}
        self.m_config_parser[newid]["name"] = rm.get_name()
        self.m_config_parser[newid]["info"] = rm.get_info()

        return True;

    def update(self, rm):
        if not rm.is_complete():
            return False
        elif (self.m_config_parser.has_section(rm.get_id())):
            for existing_room in self.m_rooms:
                if existing_room.get_id()== rm.get_id():
                    existing_room.set_name(rm.get_name())
                    existing_room.set_info(rm.get_info())
            self.m_config_parser[rm.get_id()]["name"] = rm.get_name()
            self.m_config_parser[rm.get_id()]["info"] = rm.get_info()
            return True
        else :
            return False
        
    def delete_by_id(self, id):
        for i in range(len(self.m_rooms)):
            if self.m_rooms[i].get_id()==id:
                self.m_rooms.remove(self.m_rooms[i])
                break
        self.m_config_parser.remove_section(id)
