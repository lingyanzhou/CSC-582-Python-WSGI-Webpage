from . import command
from .command import Command
from . import room
from .room import Room
from . import roomdataaccess
from .roomdataaccess import RoomDataAccess
class AddRoomCommand(Command):
    def __init__(self, ada):
        Command.__init__(self)
        self.m_ada = ada

    def get_name(self):
        return "Add a room"
    
    def run(self):
        try :
            r = Room()
            r.set_id("0")
            r.set_name(input("name:"))
            r.set_info(input("info:"))
            self.m_ada.add(r)
        except EOFError:
            print("Action canceled")
