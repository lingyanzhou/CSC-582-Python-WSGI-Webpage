from .abstractcommand import AbstractCommand
from ..datastructure import RoomReservation
from ..dataaccess import RoomReservationDataAccess
class MakeRoomReservationCommand(AbstractCommand):
    def __init__(self, rrda):
        AbstractCommand.__init__(self)
        self.m_rrda = rrda

    def get_name(self):
        return "Make a room reservation"
    
    def run(self):
        try :
            r = RoomReservation()
            r.set_id("0")
            r.set_user_id(input("User ID:"))
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
        return True 
