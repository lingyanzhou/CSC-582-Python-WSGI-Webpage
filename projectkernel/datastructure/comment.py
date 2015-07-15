"""
 @author Lingyan Zhou
"""

import datetime

class Comment:
    """
    Reservation class
    """
    def __init__(self):
        """
        Constructor.
        """
        self.m_id = None
        self.m_user_id = None
        self.m_time = None
        self.m_message = None

    def set_id(self, value):
        self.m_id = value

    def get_id(self):
        return self.m_id

    def set_time(self, year, month,  day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None):
        self.m_time = datetime.datetime(year, month, day, hour, minute, second, microsecond, tzinfo)

    def set_time_by_str(self, date_string, format=None):
        if format==None:
            format = "%x %X"
        self.m_time = datetime.datetime.strptime(date_string, format)
        
    def set_time_now(self):
        self.m_time = datetime.datetime.today()

    def set_user_id(self, id):
        self.m_user_id = id

    def set_message(self, message):
        self.m_message = message

    def get_time(self):
        return self.m_time

    def get_time_as_str(self, format=None):
        if format==None:
            format = "%x %X"
        return self.m_time.strftime(format)

    def get_user_id(self):
        return self.m_user_id

    def get_message(self):
        return self.m_message

    def is_complete(self):
        return (self.m_id != None
                and self.m_user_id != None
                and self.m_time != None
                and self.m_message != None)
