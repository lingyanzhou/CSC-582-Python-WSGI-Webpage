from . import command
from .command import Command
from . import activity
from .activity import Activity
from . import activityreservationdataaccess
from .activityreservationdataaccess import ActivityReservationDataAccess
class ListActivityReservationsCommand(Command):
    def __init__(self, arda):
        Command.__init__(self)
        self.m_arda = arda

    def get_name(self):
        return "List activity reservations"
    
    def run(self):
        arlist = self.m_arda.list_all_reservations()
        for ar in arlist:
            print("=========================")
            print("id:", ar.get_id())
            print("reserver:", ar.get_reserver_name())
            print("activity id:", ar.get_activity_id())
            print("start time:", ar.get_start_time_as_str())
            print("end time:", ar.get_end_time_as_str())
