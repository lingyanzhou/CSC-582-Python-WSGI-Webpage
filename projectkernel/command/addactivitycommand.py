from .abstractcommand import AbstractCommand
from ..datastructure import Activity
from ..dataaccess import ActivityDataAccess
class AddActivityCommand(AbstractCommand):
    def __init__(self, ada):
        AbstractCommand.__init__(self)
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
    def require_login(self):
        return True
    def require_admin(self):
        return  True
