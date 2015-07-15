from .abstractcommand import AbstractCommand
from ..datastructure import User
from ..dataaccess import UserDataAccess
class PrintCurrentUserCommand(AbstractCommand):
    def __init__(self, appUser):
        AbstractCommand.__init__(self)
        self.m_app_user = appUser

    def get_name(self):
        return "Print current user"
    
    def run(self):
        print("===========================")
        print("id: ", self.m_app_user.get_id())
        print("name: ", self.m_app_user.get_name())
        print("logged in: ", self.m_app_user.has_logged_in())
        print("is admin: ", self.m_app_user.is_admin())

    def require_login(self):
        return False
    def require_admin(self):
        return  False
