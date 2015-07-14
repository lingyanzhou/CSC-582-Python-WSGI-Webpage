from . import command
from .command import Command
from . import comment
from .comment import Comment
from . import commentdataaccess
from .commentdataaccess import CommentDataAccess
class ListCommentsCommand(Command):
    def __init__(self, cda):
        Command.__init__(self)
        self.m_cda = cda

    def get_name(self):
        return "List comments"
    
    def run(self):
        clist = self.m_cda.list_all_comments()
        for c in clist:
            print("=========================")
            print("id:", c.get_id())
            print("user:", c.get_user_name())
            print("time:", c.get_time_as_str())
            print("message:", c.get_message())
