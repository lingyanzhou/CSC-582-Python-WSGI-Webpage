from .abstractcommand import AbstractCommand
from ..datastructure import ActivityReservation
from ..dataaccess import ActivityReservationDataAccess
class UpdateActivityReservationCommand(AbstractCommand):
    def __init__(self, arda):
        AbstractCommand.__init__(self)
        self.m_arda = arda

    def get_name(self):
        return "Update an activity reservation"
    
    def run(self):
        try :
            r = ActivityReservation()
            id = input("Update the reservation with this id:")
            r.set_id(id)
            uid = input("User ID:")
            r.set_user_id(uid)
            activityid = input("Activity ID:")
            r.set_activity_id(activityid)
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
            self.m_arda.update_reservation(r)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
    def require_login(self):
        return True
    def require_admin(self):
        return  True
