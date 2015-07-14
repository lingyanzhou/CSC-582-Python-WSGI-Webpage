from . import command
from .command import Command
from . import ranch
from .ranch import Ranch
from . import ranchdataaccess
from .ranchdataaccess import RanchDataAccess
class UpdateRanchCommand(Command):
    def __init__(self, rda):
        Command.__init__(self)
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
