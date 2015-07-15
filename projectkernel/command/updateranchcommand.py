from .abstractcommand import AbstractCommand
from ..datastructure import Ranch
from ..dataaccess import RanchDataAccess
class UpdateRanchCommand(AbstractCommand):
    def __init__(self, rda):
        AbstractCommand.__init__(self)
        self.m_rda = rda

    def get_name(self):
        return "Update a ranch"
    
    def run(self):
        try :
            r = Ranch()
            r.set_name(input("name:"))
            r.set_location(input("location:"))
            r.set_description(input("description:"))
            self.m_rda.update(r)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
    def require_login(self):
        return True
    def require_admin(self):
        return  True
