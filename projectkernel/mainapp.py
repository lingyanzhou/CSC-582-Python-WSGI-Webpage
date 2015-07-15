from .cliapp import CLIApp

from .command import LoadCommand

from .dataaccess import RoomDataAccess

from .dataaccess import RoomReservationDataAccess

from .dataaccess import CommentDataAccess

from .dataaccess import RanchDataAccess

from .dataaccess import ActivityDataAccess

from .dataaccess import ActivityReservationDataAccess

from .dataaccess import DirectionsDataAccess

from .dataaccess import PaymentDataAccess

from .dataaccess import TravelArrangementDataAccess

from .dataaccess import UserDataAccess

from .guestsubapp import GuestSubApp

from .adminsubapp import AdminSubApp

from .subappcommand import SubAppCommand

from .command import LoadCommand

from .command import LoginCommand

from .command import LogoutCommand

from .command import PrintCurrentUserCommand

from .appstatus import AppUser

class MainApp(CLIApp):
    def __init__(self, roomReservationDA = None, commentDA = None, ranchDA = None,
            roomDA = None, activityDA = None, activityReservationDA = None, directionDA = None,
            paymentDA = None, travelArrangementDA = None, userDA = None,
            appUser = None):
        CLIApp.__init__(self)
        if (None == roomReservationDA):
            self.m_RoomReservationDA = RoomReservationDataAccess("./data/RoomReservation.ini")
        else:
            self.m_RoomReservationDA = roomReservationDA
        if (None == commentDA):
            self.m_CommentDA = CommentDataAccess("./data/Comment.ini")
        else:
            self.m_CommentDA = commentDA
        if (None == ranchDA):
            self.m_RanchDA = RanchDataAccess("./data/Ranch.ini")
        else:
            self.m_RanchDA = ranchDA
        if (None == roomDA):
            self.m_RoomDA = RoomDataAccess("./data/Room.ini")
        else:
            self.m_RoomDA = roomDA
        if (None == activityDA):
            self.m_ActivityDA = ActivityDataAccess("./data/Activity.ini")
        else:
            self.m_ActivityDA = activityDA
        if (None == activityReservationDA):
            self.m_ActivityReservationDA = ActivityReservationDataAccess("./data/ActivityReservation.ini")
        else:
            self.m_ActivityReservationDA = activityReservationDA
        if (None == directionDA):
            self.m_DirectionDA = DirectionsDataAccess("./data/Map.ini")
        else:
            self.m_DirectionDA = directionDA
        if (None == paymentDA):
            self.m_PaymentDA = PaymentDataAccess("./data/Payment.ini")
        else:
            self.m_PaymentDA = paymentDA
        if (None == travelArrangementDA):
            self.m_TravelArrangementDA = TravelArrangementDataAccess("./data/TravelArrangement.ini")
        else:
            self.m_TravelArrangementDA = travelArrangementDA

        if (None == userDA):
            self.m_UserDA = UserDataAccess("./data/User.ini")
        else:
            self.m_UserDA = userDA

        if (None == appUser):
            self.m_AppUser = AppUser()
            self.m_AppUser.logout()
        else :
            self.m_AppUser = appUser

        loadCommand = LoadCommand()
        loadCommand.attach_dataaccess(self.m_RoomDA)
        loadCommand.attach_dataaccess(self.m_RoomReservationDA)
        loadCommand.attach_dataaccess(self.m_CommentDA)
        loadCommand.attach_dataaccess(self.m_RanchDA)
        loadCommand.attach_dataaccess(self.m_ActivityDA)
        loadCommand.attach_dataaccess(self.m_ActivityReservationDA)
        loadCommand.attach_dataaccess(self.m_DirectionDA)
        loadCommand.attach_dataaccess(self.m_PaymentDA)
        loadCommand.attach_dataaccess(self.m_TravelArrangementDA)
        loadCommand.attach_dataaccess(self.m_UserDA)
        
        self.m_commands.append(loadCommand)
        self.m_commands.append(LoginCommand(self.m_UserDA, self.m_AppUser))
        self.m_commands.append(LogoutCommand(self.m_AppUser))
        self.m_commands.append(PrintCurrentUserCommand(self.m_AppUser))
        
        self.m_commands.append(
                SubAppCommand(
                    GuestSubApp(
                        self.m_RoomReservationDA,
                        self.m_CommentDA,
                        self.m_RanchDA,
                        self.m_RoomDA,
                        self.m_ActivityDA,
                        self.m_ActivityReservationDA,
                        self.m_DirectionDA,
                        self.m_PaymentDA,
                        self.m_TravelArrangementDA,
                        self.m_UserDA,
                        self.m_AppUser
                        ), "Guest menu", False, False))
        self.m_commands.append(
                SubAppCommand(
                    AdminSubApp(
                        self.m_RoomReservationDA,
                        self.m_CommentDA,
                        self.m_RanchDA,
                        self.m_RoomDA,
                        self.m_ActivityDA,
                        self.m_ActivityReservationDA,
                        self.m_DirectionDA,
                        self.m_PaymentDA,
                        self.m_TravelArrangementDA,
                        self.m_UserDA,
                        self.m_AppUser
                        ), "Admin menu", True, True)
                    )
