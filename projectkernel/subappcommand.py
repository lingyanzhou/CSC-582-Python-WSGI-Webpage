from .command.abstractcommand import AbstractCommand
from .cliapp import CLIApp
class SubAppCommand(AbstractCommand):
    def __init__(self, subapp, name,
            isLoginRequired, isAdminRequired):
        AbstractCommand.__init__(self)
        self.m_subapp = subapp
        self.m_name = name
        self.m_is_login_required = isLoginRequired
        self.m_is_admin_required = isAdminRequired

    def get_name(self):
        return self.m_name

    def run(self):
        self.m_subapp.run()

    def require_login(self):
        return self.m_is_login_required
    
    def require_admin(self):
        return self.m_is_admin_required
