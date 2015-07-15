from .abstractcommand import AbstractCommand
from ..datastructure import User
from ..dataaccess import UserDataAccess
class DeleteUserCommand(AbstractCommand):
    def __init__(self, uda):
        AbstractCommand.__init__(self)
        self.m_uda = uda

    def get_name(self):
        return "Delete a user"
    
    def run(self):
        id = input("Delete the user with this id:")
        self.m_uda.delete_by_id(id)
        
    def require_login(self):
        return True
    def require_admin(self):
        return  True
