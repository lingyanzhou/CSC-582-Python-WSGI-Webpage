from .abstractcommand import AbstractCommand
from ..datastructure import Room
from ..dataaccess import RoomDataAccess
class UpdateRoomCommand(AbstractCommand):
    def __init__(self, rda):
        AbstractCommand.__init__(self)
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
            
    def require_login(self):
        return True
    def require_admin(self):
        return True
