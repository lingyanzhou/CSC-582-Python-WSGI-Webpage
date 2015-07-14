from . import command
from .command import Command

class SubAppCommand(Command):
    def __init__(self, subapp, name):
        Command.__init__(self)
        self.m_subapp = subapp
        self.m_name = name

    def get_name(self):
        return self.m_name

    def run(self):
        self.m_subapp.run()
