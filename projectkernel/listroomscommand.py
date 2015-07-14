from . import command
from .command import Command
from . import room
from .room import Room
from . import roomdataaccess
from .roomdataaccess import RoomDataAccess
class ListRoomsCommand(Command):
    def __init__(self, rda):
        Command.__init__(self)
        self.m_rda = rda

    def get_name(self):
        return "List rooms"
    
    def run(self):
        rlist = self.m_rda.list_all()
        for r in rlist:
            print("=========================")
            print("id:", r.get_id())
            print("name:", r.get_name())
            print("info:", r.get_info())
