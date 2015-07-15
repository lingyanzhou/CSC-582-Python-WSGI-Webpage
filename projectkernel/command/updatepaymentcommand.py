from .abstractcommand import AbstractCommand
from ..datastructure import Payment
from ..dataaccess import PaymentDataAccess
class UpdatePaymentCommand(AbstractCommand):
    def __init__(self, pda):
        AbstractCommand.__init__(self)
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
    def require_login(self):
        return True
    def require_admin(self):
        return  True
