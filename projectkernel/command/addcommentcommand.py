from .abstractcommand import AbstractCommand
from ..datastructure import Comment
from ..dataaccess import CommentDataAccess
class AddCommentCommand(AbstractCommand):
    def __init__(self, cda):
        AbstractCommand.__init__(self)
        self.m_cda = cda

    def get_name(self):
        return "Add a comment"
    
    def run(self):
        try :
            c = Comment()
            c.set_id("0")
            c.set_user_id(input("User ID:"))
            c.set_time_now()
            c.set_message(input("Comment:"))
            self.m_cda.add_comment(c)
        except EOFError:
            print("Action canceled")
    def require_login(self):
        return True
    def require_admin(self):
        return  True
