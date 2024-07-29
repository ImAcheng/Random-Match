# import other python files
import core
import fileManager
import time

# setup
corefn = core.Core()
fM = fileManager.FileManager()

# main
class Main:
    def __init__(self):
        self.isRunning: bool = True

        self.ArgsList: list = []
        self.Args0 = None
        self.Args1 = None
        self.Args2 = None

        corefn.CurrentListDataSetup()

    def Update(self):
        while self.isRunning:
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
                if self.Args0 == "add":
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
                            print(f"\nUnexpected arg names {self.Args1}.\nPlease make sure that you entered correct command.\n")
                    else:
                        print("\nMissing args.\nCorrect usage > add <target> <name>\n")

                elif self.Args0 == "remove":
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
                            print(f"\nUnexpected arg names {self.Args1}.\nPlease make sure that you entered correct command.\n")
                    else:
                        print("\nMissing args.\nCorrect usage > remove <target> <name>\n")

                elif self.Args0 == "match":
                    if self.Args1 is None and self.Args2 is None:
                        corefn.Match()
                    else:
                        print("\nUnexpected additional arg.\nThis command only requires Arg0.\n")

                elif self.Args0 == "clear":
                    if self.Args2 is None:
                        if self.Args1 is not None:
                            corefn.clear(self.Args1)
                        else:
                            print("\nMissing args.\nCorrect usage > clear <data>\n")
                    else:
                        print("\nUnexpected additional arg.\nThis command only requires Arg0 and Arg1.\n")

                elif self.Args0 == "help":
                    if self.Args2 is None:
                        corefn.help(self.Args1)
                    else:
                        print("\nUnexpected additional arg.\nThis command only requires Arg0.\n")

                elif self.Args0 == "load":
                    if self.Args1 is not None and self.Args2 is not None:
                        try:
                            if any([self.Args1 == "name", self.Args1 == "object"]):
                                corefn.LoadFromData(self.Args1, self.Args2)
                            else:
                                print(f"\nUnknown list names {self.Args1}.\nPlease check if you entered a correct list name.\n")

                        except FileNotFoundError:
                            print(f"\nFile {self.Args2} is not found.\nPlease check if you entered a correct path.\n")
                    else:
                        print("\nMissing args.\nCorrect usage > load <List Name> <File Path>\n")

                elif self.Args0 == "print":
                    if self.Args1 is not None:
                        if self.Args2 is None:
                            if self.Args1 == "name":
                                core.PrintOutData(corefn.NamesList, "name")
                            elif self.Args1 == "object":
                                core.PrintOutData(corefn.ObjectsList, "object")
                            else:
                                print(f"\nUnknown list names {self.Args1}. \nPlease check if entered a correct list name.\n")
                        else:
                            print("\nUnexpected additional arg.\nThis command only requires Arg0 and Arg1.\n")
                    else:
                        print("\nMissing args.\nCorrect usage > print <list name>\n")

                elif any([self.Args0 == "quit", self.Args0 == "stop"]):
                    if self.Args1 is None and self.Args2 is None:
                        print("\nThanks for using! \nThis program will be automatically stopped in 3 seconds...\n")
                        time.sleep(3)
                        self.isRunning = False
                    else:
                        print("\nUnexpected additional arg.\nThis command only requires Arg0.\n")

                elif self.Args0 == "debug":
                    print("\nIt seems like that you entered a developer command.\n"
                          "This command might do something if the developer forgot to remove it from this place.\n")

                else:
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