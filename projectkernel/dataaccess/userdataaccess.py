"""
 @author Lingyan Zhou
"""
from ..datastructure import User

from .basedataaccess import BaseDataAccess

import configparser

class UserDataAccess(BaseDataAccess):
    def __init__(self, filename):
        BaseDataAccess.__init__(self)
        self.m_config_parser = configparser.ConfigParser()
        self.m_config_file_name = filename;
        self.m_users = []

    def load(self):
        self.m_config_parser.read(self.m_config_file_name)
        self.m_users = list()
        for id in self.m_config_parser.sections():
            c = User()
            c.set_id(id)
            c.set_name(self.m_config_parser[id]["name"])
            c.set_is_admin("True"==self.m_config_parser[id]["is admin"])
            c.set_password(self.m_config_parser[id]["password"])
            self.m_users.append(c)

    def save(self):
        with open(self.m_config_file_name, 'wt') as f:
            self.m_config_parser.write(f);

    def find_match(self, id, password):
        for user in self.m_users:
            if (user.get_id()==id
                    and user.get_password()==password):
                return user
        return None

    def list_all(self):
        return list(self.m_users)

    def add(self, usr):
        if not usr.is_complete():
            return False
        
        for existing_usr in self.m_users:
            if usr is existing_usr:
                return False

        newid = usr.get_id();
        if newid!=None and newid not in self.m_config_parser.sections():
            pass
        else :
            id = 0;
            while True:
                if str(id) not in self.m_config_parser.sections():
                    newid = str(id)
                    break
                id += 1
            usr.set_id(newid);
            
        newusr = User()
        newusr.set_id(usr.get_id())
        newusr.set_name(usr.get_name())
        newusr.set_is_admin(usr.is_admin())
        newusr.set_password(usr.get_password())
        self.m_users.append(newusr)

        self.m_config_parser[newid] = {}
        self.m_config_parser[newid]["name"] = usr.get_name()
        self.m_config_parser[usr.get_id()]["is admin"] = str(usr.is_admin())
        self.m_config_parser[usr.get_id()]["password"] = usr.get_password()

        return True;

    def update(self, usr):
        if not usr.is_complete():
            return False
        elif (self.m_config_parser.has_section(usr.get_id())):
            for existing_usr in self.m_users:
                if existing_usr.get_id()== usr.get_id():
                    existing_usr.set_name(usr.get_name())
                    existing_usr.set_is_admin(usr.is_admin())
                    existing_usr.set_password(usr.get_password())
            self.m_config_parser[usr.get_id()]["name"] = usr.get_name()
            self.m_config_parser[usr.get_id()]["is admin"] = str(usr.is_admin())
            self.m_config_parser[usr.get_id()]["password"] = usr.get_password()
            return True
        else :
            return False
        
    def delete_by_id(self, id):
        for i in range(len(self.m_users)):
            if self.m_users[i].get_id()==id:
                self.m_users.remove(self.m_users[i])
                break
        self.m_config_parser.remove_section(id)
