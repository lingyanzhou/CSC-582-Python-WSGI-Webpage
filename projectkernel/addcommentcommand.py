from . import command
from .command import Command
from . import comment
from .comment import Comment
from . import commentdataaccess
from .commentdataaccess import CommentDataAccess
class AddCommentCommand(Command):
    def __init__(self, cda):
        Command.__init__(self)
        self.m_cda = cda

    def get_name(self):
        return "Add a comment"
    
    def run(self):
        try :
            c = Comment()
            c.set_id("0")
            name = input("User name:")
            c.set_user_name(name)
            c.set_time_now()
            msg = input("Comment:")
            c.set_message(msg)
            self.m_cda.add_comment(c)
        except EOFError:
            print("Action canceled")
