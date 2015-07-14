"""
 @author Lingyan Zhou
"""

class User:
    """
    Activity class
    """
    def __init__(self):
        """
        Constructor.
        """
        self.m_id = None
        self.m_is_admin  = None
        self.m_name = None
        self.m_password = None

    def set_id(self, value):
        self.m_id = value

    def get_id(self):
        return self.m_id

    def set_is_admin(self, value):
        self.m_is_admin = value

    def is_admin(self):
        return self.m_is_admin

    def set_name(self, value):
        self.m_name = value

    def get_name(self):
        return self.m_name

    def set_password(self, password):
        self.m_password = password

    def get_password(self):
        return self.m_password

    def is_complete(self):
        return (self.m_id != None
                and self.m_password != None
                and self.m_is_admin !=None
                and self.m_name != None)
