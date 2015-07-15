from .abstractcommand import AbstractCommand
from ..dataaccess import BaseDataAccess

class SaveCommand(AbstractCommand):
    def __init__(self):
        AbstractCommand.__init__(self)
        self.m_dataaccesses = []

    def get_name(self):
        return "Save"

    def attach_dataaccess(self, da):
        self.m_dataaccesses.append(da)
        
    def run(self):
        for da in self.m_dataaccesses:
            da.save()
    def require_login(self):
        return True
    def require_admin(self):
        return True
