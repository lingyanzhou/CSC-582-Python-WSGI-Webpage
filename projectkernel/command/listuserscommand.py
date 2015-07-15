from .abstractcommand import AbstractCommand
from ..datastructure import User
from ..dataaccess import UserDataAccess
class ListUsersCommand(AbstractCommand):
    def __init__(self, uda):
        AbstractCommand.__init__(self)
        self.m_uda = uda

    def get_name(self):
        return "List users"
    
    def run(self):
        ulist = self.m_uda.list_all()
        for u in ulist:
            print("=========================")
            print("id:", u.get_id())
            print("name:", u.get_name())
            print("is admin:", u.is_admin())
            print("password:", u.get_password())
    def require_login(self):
        return True
    def require_admin(self):
        return  True
