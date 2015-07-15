from .abstractcommand import AbstractCommand
from ..datastructure import RoomReservation
from ..dataaccess import RoomReservationDataAccess
class GuestMakeRoomReservationCommand(AbstractCommand):
    def __init__(self, rrda, appUser):
        AbstractCommand.__init__(self)
        self.m_rrda = rrda
        self.m_AppUser = appUser

    def get_name(self):
        return "Make a room reservation"
    
    def run(self):
        if not self.m_AppUser.has_logged_in():
            return

        try :
            r = RoomReservation()
            r.set_id("0")
            r.set_user_id(self.m_AppUser.get_id())
            roomid = input("Room ID:")
            r.set_reserved_room_id(roomid)
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
            self.m_rrda.add_reservation(r)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error") 
    def require_login(self):
        return True
    def require_admin(self):
        return False 
