from .abstractcommand import AbstractCommand
from ..datastructure import TravelArrangement
from ..dataaccess import TravelArrangementDataAccess
class DeleteTravelArrangementCommand(AbstractCommand):
    def __init__(self, tada):
        AbstractCommand.__init__(self)
        self.m_tada = tada

    def get_name(self):
        return "Delete a travel arrangement"
    
    def run(self):
        try :
            id = input("Delete the travel arrangement with this id:")
            self.m_tada.delete_by_id(id)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
    def require_login(self):
        return True
    def require_admin(self):
        return  True
