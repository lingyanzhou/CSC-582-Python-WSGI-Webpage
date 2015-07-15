from .abstractcommand import AbstractCommand
from ..datastructure import Comment
from ..dataaccess import CommentDataAccess
class ListCommentsCommand(AbstractCommand):
    def __init__(self, cda):
        AbstractCommand.__init__(self)
        self.m_cda = cda

    def get_name(self):
        return "List comments"
    
    def run(self):
        clist = self.m_cda.list_all_comments()
        for c in clist:
            print("=========================")
            print("id:", c.get_id())
            print("user id:", c.get_user_id())
            print("time:", c.get_time_as_str())
            print("message:", c.get_message())
    def require_login(self):
        return False
    def require_admin(self):
        return False
