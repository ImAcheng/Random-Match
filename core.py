# import python modules
import os
import json
import random

# import json files
import fileManager
fm = fileManager.FileManager()

# functions
def ListLenType(TargetList: list) -> str:
    if len(TargetList) > 1:
        return "are"
    else:
        return "is"

def PrintOutData(TargetList: list, DisplayName: str):
    ListString = ", ".join(TargetList)
    if TargetList:
        print(f"\nThere {ListLenType(TargetList)} - \n{ListString} \nin the {DisplayName} list.\n")
    else:
        print(f"\n{DisplayName} list is empty.\n")

# main
class Core:
    def __init__(self):
        self.NamesList: list = fm.NamesData['Names']
        self.ObjectsList: list = fm.ObjectsData['Objects']
        self.cur_NamesList: list = []
        self.cur_ObjectsList: list = []
        self.StudentToRemove: str = None
        self.ListDebugNum: int = 0
        self.RandomName: str = None
        self.RandomObject: str = None
        self.Matched: list = []
        self.ListUsedToBeRange: list = None
        self.IndexCheck: int = None

    def AddNewStudent(self, name: str):
        # program data
        self.NamesList.append(name)
        self.cur_NamesList.append(name)

        # save data
        fm.NamesData['Names'] = self.NamesList
        with open(os.path.join("UserData", "Names.json"), "w") as file:
            json.dump(fm.NamesData, file)

        # print messages
        print(f"\nSuccessfully added '{name}' to the names list.")
        PrintOutData(self.NamesList, "name")

    def RemoveStudent(self, name: str):
        try:
            # program data
            self.NamesList.remove(name)
            self.cur_NamesList.remove(name)

            # save data
            fm.NamesData['Names'] = self.NamesList
            with open(os.path.join("UserData", "Names.json"), "w") as file:
                json.dump(fm.NamesData, file)

            # print messages
            print(f"\nSuccessfully removed '{name}' from the names list.")
            PrintOutData(self.NamesList, "name")
        except ValueError:
            print(f"Data '{name}' doesn't exist.")

    def AddNewObject(self, name: str):
        # program data
        self.ObjectsList.append(name)
        self.cur_ObjectsList.append(name)

        # save data
        fm.ObjectsData['Objects'] = self.ObjectsList
        with open(os.path.join("UserData", "Objects.json"), "w") as file:
            json.dump(fm.ObjectsData, file)

        # print messages
        print(f"\nSuccessfully added '{name}' to the objects list.")
        PrintOutData(self.ObjectsList, "object")

    def RemoveObject(self, name: str):
        try:
            # program data
            self.ObjectsList.remove(name)
            self.cur_ObjectsList.remove(name)

            # save data
            fm.ObjectsData['Objects'] = self.ObjectsList
            with open(os.path.join("UserData", "Objects.json"), "w") as file:
                json.dump(fm.ObjectsData, file)

                # print messages
                print(f"\nSuccessfully removed '{name}' from the objects list.")
                PrintOutData(self.NamesList, "name")
        except ValueError:
            print(f"Data '{name}' doesn't exist.")

    def Match(self):
        # get the list which is used to be the range
        if len(self.NamesList) > len(self.ObjectsList):
            self.ListUsedToBeRange = self.cur_ObjectsList
        else:
            self.ListUsedToBeRange = self.cur_NamesList

        if self.cur_NamesList and self.cur_ObjectsList:
            # match
            for i in range(len(self.ListUsedToBeRange)):
                # random choose
                self.RandomName = random.choice(self.cur_NamesList)
                self.RandomObject = random.choice(self.cur_ObjectsList)

                # add to list
                self.Matched.append([self.RandomName, self.RandomObject])

                # remove from list
                self.cur_NamesList.remove(self.RandomName)
                self.cur_ObjectsList.remove(self.RandomObject)

            # print result
            print("\n======================")
            for i in range(len(self.Matched)):
                print(", ".join(self.Matched[i]))
            print("======================\n")
        else:
            print("\nCannot run match command due to the empty list(s).\n")

        # reset
        self.Matched.clear()
        self.CurrentListDataSetup()

    def clear(self, data: str):
        AbleToPrint: bool = False
        isDataCorrect: bool = True

        if data == "name":
            if self.NamesList:
                # program data
                self.NamesList.clear()
                self.cur_NamesList.clear()

                # save data
                fm.NamesData['Names'] = self.NamesList
                with open(os.path.join("UserData", "Names.json"), "w") as file:
                    json.dump(fm.NamesData, file)

                AbleToPrint = True
            else:
                print("\nCannot run 'clear name' command due to the empty list.")

        elif data == "object":
            if self.ObjectsList:
                # program data
                self.ObjectsList.clear()
                self.cur_ObjectsList.clear()

                # save data
                fm.ObjectsData['Objects'] = self.ObjectsList
                with open(os.path.join("UserData", "Objects.json"), "w") as file:
                    json.dump(fm.ObjectsData, file)

                AbleToPrint = True
            else:
                print("\nCannot run 'clear object' command due to the empty list.")

        elif data == "all":
            if self.NamesList and self.ObjectsList:
                # program data
                self.NamesList.clear()
                self.ObjectsList.clear()
                self.cur_NamesList.clear()
                self.cur_ObjectsList.clear()

                # save data
                fm.NamesData['Names'] = self.NamesList
                with open(os.path.join("UserData", "Names.json"), "w") as file:
                    json.dump(fm.NamesData, file)

                fm.ObjectsData['Objects'] = self.ObjectsList
                with open(os.path.join("UserData", "Objects.json"), "w") as file:
                    json.dump(fm.ObjectsData, file)

                AbleToPrint = True
            else:
                print("\nCannot run 'clear all' command due to the empty list(s).")

        else:
            print(f"\nUnexpected arg names {data}.\nPlease make sure that you entered correct command.\n")
            isDataCorrect = False

        if isDataCorrect and AbleToPrint:
            print(f"\n====================\nCleared {data}\n====================\n")

    def help(self, command):
        if command is None:
            print("\n- Commands List -")
            for i in range(len(fm.CmdList['cmds'])):
                print(f"{fm.CmdList['cmds'][i]}: {fm.CmdExpl['expl'][i]}")
            print("")
        else:
            # check if command is found and record its index
            for i in range(len(fm.CmdList['cmds'])):
                if command == fm.CmdList['cmds'][i]:
                    self.IndexCheck = i

            if self.IndexCheck is not None:
                print(f"\nCommand - {fm.CmdList['cmds'][self.IndexCheck]}\n{fm.CmdExpl['detail'][self.IndexCheck]}\n")
            else:
                print(f"\nCommand '{command}' is not found.\n")

        # reset data
        self.IndexCheck = None

    def CurrentListDataSetup(self):
        # clear exist data
        self.cur_NamesList.clear()
        self.cur_ObjectsList.clear()

        # name
        if self.NamesList:
            for idx, digit in enumerate(self.NamesList):
                self.cur_NamesList.append(digit)

        # object
        if self.ObjectsList:
            for idx, digit in enumerate(self.ObjectsList):
                self.cur_ObjectsList.append(digit)

    def LoadFromData(self, list_name: str, File: str):
        # load file
        with open(File, "r", encoding='utf8') as file:
            Data = list(map(str, file.read().strip().split()))

        if list_name == "name":
            # cover data
            self.NamesList = Data

            # save data
            fm.NamesData['Names'] = self.NamesList
            with open(os.path.join("UserData", "Names.json"), "w") as file:
                json.dump(fm.NamesData, file)

            # print data
            PrintOutData(self.NamesList, "names")

        elif list_name == "object":
            # cover data
            self.ObjectsList = Data

            # save data
            fm.ObjectsData['Objects'] = self.ObjectsList
            with open(os.path.join("UserData", "Objects.json"), "w") as file:
                json.dump(fm.ObjectsData, file)

            # print data
            PrintOutData(self.ObjectsList, "objects")

        self.CurrentListDataSetup()