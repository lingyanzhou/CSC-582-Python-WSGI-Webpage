from .abstractcommand import AbstractCommand
from ..datastructure import Comment
from ..dataaccess import CommentDataAccess
class GuestAddCommentCommand(AbstractCommand):
    def __init__(self, cda, appUser):
        AbstractCommand.__init__(self)
        self.m_cda = cda
        self.m_AppUser = appUser

    def get_name(self):
        return "Add a comment"
    
    def run(self):
        if not self.m_AppUser.has_logged_in():
            return
        try :
            c = Comment()
            c.set_id("0")
            c.set_user_id(self.m_AppUser.get_id())
            c.set_time_now()
            c.set_message(input("Comment:"))
            self.m_cda.add_comment(c)
        except EOFError:
            print("Action canceled")
    def require_login(self):
        return True
    def require_admin(self):
        return False 
