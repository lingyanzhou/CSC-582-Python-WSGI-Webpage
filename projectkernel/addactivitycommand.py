from . import command
from .command import Command
from . import activity
from .activity import Activity
from . import activitydataaccess
from .activitydataaccess import ActivityDataAccess
class AddActivityCommand(Command):
    def __init__(self, ada):
        Command.__init__(self)
        self.m_ada = ada

    def get_name(self):
        return "Add an activity"
    
    def run(self):
        try :
            a = Activity()
            a.set_id("0")
            a.set_name(input("Name:"))
            a.set_info(input("Info:"))
            self.m_ada.add_activity(a)
        except EOFError:
            print("Action canceled")
