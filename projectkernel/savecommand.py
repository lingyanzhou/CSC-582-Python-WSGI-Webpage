from . import command
from .command import Command

class SaveCommand(Command):
    def __init__(self):
        Command.__init__(self)
        self.m_dataaccesses = []

    def get_name(self):
        return "Save"

    def attach_dataaccess(self, da):
        self.m_dataaccesses.append(da)
        
    def run(self):
        for da in self.m_dataaccesses:
            da.save()
