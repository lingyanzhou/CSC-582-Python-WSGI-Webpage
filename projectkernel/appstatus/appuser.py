"""
 @author Lingyan Zhou
"""
from ..datastructure import User

class AppUser:
    """
    """
    def __init__(self):
        """
        Constructor.
        """
        self.m_id = None
        self.m_is_admin  = False
        self.m_name = "Guest"

    def set_from_user(self, user):
        self.m_id = user.get_id()
        self.m_is_admin = user.is_admin()
        self.m_name = user.get_name()

    def has_logged_in(self):
        return None!=self.m_id

    def logout(self):
        self.m_id = None
        self.m_is_admin  = False
        self.m_name = "Guest"

    def get_id(self):
        return self.m_id

    def is_admin(self):
        return self.m_is_admin

    def get_name(self):
        return self.m_name

