# import python modules
import os
import json
import random

# import json files
import fileManager
fm = fileManager.FileManager()

# main
class Core:
    def __init__(self):
        self.StudentsList: list = fm.StudentsData['Students']
        self.ObjectsList: list = fm.ObjectsData['Objects']
        self.cur_NamesList: list = []
        self.cur_ObjectsList: list = []
        self.StudentToRemove: str = None
        self.ListDebugNum: int = 0
        self.RandomName: str = None
        self.RandomObject: str = None
        self.Matched: list = []
        self.ListUsedToBeRange: list = None
        self.isExist: bool = False

    def AddNewStudent(self, name: str) -> object:
        # program data
        self.StudentsList.append(name)
        self.cur_NamesList.append(name)

        # save data
        fm.StudentsData['Students'] = self.StudentsList
        with open(os.path.join("UserData", "Students.json"), "w") as file:
            json.dump(fm.StudentsData, file)

        # print current list
        print(f'There {self.ListLenType(self.StudentsList)}: \n{", ".join(self.StudentsList)} \nin the list.\n')

    def RemoveStudent(self, name: str):
        for i in range(len(self.StudentsList)):
            if name == self.StudentsList[i]:
                self.isExist = True

        if self.isExist:
            # program data
            self.StudentsList.remove(name)
            self.cur_NamesList.remove(name)

            # save data
            fm.StudentsData['Students'] = self.StudentsList
            with open(os.path.join("UserData", "Students.json"), "w") as file:
                json.dump(fm.StudentsData, file)

            # print current list
            print(f'There {self.ListLenType(self.StudentsList)}: \n{", ".join(self.StudentsList)} \nin the list.\n')
        else:
            print("Name not found.")

        self.isExist = False

    def AddNewObject(self, name: str):
        # program data
        self.ObjectsList.append(name)
        self.cur_ObjectsList.append(name)

        # save data
        fm.ObjectsData['Objects'] = self.ObjectsList
        with open(os.path.join("UserData", "Objects.json"), "w") as file:
            json.dump(fm.ObjectsData, file)

        # print current list
        print(f'There {self.ListLenType(self.ObjectsList)}: \n{", ".join(self.ObjectsList)} \nin the list.\n')

    def RemoveObject(self, name: str):
        for i in range(len(self.ObjectsList)):
            if name == self.ObjectsList[i]:
                self.isExist = True

        if self.isExist:
            # program data
            self.ObjectsList.remove(name)
            self.cur_ObjectsList.remove(name)

            # save data
            fm.ObjectsData['Objects'] = self.ObjectsList
            with open(os.path.join("UserData", "Objects.json"), "w") as file:
                json.dump(fm.ObjectsData, file)

            # print current list
            print(f'There {self.ListLenType(self.ObjectsList)}: \n{", ".join(self.ObjectsList)} \nin the list.\n')
        else:
            print("\nObject not found.\n")

        self.isExist = False

    def Match(self):
        # get the list which is used to be the range
        if len(self.StudentsList) > len(self.ObjectsList):
            self.ListUsedToBeRange = self.cur_ObjectsList
        else:
            self.ListUsedToBeRange = self.cur_NamesList

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

        # reset
        self.Matched.clear()
        self.CurListDataSetup()

    def clear(self, data: str):
        if data == "name":
            # program data
            self.StudentsList.clear()

            # save data
            fm.StudentsData['Students'] = self.StudentsList
            with open(os.path.join("UserData", "Students.json"), "w") as file:
                json.dump(fm.StudentsData, file)

        elif data == "obj":
            # program data
            self.ObjectsList.clear()

            # save data
            fm.ObjectsData['Objects'] = self.ObjectsList
            with open(os.path.join("UserData", "Objects.json"), "w") as file:
                json.dump(fm.ObjectsData, file)

        elif data == "all":
            # program data
            self.StudentsList.clear()
            self.ObjectsList.clear()

            # save data
            fm.StudentsData['Students'] = self.StudentsList
            with open(os.path.join("UserData", "Students.json"), "w") as file:
                json.dump(fm.StudentsData, file)

            fm.ObjectsData['Objects'] = self.ObjectsList
            with open(os.path.join("UserData", "Objects.json"), "w") as file:
                json.dump(fm.ObjectsData, file)

        print(f"\n====================\nCleared {data}\n====================\n")

    def ListLenType(self, TargetList: list):
        if len(TargetList) > 1:
            return "are"
        else:
            return "is"

    def CurListDataSetup(self):
        self.cur_NamesList.clear()
        self.cur_ObjectsList.clear()

        for i in range(len(self.StudentsList)):
            self.cur_NamesList.append(self.StudentsList[i])

        for i in range(len(self.ObjectsList)):
            self.cur_ObjectsList.append(self.ObjectsList[i])

    def PrintListContent(self):
        print(f"Names List: {self.StudentsList}\n"
              f"Objects List: {self.ObjectsList}\n"
              f"Current Names List: {self.cur_NamesList}\n"
              f"Current Objects List: {self.cur_ObjectsList}")