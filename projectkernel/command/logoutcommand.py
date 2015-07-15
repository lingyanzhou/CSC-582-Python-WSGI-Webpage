from .abstractcommand import AbstractCommand
from ..datastructure import User
from ..dataaccess import UserDataAccess
class LogoutCommand(AbstractCommand):
    def __init__(self, appUser):
        AbstractCommand.__init__(self)
        self.m_app_user = appUser

    def get_name(self):
        return "Logout"
    
    def run(self):
        self.m_app_user.logout()

    def require_login(self):
        return True
    def require_admin(self):
        return  False
