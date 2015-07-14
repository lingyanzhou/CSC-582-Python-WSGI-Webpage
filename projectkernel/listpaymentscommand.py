from . import command
from .command import Command
from . import payment
from .payment import Payment
from . import paymentdataaccess
from .paymentdataaccess import PaymentDataAccess
class ListPaymentsCommand(Command):
    def __init__(self, pda):
        Command.__init__(self)
        self.m_pda = pda

    def get_name(self):
        return "List payments"
    
    def run(self):
        plist = self.m_pda.list_all()
        for p in plist:
            print("=========================")
            print("id:", p.get_id())
            print("user id:", p.get_user_id())
            print("pending:", p.is_pending())
            print("amount:", p.get_amount())
