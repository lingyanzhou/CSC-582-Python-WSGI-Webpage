from .abstractcommand import AbstractCommand
from ..datastructure import Activity
from ..dataaccess import ActivityDataAccess
class UpdateActivityCommand(AbstractCommand):
    def __init__(self, ada):
        AbstractCommand.__init__(self)
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
    def require_login(self):
        return True
    def require_admin(self):
        return True
