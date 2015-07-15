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

from .command import SaveCommand

from .command import LoginCommand

from .command import LogoutCommand

from .command import ListCommentsCommand

from .command import ListActivitiesCommand

from .command import ListRoomsCommand

from .command import ListRoomReservationsCommand

from .command import ListActivityReservationsCommand

from .command import ListPaymentsCommand

from .command import ListDirectionsCommand

from .command import ListTravelArrangementsCommand

from .command import ListUsersCommand

from .command import PrintRanchCommand

from .command import AddActivityCommand

from .command import AddRoomCommand

from .command import AddCommentCommand

from .command import MakeRoomReservationCommand

from .command import MakeActivityReservationCommand

from .command import MakePaymentCommand

from .command import MakeTravelArrangementCommand

from .command import UpdateRanchCommand

from .command import UpdateRoomCommand

from .command import UpdateActivityCommand

from .command import UpdateCommentCommand

from .command import UpdateRoomReservationCommand

from .command import UpdateActivityReservationCommand

from .command import UpdatePaymentCommand

from .command import UpdateTravelArrangementCommand

from .command import UpdateUserCommand

from .command import DeleteRoomCommand

from .command import DeleteActivityCommand

from .command import DeleteCommentCommand

from .command import DeleteRoomReservationCommand

from .command import DeleteActivityReservationCommand

from .command import DeletePaymentCommand

from .command import DeleteTravelArrangementCommand

from .command import DeleteUserCommand

from .command import LoginCommand

from .command import LogoutCommand

from .command import AddUserCommand

from .command import PrintCurrentUserCommand

from .appstatus import AppUser

class AdminSubApp(CLIApp):
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
 
        saveCommand = SaveCommand()
        saveCommand.attach_dataaccess(self.m_RoomDA)
        saveCommand.attach_dataaccess(self.m_RoomReservationDA)
        saveCommand.attach_dataaccess(self.m_CommentDA)
        saveCommand.attach_dataaccess(self.m_RanchDA)
        saveCommand.attach_dataaccess(self.m_ActivityDA)
        saveCommand.attach_dataaccess(self.m_ActivityReservationDA)
        saveCommand.attach_dataaccess(self.m_DirectionDA)
        saveCommand.attach_dataaccess(self.m_PaymentDA)
        saveCommand.attach_dataaccess(self.m_TravelArrangementDA)


        printRanchCommand = PrintRanchCommand(self.m_RanchDA)
        listCommentsCommand = ListCommentsCommand(self.m_CommentDA)
        listActivitiesCommand = ListActivitiesCommand(self.m_ActivityDA)
        listRoomsCommand = ListRoomsCommand(self.m_RoomDA)
        listRoomReservationsCommand = ListRoomReservationsCommand(self.m_RoomReservationDA)
        listActivityReservationsCommand = ListActivityReservationsCommand(self.m_ActivityReservationDA)
        listDirectionsCommand = ListDirectionsCommand(self.m_DirectionDA)
        listPaymentsCommand = ListPaymentsCommand(self.m_PaymentDA)
        listTravelArrangementsCommand = ListTravelArrangementsCommand(self.m_TravelArrangementDA)
        
        addRoomCommand = AddRoomCommand(self.m_RoomDA)
        addActivityCommand = AddActivityCommand(self.m_ActivityDA)
        addCommentCommand = AddCommentCommand(self.m_CommentDA)
        makeRoomReservationCommand = MakeRoomReservationCommand(self.m_RoomReservationDA)
        makeActivityReservationCommand = MakeActivityReservationCommand(self.m_ActivityReservationDA)
        makePaymentCommand = MakePaymentCommand(self.m_PaymentDA)
        makeTravelArrangementCommand = MakeTravelArrangementCommand(self.m_TravelArrangementDA)
        
        updateRanchCommand = UpdateRanchCommand(self.m_RanchDA)
        updateRoomCommand = UpdateRoomCommand(self.m_RoomDA)
        updateActivityCommand = UpdateActivityCommand(self.m_ActivityDA)
        updateCommentCommand = UpdateCommentCommand(self.m_CommentDA)
        updateRoomReservationCommand = UpdateRoomReservationCommand(self.m_RoomReservationDA)
        updateActivityReservationCommand = UpdateActivityReservationCommand(self.m_ActivityReservationDA)
        updatePaymentCommand = UpdatePaymentCommand(self.m_PaymentDA)
        updateTravelArrangementCommand = UpdateTravelArrangementCommand(self.m_TravelArrangementDA)

        deleteRoomCommand = DeleteRoomCommand(self.m_RoomDA)
        deleteActivityCommand = DeleteActivityCommand(self.m_ActivityDA)
        deleteCommentCommand = DeleteCommentCommand(self.m_CommentDA)
        deleteRoomReservationCommand = DeleteRoomReservationCommand(self.m_RoomReservationDA)
        deleteActivityReservationCommand = DeleteActivityReservationCommand(self.m_ActivityReservationDA)
        deletePaymentCommand = DeletePaymentCommand(self.m_PaymentDA)
        deleteTravelArrangementCommand = DeleteTravelArrangementCommand(self.m_TravelArrangementDA)

        self.m_commands.append(saveCommand)
        self.m_commands.append(loadCommand)
        self.m_commands.append(LoginCommand(self.m_UserDA, self.m_AppUser))
        self.m_commands.append(LogoutCommand(self.m_AppUser))
        self.m_commands.append(PrintCurrentUserCommand(self.m_AppUser))
        self.m_commands.append(printRanchCommand)
        self.m_commands.append(listRoomsCommand)
        self.m_commands.append(listCommentsCommand)
        self.m_commands.append(listActivitiesCommand)
        self.m_commands.append(listRoomReservationsCommand)
        self.m_commands.append(listActivityReservationsCommand)
        self.m_commands.append(listPaymentsCommand)
        self.m_commands.append(listDirectionsCommand)
        self.m_commands.append(listTravelArrangementsCommand)
        self.m_commands.append(ListUsersCommand(self.m_UserDA))
        
        self.m_commands.append(addRoomCommand)
        self.m_commands.append(addActivityCommand)
        self.m_commands.append(addCommentCommand)
        self.m_commands.append(makeRoomReservationCommand)
        self.m_commands.append(makeActivityReservationCommand)
        self.m_commands.append(makePaymentCommand)
        self.m_commands.append(makeTravelArrangementCommand)
        self.m_commands.append(AddUserCommand(self.m_UserDA))


        self.m_commands.append(updateRanchCommand)
        self.m_commands.append(updateRoomCommand)
        self.m_commands.append(updateActivityCommand)
        self.m_commands.append(updateCommentCommand)
        self.m_commands.append(updateRoomReservationCommand)
        self.m_commands.append(updateActivityReservationCommand)
        self.m_commands.append(updatePaymentCommand)
        self.m_commands.append(updateTravelArrangementCommand)
        self.m_commands.append(UpdateUserCommand(self.m_UserDA))

        self.m_commands.append(deleteRoomCommand)
        self.m_commands.append(deleteActivityCommand)
        self.m_commands.append(deleteCommentCommand)
        self.m_commands.append(deleteRoomReservationCommand)
        self.m_commands.append(deleteActivityReservationCommand)
        self.m_commands.append(deletePaymentCommand)
        self.m_commands.append(deleteTravelArrangementCommand)
        self.m_commands.append(DeleteUserCommand(self.m_UserDA))
