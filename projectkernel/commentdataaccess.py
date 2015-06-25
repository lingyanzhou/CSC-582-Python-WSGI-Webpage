"""
 @author Lingyan Zhou
"""
from . import comment

import configparser

class CommentDataAccess:
    def __init__(self, filename):
        self.m_config_parser = configparser.ConfigParser()
        self.m_config_file_name = filename;
        self.m_comments = []

    def load(self):
        self.m_config_parser.read(self.m_config_file_name)
        self.m_comments = list()
        for id in self.m_config_parser.sections():
            c = comment.Comment()
            c.set_id(id)
            c.set_time_by_str(self.m_config_parser[id]["time"])
            c.set_user_name(self.m_config_parser[id]["user"])
            c.set_message(self.m_config_parser[id]["message"])
            self.m_comments.append(c)

    def save(self):
        with open(self.m_config_file_name, 'wt') as f:
            self.m_config_parser.write(f);

    def list_all_comments(self):
        return list(self.m_comments)

    def list_comments_by_user(self, name):
        l = list()
        for cmt in self.m_comments:
            if cmt.get_resever_name() == name:
                l.append(cmt)
        return l

    def add_comment(self, cmt):
        if not cmt.is_complete():
            return False
        
        for existing_cmt in self.m_comments:
            if cmt is existing_cmt:
                return False

        newid = cmt.get_id();
        if newid!=None and newid not in self.m_config_parser.sections():
            pass
        else :
            id = 0;
            while True:
                if str(id) not in self.m_config_parser.sections():
                    newid = str(id)
                    break
                id += 1
            cmt.set_id(newid);
            
        newcmt = comment.Comment()
        newcmt.set_id(cmt.get_id())
        newcmt.set_time_by_str(cmt.get_time_as_str())
        newcmt.set_user_name(cmt.get_user_name())
        newcmt.set_message(cmt.get_message())
        self.m_comments.append(newcmt)

        self.m_config_parser[newid] = {}
        self.m_config_parser[newid]["time"] = cmt.get_time_as_str()
        self.m_config_parser[newid]["user"] = cmt.get_user_name()
        self.m_config_parser[newid]["message"] = cmt.get_message()

        return True;

    def update_comment(self, cmt):
        if (self.m_config_parser.has_section(cmt.get_id())):
            for existing_cmt in self.m_comments:
                if existing_cmt.get_id()== cmt.get_id():
                    existing_cmt.set_time_by_str(cmt.get_time_as_str())
                    existing_cmt.set_user_name(cmt.get_user_name())
                    existing_cmt.set_message(cmt.get_message())
            self.m_config_parser[cmt.get_id()]["time"] = cmt.get_time_as_str()
            self.m_config_parser[cmt.get_id()]["user"] = cmt.get_user_name()
            self.m_config_parser[cmt.get_id()]["message"] = cmt.get_message()
            return True
        else :
            return False
        
    def delete_comment_by_id(self, id):
        for i in range(len(self.m_comments)):
            if self.m_comments[i].get_id()==id:
                self.m_comments.remove(self.m_comments[i])
                break
        self.m_config_parser.remove_section(id)
