from . import command
from .command import Command
from . import ranch
from .ranch import Ranch
from . import ranchdataaccess
from .ranchdataaccess import RanchDataAccess
class PrintRanchCommand(Command):
    def __init__(self, rda):
        Command.__init__(self)
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
