from .abstractcommand import AbstractCommand
from ..datastructure import Directions
from ..dataaccess import DirectionsDataAccess
class ListDirectionsCommand(AbstractCommand):
    def __init__(self, dda):
        AbstractCommand.__init__(self)
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

    def require_login(self):
        return False
    def require_admin(self):
        return False
