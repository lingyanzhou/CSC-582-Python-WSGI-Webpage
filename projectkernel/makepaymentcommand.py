from . import command
from .command import Command
from . import payment
from .payment import Payment
from . import paymentdataaccess
from .paymentdataaccess import PaymentDataAccess
class MakePaymentCommand(Command):
    def __init__(self, pda):
        Command.__init__(self)
        self.m_pda = pda

    def get_name(self):
        return "Make a payment"
    
    def run(self):
        try :
            p = Payment()
            p.set_id("0")
            amount = int(input("Amount:"))
            p.set_amount(amount)
            self.m_pda.add(p)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
