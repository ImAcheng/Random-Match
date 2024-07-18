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
        self.CmdDetail: str = None

        corefn.CurListDataSetup()

    def Update(self):
        while self.isRunning:
            self.Command()

            if self.CmdToExecute == "add":
                self.CmdDetail = input("Enter the target (name / object): ")

                if self.CmdDetail == "name":
                    corefn.AddNewStudent(input("Enter a name: "))
                elif self.CmdDetail == "object":
                    corefn.AddNewObject(input("Enter a object: "))

            elif self.CmdToExecute == "remove":
                self.CmdDetail = input("Enter the target (name / object): ")

                if self.CmdDetail == "name":
                    corefn.RemoveStudent(input("Enter a name: "))
                elif self.CmdDetail == "object":
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

            else:
                print("\nUnknown command.\n")

    def Command(self):
        self.CmdToExecute = input("Enter a command: ")

main = Main()
if __name__ == "__main__":
    main.Update()