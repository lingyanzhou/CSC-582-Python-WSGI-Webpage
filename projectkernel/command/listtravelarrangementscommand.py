from .abstractcommand import AbstractCommand
from ..datastructure import TravelArrangement
from ..dataaccess import TravelArrangementDataAccess
class ListTravelArrangementsCommand(AbstractCommand):
    def __init__(self, tada):
        AbstractCommand.__init__(self)
        self.m_tada = tada

    def get_name(self):
        return "List travel arrangements"
    
    def run(self):
        talist = self.m_tada.list_all()
        for ta in talist:
            print("=========================")
            print("id:", ta.get_id())
            print("name:", ta.get_name())
            print("description:", ta.get_description())
    def require_login(self):
        return False
    def require_admin(self):
        return False 
