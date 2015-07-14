from . import command
from .command import Command
from . import roomreservation
from .roomreservation import RoomReservation
from . import roomreservationdataaccess
from .roomreservationdataaccess import RoomReservationDataAccess
class ListRoomReservationsCommand(Command):
    def __init__(self, rrda):
        Command.__init__(self)
        self.m_rrda = rrda

    def get_name(self):
        return "List room reservations"
    
    def run(self):
        rrlist = self.m_rrda.list_all_reservations()
        for rr in rrlist:
            print("=========================")
            print("id:", rr.get_id())
            print("reserver:", rr.get_reserver_name())
            print("room id:", rr.get_reserved_room_id())
            print("start time:", rr.get_start_time_as_str())
            print("end time:", rr.get_end_time_as_str())
