from . import command
from .command import Command
from . import travelarrangement
from .travelarrangement import TravelArrangement
from . import travelarrangementdataaccess
from .travelarrangementdataaccess import TravelArrangementDataAccess
class UpdateTravelArrangementCommand(Command):
    def __init__(self, tada):
        Command.__init__(self)
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
