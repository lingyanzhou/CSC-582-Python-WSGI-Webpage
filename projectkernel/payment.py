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
        self.m_amount = None

    def set_id(self, value):
        self.m_id = value

    def get_id(self):
        return self.m_id

    def set_amount(self, amount):
        self.m_amount = amount

    def get_amount(self):
        return self.m_amount

    def is_complete(self):
        return (self.m_id != None
                and self.m_amount != None)
