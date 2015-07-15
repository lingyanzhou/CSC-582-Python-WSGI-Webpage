from .abstractcommand import AbstractCommand
from ..datastructure import ActivityReservation
from ..dataaccess import ActivityReservationDataAccess
class DeleteActivityReservationCommand(AbstractCommand):
    def __init__(self, arda):
        AbstractCommand.__init__(self)
        self.m_arda = arda

    def get_name(self):
        return "Delete an activity reservation"
    
    def run(self):
        try :
            id = input("Delete the activity with this id:")
            self.m_arda.delete_activity_by_id(id)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
    def require_login(self):
        return True
    def require_admin(self):
        return True
