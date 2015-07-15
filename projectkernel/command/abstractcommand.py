from ..appstatus import appuser

class AbstractCommand:
    def __init__(self):
        pass
    def run(self):
        pass
    def get_name(self):
        pass
    def require_login(self):
        pass
    def require_admin(self):
        pass
    def is_appuser_accepted(self, appUser):
        if (not appUser.has_logged_in()
                and not self.require_login()):
            return True
        elif (appUser.has_logged_in()
                and not appUser.is_admin()
                and not self.require_admin()):
            return True
        elif (appUser.has_logged_in()
                and appUser.is_admin()):
            return True
        else:
            return False
