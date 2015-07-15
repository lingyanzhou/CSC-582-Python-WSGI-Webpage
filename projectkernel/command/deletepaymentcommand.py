from .abstractcommand import AbstractCommand
from ..datastructure import Payment
from ..dataaccess import PaymentDataAccess
class DeletePaymentCommand(AbstractCommand):
    def __init__(self, pda):
        AbstractCommand.__init__(self)
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
            
    def require_login(self):
        return True
    def require_admin(self):
        return True
