# import other python files
import core
from fileManager import FileManager
import time
import window
import gloabalVars as gv

# setup
corefn = core.Core()
fM = FileManager()
window = window.Window()

# main
class Main:
    def __init__(self):
        self.ArgsList: list = []
        self.Args0 = None
        self.Args1 = None
        self.Args2 = None
        self.LaunchMode: str = fM.Settings['Preferred_Startup_Mode']

    def Update(self):
        corefn.CurrentListDataSetup()
        if self.LaunchMode == "":
            self.LaunchMode = input("Enter launch mode (console / window) > ")

        while gv.isProgramRunning:
            # process command
            match self.LaunchMode:
                case "console":
                    self.Console()
                case "window":
                    window.update()
                case _:
                    gv.isProgramRunning = False

    def Console(self):
        # I'm planning to remove console mode as it's harder to use and I haven't done anything new for it since the window mode was released.
        # uhh... I think the only thing I did for it is improving its performance.
        # anyway, I may remove it or keep it in another way.

        # get command
        self.ArgsList = list(map(str, input("Enter command\n> ").strip().split()))

        # distribute args
        try:
            self.Args0 = self.ArgsList[0]
            self.Args1 = self.ArgsList[1]
            self.Args2 = self.ArgsList[2]
        except IndexError:
            pass

        # process command
        if self.Args0 is not None:
            match self.Args0:
                case "add":
                    if self.Args1 is not None:
                        if self.Args1 == "name":
                            if self.Args2 is not None:
                                corefn.AddNewStudent(self.Args2)
                            else:
                                print("\nMissing args.\nCorrect usage > add <target> <name>\n")
                        elif self.Args1 == "object":
                            if self.Args2 is not None:
                                corefn.AddNewObject(self.Args2)
                            else:
                                print("\nMissing args.\nCorrect usage > add <target> <name>\n")
                        else:
                            print(
                                f"\nUnexpected arg names {self.Args1}.\nPlease make sure that you entered correct command.\n")
                    else:
                        print("\nMissing args.\nCorrect usage > add <target> <name>\n")

                case "remove":
                    if self.Args1 is not None:
                        if self.Args1 == "name":
                            if self.Args2 is not None:
                                corefn.RemoveName(self.Args2)
                            else:
                                print("\nMissing args.\nCorrect usage > remove <target> <name>\n")
                        elif self.Args1 == "object":
                            if self.Args2 is not None:
                                corefn.RemoveObject(self.Args2)
                            else:
                                print("\nMissing args.\nCorrect usage > remove <target> <name>\n")
                        else:
                            print(
                                f"\nUnexpected arg names {self.Args1}.\nPlease make sure that you entered correct command.\n")
                    else:
                        print("\nMissing args.\nCorrect usage > remove <target> <name>\n")

                case "match":
                    if self.Args1 is None and self.Args2 is None:
                        corefn.Match()
                    else:
                        print("\nUnexpected additional arg.\nThis command only requires Arg0.\n")

                case "clear":
                    if self.Args2 is None:
                        if self.Args1 is not None:
                            corefn.clear(self.Args1)
                        else:
                            print("\nMissing args.\nCorrect usage > clear <data>\n")
                    else:
                        print("\nUnexpected additional arg.\nThis command only requires Arg0 and Arg1.\n")

                case "help":
                    if self.Args2 is None:
                        corefn.help(self.Args1)
                    else:
                        print("\nUnexpected additional arg.\nThis command only requires Arg0.\n")

                case "load":
                    if self.Args1 is not None and self.Args2 is not None:
                        try:
                            if any([self.Args1 == "name", self.Args1 == "object"]):
                                corefn.LoadFromData(self.Args1, self.Args2)
                            else:
                                print(
                                    f"\nUnknown list names {self.Args1}.\nPlease check if you entered a correct list name.\n")

                        except FileNotFoundError:
                            print(f"\nFile {self.Args2} is not found.\nPlease check if you entered a correct path.\n")
                    else:
                        print("\nMissing args.\nCorrect usage > load <List Name> <File Path>\n")

                case "print":
                    if self.Args1 is not None:
                        if self.Args2 is None:
                            if self.Args1 == "name":
                                core.PrintOutData(corefn.NamesList, "name")
                            elif self.Args1 == "object":
                                core.PrintOutData(corefn.ObjectsList, "object")
                            else:
                                print(
                                    f"\nUnknown list names {self.Args1}. \nPlease check if entered a correct list name.\n")
                        else:
                            print("\nUnexpected additional arg.\nThis command only requires Arg0 and Arg1.\n")
                    else:
                        print("\nMissing args.\nCorrect usage > print <list name>\n")

                case "stop":
                    if self.Args1 is None and self.Args2 is None:
                        print("\nThanks for using! \nThis program will be automatically stopped in 3 seconds...\n")
                        time.sleep(3)
                        gv.isProgramRunning = False
                    else:
                        print("\nUnexpected additional arg.\nThis command only requires Arg0.\n")

                case "debug":
                    print("\nIt seems like that you entered a developer command.\n"
                          "This command might do something if the developer forgot to remove it from this place.\n")

                case _:
                    print("\nUnknown command.\nPlease make sure that you entered correct command (or use help command).\n")
        else:
            print("\nCommand cannot be None.\n")

        # reset vars
        self.Args0 = None
        self.Args1 = None
        self.Args2 = None

main = Main()
if __name__ == "__main__":
    main.Update()