from .abstractcommand import AbstractCommand
from ..datastructure import User
from ..dataaccess import UserDataAccess
from hashlib import md5
class LoginCommand(AbstractCommand):
    def __init__(self, uda, appUser):
        AbstractCommand.__init__(self)
        self.m_uda = uda
        self.m_app_user = appUser

    def get_name(self):
        return "Login"
    
    def run(self):
        user = None
        id = input("id:")
        passwd = input("password:")
        passwd = passwd.encode("ascii", "ignore")
        passwd = md5(passwd).hexdigest()
        user = self.m_uda.find_match(id, passwd)
        if (None!= user):
            self.m_app_user.set_from_user(user)
            print("Login successful")
        else:
            print("Login failed")

    def require_login(self):
        return False
    def require_admin(self):
        return  False
    def is_appuser_accepted(self, appUser):
        if appUser.has_logged_in():
            return False
        else: 
            return True
