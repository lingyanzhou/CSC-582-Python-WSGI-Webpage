from . import command
from .command import Command
from . import activityreservation
from .activityreservation import ActivityReservation
from . import activityreservationdataaccess
from .activityreservationdataaccess import ActivityReservationDataAccess
class DeleteActivityReservationCommand(Command):
    def __init__(self, arda):
        Command.__init__(self)
        self.m_arda = arda

    def get_name(self):
        return "Delete an activity reservation"
    
    def run(self):
        try :
            id = input("Update the reservation with this id:")
            self.m_arda.delete_reservation_by_id(id)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
