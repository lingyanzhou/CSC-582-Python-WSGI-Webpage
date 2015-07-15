from .abstractcommand import AbstractCommand
from ..datastructure import Activity
from ..dataaccess import ActivityDataAccess
class ListActivitiesCommand(AbstractCommand):
    def __init__(self, ada):
        AbstractCommand.__init__(self)
        self.m_ada = ada

    def get_name(self):
        return "List activities"
    
    def run(self):
        alist = self.m_ada.list_all_activities()
        for a in alist:
            print("=========================")
            print("id:", a.get_id())
            print("name:", a.get_name())
            print("info:", a.get_info())
    def require_login(self):
        return False
    def require_admin(self):
        return False
