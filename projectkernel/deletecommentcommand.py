from . import command
from .command import Command
from . import comment
from .comment import Comment
from . import commentdataaccess
from .commentdataaccess import CommentDataAccess
class DeleteCommentCommand(Command):
    def __init__(self, cda):
        Command.__init__(self)
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
