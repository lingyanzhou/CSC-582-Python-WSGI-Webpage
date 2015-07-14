from . import command
from .command import Command
from . import activity
from .activity import Activity
from . import activitydataaccess
from .activitydataaccess import ActivityDataAccess
class DeleteActivityCommand(Command):
    def __init__(self, ada):
        Command.__init__(self)
        self.m_ada = ada

    def get_name(self):
        return "Delete an activity"
    
    def run(self):
        try :
            id = input("Delete the activity with this id:")
            self.m_ada.delete_activity_by_id(id)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
