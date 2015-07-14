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

from . import guestsubapp
from .guestsubapp import GuestSubApp

from . import adminsubapp
from .adminsubapp import AdminSubApp

from . import subappcommand
from .subappcommand import SubAppCommand


class MainApp(CLIApp):
    def __init__(self):
        CLIApp.__init__(self)
        self.m_RoomReservationDA = RoomReservationDataAccess("./data/RoomReservation.ini")
        self.m_CommentDA = CommentDataAccess("./data/Comment.ini")
        self.m_RanchDA = RanchDataAccess("./data/Ranch.ini")
        self.m_RoomDA = RoomDataAccess("./data/Room.ini")
        self.m_ActivityDA = ActivityDataAccess("./data/Activity.ini")
        self.m_ActivityReservationDA = ActivityReservationDataAccess("./data/ActivityReservation.ini")
        self.m_DirectionDA = DirectionsDataAccess("./data/Map.ini")
        self.m_PaymentDA = PaymentDataAccess("./data/Payment.ini")
        self.m_TravelArrangementDA = TravelArrangementDataAccess("./data/TravelArrangement.ini")

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
                        self.m_TravelArrangementDA
                        ), "Guest menu"))
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
                        self.m_TravelArrangementDA
                        ), "Admin menu")
                    )
