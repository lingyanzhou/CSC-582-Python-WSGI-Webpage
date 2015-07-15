from .abstractcommand import AbstractCommand
from ..datastructure import Room
from ..dataaccess import RoomDataAccess
class ListRoomsCommand(AbstractCommand):
    def __init__(self, rda):
        AbstractCommand.__init__(self)
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

    def require_login(self):
        return False
    def require_admin(self):
        return False
