# import other python files
import core
import fileManager

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

        corefn.CurListDataSetup()

    def Update(self):
        while self.isRunning:
            # get command
            self.ArgsList = list(map(str, input("Enter command\n> ").strip().split()))

            # distribute args
            self.Args0 = self.ArgsList[0]
            if len(self.ArgsList) - 1 >= 1:
                self.Args1 = self.ArgsList[1]
            if len(self.ArgsList) - 1 >= 2:
                self.Args2 = self.ArgsList[2]   # I know these codes look stupid.

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
                            corefn.AddNewStudent(self.Args2)
                        else:
                            print("\nMissing args.\nCorrect usage > remove <target> <name>\n")
                    elif self.Args1 == "object":
                        if self.Args2 is not None:
                            corefn.AddNewObject(self.Args2)
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

            elif any([self.Args0 == "quit", self.Args0 == "stop"]):
                if self.Args1 is None and self.Args2 is None:
                    self.isRunning = False
                else:
                    print("\nUnexpected additional arg.\nThis command only requires Arg0.\n")

            else:
                print("\nUnknown command.\nPlease make sure that you entered correct command (or use help command).\n")

            # reset vars
            self.Args0 = None
            self.Args1 = None
            self.Args2 = None

main = Main()
if __name__ == "__main__":
    main.Update()