# import python files
import core

# setup
corefn = core.Core()

# main
class Main:
    def __init__(self):
        self.isRunning: bool = True
        self.CmdToExecute: str = None

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

            elif self.CmdToExecute == "quit":
                self.isRunning = False

            else:
                print("Unknown command.\n")

    def Command(self):
        self.CmdToExecute = input("Enter a command: ")

main = Main()
if __name__ == "__main__":
    main.Update()