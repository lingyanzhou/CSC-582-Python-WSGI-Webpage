from . import command
from .command import Command

class CLIApp:
    def __init__(self):
        self.m_commands = []
    def run(self):
        while True:
            print("====================================")
            for i in range(len(self.m_commands)):
                print("{0:d}. {1:s}".format(i, self.m_commands[i].get_name()))
            print("{0:d}. Quit".format(len(self.m_commands)))
            print("Command: ")
            choice = 0
            try :
                choice = int(input("Your choice:"))
                if not choice in range(len(self.m_commands)+1):
                    raise ValueError()
            except EOFError:
                choice = len(self.m_commands)
            except ValueError:
                print("Invalid option")
                continue

            if choice == len(self.m_commands):
                print(chr(27) + "[2J")
                return
            elif choice in range(len(self.m_commands)):
                print(chr(27) + "[2J")
                self.m_commands[choice].run()
                input("Press Enter to continue")
                print(chr(27) + "[2J")
