"""
 @author Lingyan Zhou
"""

class Activity:
    """
    Activity class
    """
    def __init__(self):
        """
        Constructor.
        """
        self.m_id = None
        self.m_name = None
        self.m_info = None

    def set_id(self, value):
        self.m_id = value

    def get_id(self):
        return self.m_id

    def set_name(self, value):
        self.m_name = value

    def get_name(self):
        return self.m_name

    def set_info(self, info):
        self.m_info = info

    def get_info(self):
        return self.m_info

    def is_complete(self):
        return (self.m_id != None
                and self.m_info != None
                and self.m_name != None)
