from .abstractcommand import AbstractCommand
from ..datastructure import Comment
from ..dataaccess import CommentDataAccess

class DeleteCommentCommand(AbstractCommand):
    def __init__(self, cda):
        AbstractCommand.__init__(self)
        self.m_cda = cda

    def get_name(self):
        return "Delete a comment"
    
    def run(self):
        try :
            id = input("Delete the comment with this id:")
            self.m_cda.delete_comment_by_id(id)
        except EOFError:
            print("Action canceled")
        except ValueError:
            print("Value Error")
    def require_login(self):
        return True
    def require_admin(self):
        return  True
