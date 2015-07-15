from .abstractcommand import AbstractCommand
from ..datastructure import Payment
from ..dataaccess import PaymentDataAccess
class MakePaymentCommand(AbstractCommand):
    def __init__(self, pda):
        AbstractCommand.__init__(self)
        self.m_pda = pda

    def get_name(self):
        return "Make a payment"
    
    def run(self):
        try :
            p = Payment()
            p.set_id("0")
            p.set_user_id(input("user id:"))
            p.set_is_pending("True"==input("Pending (True or False):"))
            p.set_amount(float(input("Amount:")))
            self.m_pda.add(p)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
    def require_login(self):
        return True
    def require_admin(self):
        return True
