from . import command
from .command import Command
from . import payment
from .payment import Payment
from . import paymentdataaccess
from .paymentdataaccess import PaymentDataAccess
class UpdatePaymentCommand(Command):
    def __init__(self, pda):
        Command.__init__(self)
        self.m_pda = pda

    def get_name(self):
        return "Update a payment"
    
    def run(self):
        try :
            p = Payment()
            p.set_id(input("Update the payment with this id:"))
            p.set_user_id(input("user id:"))
            p.set_is_pending("True"==input("Pending (True or False):"))
            p.set_amount(float(input("Amount:")))
            self.m_pda.update(p)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
