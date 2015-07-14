from . import command
from .command import Command
from . import activity
from .activity import Activity
from . import activitydataaccess
from .activitydataaccess import ActivityDataAccess
class UpdateActivityCommand(Command):
    def __init__(self, ada):
        Command.__init__(self)
        self.m_ada = ada

    def get_name(self):
        return "Update an activity"
    
    def run(self):
        try :
            a = Activity()
            a.set_id(input("Update the activity with this id:"))
            a.set_name(input("name:"))
            a.set_info(input("Info:"))
            self.m_ada.update_activity(a)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
