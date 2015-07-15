from .abstractcommand import AbstractCommand
from ..datastructure import RoomReservation
from ..dataaccess import RoomReservationDataAccess
class DeleteRoomReservationCommand(AbstractCommand):
    def __init__(self, rrda):
        AbstractCommand.__init__(self)
        self.m_rrda = rrda

    def get_name(self):
        return "Delete a room reservation"
    
    def run(self):
        try :
            id = input("Delete the room reservation with this id:")
            self.m_rrda.delete_reservation_by_id(id)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
    def require_login(self):
        return True
    def require_admin(self):
        return  True
