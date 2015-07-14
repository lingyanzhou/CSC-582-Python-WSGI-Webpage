from . import command
from .command import Command
from . import roomreservation
from .roomreservation import RoomReservation
from . import roomreservationdataaccess
from .roomreservationdataaccess import RoomReservationDataAccess
class DeleteRoomReservationCommand(Command):
    def __init__(self, rrda):
        Command.__init__(self)
        self.m_rrda = rrda

    def get_name(self):
        return "Delete a room reservation"
    
    def run(self):
        try :
            id = input("Delete the reservation with this id:")
            self.m_rrda.delete_reservation_by_id(id)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
