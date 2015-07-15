from .abstractcommand import AbstractCommand
from ..datastructure import Ranch
from ..dataaccess import RanchDataAccess
class PrintRanchCommand(AbstractCommand):
    def __init__(self, rda):
        AbstractCommand.__init__(self)
        self.m_rda = rda

    def get_name(self):
        return "Print ranch"
    
    def run(self):
        r = self.m_rda.get()
        if not None == r:
            print("=========================")
            print("name:", r.get_name())
            print("location:", r.get_location())
            print("description:", r.get_description())
    def require_login(self):
        return False 
    def require_admin(self):
        return False
