from . import command
from .command import Command
from . import payment
from .payment import Payment
from . import paymentdataaccess
from .paymentdataaccess import PaymentDataAccess
class DeletePaymentCommand(Command):
    def __init__(self, pda):
        Command.__init__(self)
        self.m_pda = pda

    def get_name(self):
        return "Delete a payment"
    
    def run(self):
        try :
            id = input("Delete the payment with this id:")
            self.m_pda.delete_by_id(id)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
