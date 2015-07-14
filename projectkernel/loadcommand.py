from . import command
from .command import Command

class LoadCommand(Command):
    def __init__(self, rrda, cda, rda, ada, arda, dda, pda, tada):
        Command.__init__(self)
        self.m_rrda = rrda
        self.m_cda = cda
        self.m_rda = rda
        self.m_ada = ada
        self.m_arda = arda
        self.m_dda = dda
        self.m_pda = pda
        self.m_tada = tada

    def get_name(self):
        return "Load"

    def run(self):
        self.m_rrda.load()
        self.m_cda.load()
        self.m_rda.load()
        self.m_ada.load()
        self.m_arda.load()
        self.m_dda.load()
        self.m_pda.load()
        self.m_tada.load()
