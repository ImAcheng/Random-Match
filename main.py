# import python files
import core

# import other python files
import fileManager

# setup
corefn = core.Core()
fM = fileManager.FileManager()

# main
class Main:
    def __init__(self):
        self.isRunning: bool = True
        self.CmdToExecute: str = None

        corefn.CurListDataSetup()

    def Update(self):
        while self.isRunning:
            self.Command()

            if self.CmdToExecute == "add st":
                corefn.AddNewStudent(input("Enter a name: "))

            elif self.CmdToExecute == "remove st":
                corefn.RemoveStudent(input("Enter a name: "))

            elif self.CmdToExecute == "add obj":
                corefn.AddNewObject(input("Enter a object: "))

            elif self.CmdToExecute == "remove obj":
                corefn.RemoveObject(input("Enter a object: "))

            elif self.CmdToExecute == "match":
                corefn.Match()

            elif self.CmdToExecute == "clear":
                corefn.clear(input("\nEnter data type (name / obj / all): "))

            elif self.CmdToExecute == "help":
                print("\n- Commands List -")
                for i in range(len(fM.CmdList['cmds'])):
                    print(f"{fM.CmdList['cmds'][i]}: {fM.CmdExpl['expl'][i]}")
                print("\n")

            elif self.CmdToExecute == "quit":
                self.isRunning = False

            elif self.CmdToExecute == "print":
                corefn.PrintListContent()

            else:
                print("\nUnknown command.\n")

    def Command(self):
        self.CmdToExecute = input("Enter a command: ")

main = Main()
if __name__ == "__main__":
    main.Update()