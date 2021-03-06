"""
 @author Lingyan Zhou
"""

import datetime

class ActivityReservation:
    """
    ActivityReservation class
    """
    def __init__(self):
        """
        Constructor.
        """
        self.m_id = None
        self.m_user_id = None
        self.m_start_time = None
        self.m_end_time = None
        self.m_activity_id = None

    def set_id(self, value):
        self.m_id = value

    def get_id(self):
        return self.m_id

    def set_start_time(self, year, month,  day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None):
        self.m_start_time = datetime.datetime(year, month, day, hour, minute, second, microsecond, tzinfo)

    def set_end_time(self, year, month,  day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None):
        self.m_end_time = datetime.datetime(year, month, day, hour, minute, second, microsecond, tzinfo)

    def set_start_time_by_str(self, date_string, format=None):
        if format==None:
            format = "%x %X"
        self.m_start_time = datetime.datetime.strptime(date_string, format)

    def set_end_time_by_str(self, date_string, format=None):
        if format==None:
            format = "%x %X"
        self.m_end_time = datetime.datetime.strptime(date_string, format)

    def set_end_time_by_offset(self, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
        td = datetime.timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks)
        self.m_end_time = m_start_time + td

    def set_user_id(self, id):
        self.m_user_id = id

    def set_activity_id(self, id):
        self.m_activity_id = id

    def get_start_time(self):
        return self.m_start_time

    def get_start_time_as_str(self, format=None):
        if format==None:
            format = "%x %X"
        return self.m_start_time.strftime(format)

    def get_end_time(self):
        return self.m_end_time

    def get_end_time_as_str(self, format=None):
        if format==None:
            format = "%x %X"
        return self.m_end_time.strftime(format)

    def get_user_id(self):
        return self.m_user_id

    def get_activity_id(self):
        return self.m_activity_id

    def is_reservation_complete(self):
        return (self.m_end_time != None
                and self.m_start_time != None
                and self.m_user_id != None
                and self.m_activity_id != None)

    def is_reservation_time_valid(self):
        if (None == self.m_end_time 
                or None==self.m_start_time):
            return false;
        td = self.m_end_time - self.m_start_time
        return td.total_seconds() > 0

    def has_expired(self):
        td = self.m_end_time - datetime.datetime.today()
        return td.total_seconds() <= 0

    def conflict_with(self, reserv):
        if (self.m_user_id == reserv.m_user_id
                or self.m_activity_id == reserv.m_activity_id):
            if self.m_start_time >= reserv.m_end_time:
                return False
            if self.m_end_time <= reserv.m_start_time:
                return False
            return True
        else:
            return False
