from . import command
from .command import Command
from . import activity
from .activity import Activity
from . import activitydataaccess
from .activitydataaccess import ActivityDataAccess
class ListActivitiesCommand(Command):
    def __init__(self, ada):
        Command.__init__(self)
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
