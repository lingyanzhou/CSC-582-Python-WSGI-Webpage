from .abstractcommand import AbstractCommand
from ..datastructure import Comment
from ..dataaccess import CommentDataAccess

class UpdateCommentCommand(AbstractCommand):
    def __init__(self, cda):
        AbstractCommand.__init__(self)
        self.m_cda = cda

    def get_name(self):
        return "Update a comment"
    
    def run(self):
        try :
            c = Comment()
            id = input("Update the comment with this id:")
            c.set_id(id)
            id = input("User id:")
            c.set_user_id(id)
            c.set_time_now()
            msg = input("Comment:")
            c.set_message(msg)
            self.m_cda.update_comment(c)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
    def require_login(self):
        return True
    def require_admin(self):
        return  True
