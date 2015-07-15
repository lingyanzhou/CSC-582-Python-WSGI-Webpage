from .abstractcommand import AbstractCommand
from ..datastructure import User
from ..dataaccess import UserDataAccess
from hashlib import md5
class AddUserCommand(AbstractCommand):
    def __init__(self, uda):
        AbstractCommand.__init__(self)
        self.m_uda = uda

    def get_name(self):
        return "Add a user"
    
    def run(self):
        u = User()
        u.set_id("0")
        u.set_name(input("name: "))
        u.set_is_admin(True==input("Is admin (True/False):"))
        u.set_password(md5(input("password:").encode("ascii", "ignore")).hexdigest())
        if self.m_uda.add(u):
            print("User " + u.get_id() + " added")
        
    def require_login(self):
        return True
    def require_admin(self):
        return  True
