from . import command
from .command import Command
from . import travelarrangement
from .travelarrangement import TravelArrangement
from . import travelarrangementdataaccess
from .travelarrangementdataaccess import TravelArrangementDataAccess
class DeleteTravelArrangementCommand(Command):
    def __init__(self, tada):
        Command.__init__(self)
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
