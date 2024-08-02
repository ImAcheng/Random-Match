# import python modules
import os
import json
import random

# import other python files
import fileManager
import gloabalVars as gv

# setup
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
        PrintOutData(self.NamesList, "names")

    def RemoveName(self, name: str):
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
            PrintOutData(self.NamesList, "names")
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
        PrintOutData(self.ObjectsList, "objects")

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
                PrintOutData(self.NamesList, "objects")
        except ValueError:
            print(f"Data '{name}' doesn't exist.")

    def Match(self):
        ListUsedToBeRange: list = []
        Matched: list = []
        RandomName: str = None
        RandomObject: str = None

        # get the list which is used to be the range
        if len(self.NamesList) > len(self.ObjectsList):
            ListUsedToBeRange = self.cur_ObjectsList
        else:
            ListUsedToBeRange = self.cur_NamesList

        if self.cur_NamesList and self.cur_ObjectsList:
            # match
            for i in range(len(ListUsedToBeRange)):
                # random choose
                RandomName = random.choice(self.cur_NamesList)
                RandomObject = random.choice(self.cur_ObjectsList)

                # add to list
                Matched.append([RandomName, RandomObject])

                # remove from list
                self.cur_NamesList.remove(RandomName)
                self.cur_ObjectsList.remove(RandomObject)

            # print result
            print("\n======================")
            for i in range(len(Matched)):
                print(", ".join(Matched[i]))
            print("======================\n")
        else:
            print("\nCannot run match command due to the empty list(s).\n")

        # reset
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
                print("\nCannot run 'clear name' command due to the empty list.\n")
                gv.ResultMessage = gv.ResultMessage = "\nCannot Run 'clear name' Function\n"

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
                print("\nCannot run 'clear object' command due to the empty list.\n")
                gv.ResultMessage = "\nCannot Run 'clear object' Function\n"

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
                print("\nCannot run 'clear all' command due to the empty list(s).\n")
                gv.ResultMessage = "\nCannot Run 'clear all' Function\n"

        else:
            print(f"\nUnexpected arg names {data}.\nPlease make sure that you entered correct command.\n")
            isDataCorrect = False

        if isDataCorrect and AbleToPrint:
            print(f"\n====================\nCleared {data}\n====================\n")
            gv.ResultMessage = f"\nCleared {data}\n"

    def help(self, command):
        IndexCheck: int = None

        if command is None:
            print("\n- Commands List -")
            for i in range(len(fm.CmdList['cmds'])):
                print(f"{fm.CmdList['cmds'][i]}: {fm.CmdExpl['expl'][i]}")
            print("")
        else:
            # check if command is found and record its index
            for i in range(len(fm.CmdList['cmds'])):
                if command == fm.CmdList['cmds'][i]:
                    IndexCheck = i

            if IndexCheck is not None:
                print(f"\nCommand - {fm.CmdList['cmds'][IndexCheck]}\n{fm.CmdExpl['detail'][IndexCheck]}\n")
            else:
                print(f"\nCommand '{command}' is not found.\n")

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