from .abstractcommand import AbstractCommand
from ..datastructure import Room
from ..dataaccess import RoomDataAccess
class DeleteRoomCommand(AbstractCommand):
    def __init__(self, rda):
        AbstractCommand.__init__(self)
        self.m_rda = rda

    def get_name(self):
        return "Delete a room"
    
    def run(self):
        try :
            id = input("Update the activity with this id:")
            self.m_rda.delete_by_id(id)
        except EOFError:
            print("Action canceled")
    def require_login(self):
        return True
    def require_admin(self):
        return  True
