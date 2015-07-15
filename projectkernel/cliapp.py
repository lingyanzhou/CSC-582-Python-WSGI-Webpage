from .command import AbstractCommand
from .appstatus import AppUser
import os

class CLIApp:
    def __init__(self):
        self.m_commands = []
        self.m_AppUser = None
        
    def run(self):
        while True:
            print("====================================")
            optionList = []
            for i in range(len(self.m_commands)):
                isAccepted = self.m_commands[i].is_appuser_accepted(self.m_AppUser)
                if isAccepted:
                    print("{0:d}. {1:s}".format(len(optionList), self.m_commands[i].get_name()))
                    optionList.append(i)

            print("{0:d}. Quit".format(len(optionList)))
            print("Command: ")
            choice = 0
            try :
                choice = int(input("Your choice:"))
                if not (choice>=0 and choice <=len(optionList)):
                    raise ValueError()
            except EOFError:
                choice = len(optionList)
            except ValueError:
                print("Invalid option")
                continue

            if choice == len(optionList):
                self.clear_screen()
                return
            elif choice>=0 and choice <len(optionList):
                self.clear_screen()
                self.m_commands[optionList[choice]].run()
                input("Press Enter to continue")
                self.clear_screen()
                
    def clear_screen(self):
        if os.name=="nt":
            os.system("cls")
        elif os.name=="posix":
            print(chr(27) + "[2J")
        else:
            print("\n"*10)
