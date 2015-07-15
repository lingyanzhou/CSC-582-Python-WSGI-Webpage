from .abstractcommand import AbstractCommand
from ..datastructure import Payment
from ..dataaccess import PaymentDataAccess
class ListPaymentsCommand(AbstractCommand):
    def __init__(self, pda):
        AbstractCommand.__init__(self)
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
                    
    def require_login(self):
        return True
    def require_admin(self):
        return True
