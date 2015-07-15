from .abstractcommand import AbstractCommand
from ..datastructure import ActivityReservation
from ..dataaccess import ActivityReservationDataAccess
class MakeActivityReservationCommand(AbstractCommand):
    def __init__(self, arda):
        AbstractCommand.__init__(self)
        self.m_arda = arda

    def get_name(self):
        return "Make an activity reservation"
    
    def run(self):
        try :
            r = ActivityReservation()
            r.set_id("0")
            r.set_user_id(input("User ID:"))
            roomid = input("Activity ID:")
            r.set_activity_id(roomid)
            year = int(input("start year:"))
            month = int(input("start month:"))
            day = int(input("start day:"))
            hour = int(input("start hour:"))
            r.set_start_time(year, month, day, hour)
            year = int(input("end year:"))
            month = int(input("end month:"))
            day = int(input("end day:"))
            hour = int(input("end hour:"))
            r.set_end_time(year, month, day, hour)
            self.m_arda.add_reservation(r)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
    def require_login(self):
        return True
    def require_admin(self):
        return  True
