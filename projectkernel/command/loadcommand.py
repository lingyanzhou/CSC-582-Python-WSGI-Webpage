from .abstractcommand import AbstractCommand
from ..dataaccess import BaseDataAccess

class LoadCommand(AbstractCommand):
    def __init__(self):
        AbstractCommand.__init__(self)
        self.m_dataaccesses = []

    def get_name(self):
        return "Load"

    def attach_dataaccess(self, da):
        self.m_dataaccesses.append(da)

    def run(self):
        for da in self.m_dataaccesses:
            da.load()
    def require_login(self):
        return False 
    def require_admin(self):
        return False
