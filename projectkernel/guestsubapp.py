from .cliapp import CLIApp

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

from .command import LoadCommand

from .command import ListCommentsCommand

from .command import ListActivitiesCommand

from .command import ListRoomsCommand

from .command import ListRoomReservationsCommand

from .command import ListActivityReservationsCommand

from .command import ListPaymentsCommand

from .command import ListDirectionsCommand

from .command import ListTravelArrangementsCommand

from .command import PrintRanchCommand

from .command import LoginCommand

from .command import LogoutCommand

from .command import GuestAddCommentCommand

from .command import GuestMakeRoomReservationCommand

from .command import PrintCurrentUserCommand

from .appstatus import AppUser

class GuestSubApp(CLIApp):
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

        printRanchCommand = PrintRanchCommand(self.m_RanchDA)
        listCommentsCommand = ListCommentsCommand(self.m_CommentDA)
        listActivitiesCommand = ListActivitiesCommand(self.m_ActivityDA)
        listRoomsCommand = ListRoomsCommand(self.m_RoomDA)
        listDirectionsCommand = ListDirectionsCommand(self.m_DirectionDA)
        listTravelArrangementsCommand = ListTravelArrangementsCommand(self.m_TravelArrangementDA)
     
        self.m_commands.append(loadCommand)
        self.m_commands.append(LoginCommand(self.m_UserDA, self.m_AppUser))
        self.m_commands.append(LogoutCommand(self.m_AppUser)) 
        self.m_commands.append(PrintCurrentUserCommand(self.m_AppUser))
        self.m_commands.append(printRanchCommand)
        self.m_commands.append(listRoomsCommand)
        self.m_commands.append(listCommentsCommand)
        self.m_commands.append(listActivitiesCommand)
        self.m_commands.append(listDirectionsCommand)
        self.m_commands.append(listTravelArrangementsCommand)
        self.m_commands.append(GuestAddCommentCommand(self.m_CommentDA, self.m_AppUser))
        self.m_commands.append(GuestMakeRoomReservationCommand(self.m_RoomReservationDA, self.m_AppUser))
