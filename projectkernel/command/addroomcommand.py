from .abstractcommand import AbstractCommand
from ..datastructure import Room
from ..dataaccess import RoomDataAccess
class AddRoomCommand(AbstractCommand):
    def __init__(self, ada):
        AbstractCommand.__init__(self)
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
    def require_login(self):
        return True
    def require_admin(self):
        return True
