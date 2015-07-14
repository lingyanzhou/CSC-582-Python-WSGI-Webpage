from . import command
from .command import Command
from . import room
from .room import Room
from . import roomdataaccess
from .roomdataaccess import RoomDataAccess
class UpdateRoomCommand(Command):
    def __init__(self, rda):
        Command.__init__(self)
        self.m_rda = rda

    def get_name(self):
        return "Update a room"
    
    def run(self):
        try :
            r = Room()
            r.set_id(input("Update the activity with this id:"))
            r.set_name(input("name:"))
            r.set_info(input("Info:"))
            self.m_rda.update(r)
        except EOFError:
            print("Action canceled")
