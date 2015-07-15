"""
 @author Lingyan Zhou
"""

class Payment:
    """
    Payment class
    """
    def __init__(self):
        """
        Constructor.
        """
        self.m_id = None
        self.m_user_id = None
        self.m_is_pending = None
        self.m_amount = None

    def set_id(self, value):
        self.m_id = value

    def get_id(self):
        return self.m_id

    def set_user_id(self, value):
        self.m_user_id = value

    def get_user_id(self):
        return self.m_user_id

    def set_is_pending(self, value):
        self.m_is_pending = value

    def is_pending(self):
        return self.m_is_pending

    def set_amount(self, amount):
        self.m_amount = amount

    def get_amount(self):
        return self.m_amount

    def is_complete(self):
        return (self.m_id != None
                and self.m_user_id != None
                and self.m_is_pending != None
                and self.m_amount != None)
