from . import command
from .command import Command
from . import travelarrangement
from .travelarrangement import TravelArrangement
from . import travelarrangementdataaccess
from .travelarrangementdataaccess import TravelArrangementDataAccess
class ListTravelArrangementsCommand(Command):
    def __init__(self, tada):
        Command.__init__(self)
        self.m_tada = tada

    def get_name(self):
        return "List travel arrangements"
    
    def run(self):
        talist = self.m_tada.list_all()
        for ta in talist:
            print("=========================")
            print("name:", ta.get_name())
            print("description:", ta.get_description())
