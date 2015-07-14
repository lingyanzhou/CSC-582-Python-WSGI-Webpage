from . import command
from .command import Command
from . import room
from .room import Room
from . import roomdataaccess
from .roomdataaccess import RoomDataAccess
class DeleteRoomCommand(Command):
    def __init__(self, rda):
        Command.__init__(self)
        self.m_rda = rda

    def get_name(self):
        return "Delete a room"
    
    def run(self):
        try :
            id = input("Update the activity with this id:")
            self.m_rda.delete_by_id(id)
        except EOFError:
            print("Action canceled")
