from .abstractcommand import AbstractCommand
from ..datastructure import RoomReservation
from ..dataaccess import RoomReservationDataAccess
class ListRoomReservationsCommand(AbstractCommand):
    def __init__(self, rrda):
        AbstractCommand.__init__(self)
        self.m_rrda = rrda

    def get_name(self):
        return "List room reservations"
    
    def run(self):
        rrlist = self.m_rrda.list_all_reservations()
        for rr in rrlist:
            print("=========================")
            print("id:", rr.get_id())
            print("user id:", rr.get_user_id())
            print("room id:", rr.get_reserved_room_id())
            print("start time:", rr.get_start_time_as_str())
            print("end time:", rr.get_end_time_as_str())
    def require_login(self):
        return True
    def require_admin(self):
        return  True
