from .abstractcommand import AbstractCommand
from ..datastructure import Activity
from ..dataaccess import ActivityDataAccess
class DeleteActivityCommand(AbstractCommand):
    def __init__(self, ada):
        AbstractCommand.__init__(self)
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
            
    def require_login(self):
        return True
    def require_admin(self):
        return True
