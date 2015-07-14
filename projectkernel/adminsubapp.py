from . import cliapp
from .cliapp import CLIApp

from . import loadcommand
from .loadcommand import LoadCommand

from . import savecommand
from .savecommand import SaveCommand

from . import roomdataaccess
from .roomdataaccess import RoomDataAccess

from . import roomreservationdataaccess
from .roomreservationdataaccess import RoomReservationDataAccess

from . import commentdataaccess
from .commentdataaccess import CommentDataAccess

from . import ranchdataaccess
from .ranchdataaccess import RanchDataAccess

from . import activitydataaccess
from .activitydataaccess import ActivityDataAccess

from . import activityreservationdataaccess
from .activityreservationdataaccess import ActivityReservationDataAccess

from . import directionsdataaccess
from .directionsdataaccess import DirectionsDataAccess

from . import paymentdataaccess
from .paymentdataaccess import PaymentDataAccess

from . import travelarrangementdataaccess
from .travelarrangementdataaccess import TravelArrangementDataAccess

from . import listcommentscommand
from .listcommentscommand import ListCommentsCommand

from . import listactivitiescommand
from .listactivitiescommand import ListActivitiesCommand

from . import listroomscommand
from .listroomscommand import ListRoomsCommand

from . import listroomreservationscommand
from .listroomreservationscommand import ListRoomReservationsCommand

from . import listactivityreservationscommand
from .listactivityreservationscommand import ListActivityReservationsCommand

from . import listpaymentscommand
from .listpaymentscommand import ListPaymentsCommand

from . import listdirectionscommand
from .listdirectionscommand import ListDirectionsCommand

from . import listtravelarrangementscommand
from .listtravelarrangementscommand import ListTravelArrangementsCommand

from . import printranchcommand
from .printranchcommand import PrintRanchCommand

from . import addactivitycommand
from .addactivitycommand import AddActivityCommand

from . import addroomcommand
from .addroomcommand import AddRoomCommand

from . import addcommentcommand
from .addcommentcommand import AddCommentCommand

from . import makeroomreservationcommand
from .makeroomreservationcommand import MakeRoomReservationCommand

from . import makeactivityreservationcommand
from .makeactivityreservationcommand import MakeActivityReservationCommand

from . import makepaymentcommand
from .makepaymentcommand import MakePaymentCommand

from . import maketravelarrangementcommand
from .maketravelarrangementcommand import MakeTravelArrangementCommand

from . import updateranchcommand
from .updateranchcommand import UpdateRanchCommand

from . import updateroomcommand
from .updateroomcommand import UpdateRoomCommand

from . import updateactivitycommand
from .updateactivitycommand import UpdateActivityCommand

from . import updatecommentcommand
from .updatecommentcommand import UpdateCommentCommand

from . import updateroomreservationcommand
from .updateroomreservationcommand import UpdateRoomReservationCommand

from . import updateactivityreservationcommand
from .updateactivityreservationcommand import UpdateActivityReservationCommand

from . import updatepaymentcommand
from .updatepaymentcommand import UpdatePaymentCommand

from . import updatetravelarrangementcommand
from .updatetravelarrangementcommand import UpdateTravelArrangementCommand

from . import deleteroomcommand
from .deleteroomcommand import DeleteRoomCommand

from . import deleteactivitycommand
from .deleteactivitycommand import DeleteActivityCommand

from . import deletecommentcommand
from .deletecommentcommand import DeleteCommentCommand

from . import deleteroomreservationcommand
from .deleteroomreservationcommand import DeleteRoomReservationCommand

from . import deleteactivityreservationcommand
from .deleteactivityreservationcommand import DeleteActivityReservationCommand

from . import deletepaymentcommand
from .deletepaymentcommand import DeletePaymentCommand

from . import deletetravelarrangementcommand
from .deletetravelarrangementcommand import DeleteTravelArrangementCommand

class AdminSubApp(CLIApp):
    def __init__(self, roomReservationDA = None, commentDA = None, ranchDA = None,
            roomDA = None, activityDA = None, activityReservationDA = None, directionDA = None,
            paymentDA = None, travelArrangementDA = None):
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
        self.m_commands.append(printRanchCommand)
        self.m_commands.append(listRoomsCommand)
        self.m_commands.append(listCommentsCommand)
        self.m_commands.append(listActivitiesCommand)
        self.m_commands.append(listRoomReservationsCommand)
        self.m_commands.append(listActivityReservationsCommand)
        self.m_commands.append(listPaymentsCommand)
        self.m_commands.append(listDirectionsCommand)
        self.m_commands.append(listTravelArrangementsCommand)
        
        self.m_commands.append(addRoomCommand)
        self.m_commands.append(addActivityCommand)
        self.m_commands.append(addCommentCommand)
        self.m_commands.append(makeRoomReservationCommand)
        self.m_commands.append(makeActivityReservationCommand)
        self.m_commands.append(makePaymentCommand)
        self.m_commands.append(makeTravelArrangementCommand)

        self.m_commands.append(updateRanchCommand)
        self.m_commands.append(updateRoomCommand)
        self.m_commands.append(updateActivityCommand)
        self.m_commands.append(updateCommentCommand)
        self.m_commands.append(updateRoomReservationCommand)
        self.m_commands.append(updateActivityReservationCommand)
        self.m_commands.append(updatePaymentCommand)
        self.m_commands.append(updateTravelArrangementCommand)

        self.m_commands.append(deleteRoomCommand)
        self.m_commands.append(deleteActivityCommand)
        self.m_commands.append(deleteCommentCommand)
        self.m_commands.append(deleteRoomReservationCommand)
        self.m_commands.append(deleteActivityReservationCommand)
        self.m_commands.append(deletePaymentCommand)
        self.m_commands.append(deleteTravelArrangementCommand)
