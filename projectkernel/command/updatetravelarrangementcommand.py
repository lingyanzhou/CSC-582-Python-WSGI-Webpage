from .abstractcommand import AbstractCommand
from ..datastructure import TravelArrangement
from ..dataaccess import TravelArrangementDataAccess
class UpdateTravelArrangementCommand(AbstractCommand):
    def __init__(self, tada):
        AbstractCommand.__init__(self)
        self.m_tada = tada

    def get_name(self):
        return "Update a travel arrangement"
    
    def run(self):
        try :
            ta = TravelArrangement()
            ta.set_id(input("Update the travel arrangement with this id:"))
            ta.set_name(input("name:"))
            ta.set_description(input("description:"))
            self.m_tada.update(ta)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
    def require_login(self):
        return True
    def require_admin(self):
        return  True
