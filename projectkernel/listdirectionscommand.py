from . import command
from .command import Command
from . import directions
from .directions import Directions
from . import directionsdataaccess
from .directionsdataaccess import DirectionsDataAccess
class ListDirectionsCommand(Command):
    def __init__(self, dda):
        Command.__init__(self)
        self.m_dda = dda

    def get_name(self):
        return "List directions"
    
    def run(self):
        d = self.m_dda.get()
        if not None == d:
            locList = d.get_locations()
            for loc in locList:
                print("=========================")
                for loc2 in locList:
                    print("{0:s}-{1:s}: {2:s}".format(loc, loc2,d.get_direction(loc, loc2)))
