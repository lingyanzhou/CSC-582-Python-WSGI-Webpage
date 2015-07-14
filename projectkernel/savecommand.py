from . import command
from .command import Command

class SaveCommand(Command):
    def __init__(self, rrda, cda, rda, ada, arda, dda, pda, tada):
        Command.__init__(self)
        self.m_rrda = rrda
        self.m_cda = cda
        self.m_ada = ada
        self.m_rda = rda
        self.m_arda = arda
        self.m_dda = dda
        self.m_pda = pda
        self.m_tada = tada

    def get_name(self):
        return "Save"

    def run(self):
        self.m_rrda.save()
        self.m_cda.save()
        self.m_rda.save()
        self.m_ada.save()
        self.m_arda.save()
        self.m_dda.save()
        self.m_pda.save()
        self.m_tada.save()
