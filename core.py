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
        self.cur_NamesList: list = self.StudentsList
        self.cur_ObjectsList: list = self.ObjectsList
        self.StudentToRemove: str = None
        self.ListDebugNum: int = 0
        self.RandomName: str = None
        self.RandomObject: str = None
        self.Matched: list = []
        self.ListUsedToBeRange: list = None

    def AddNewStudent(self, name: str) -> object:
        # program data
        self.StudentsList.append(name)

        # save data
        fm.StudentsData['Students'] = self.StudentsList
        with open(os.path.join("UserData", "Students.json"), "w") as file:
            json.dump(fm.StudentsData, file)

        # print current list
        print(f'There are: \n{", ".join(self.StudentsList)} \nin the list.\n')

    def RemoveStudent(self, name: str):
        if len(self.StudentsList) > 1:
            self.ListDebugNum = 1
        else:
            self.ListDebugNum = 0

        # program data
        for i in range(len(self.StudentsList) - self.ListDebugNum):
            if self.StudentsList[i] == name:
                self.StudentsList.remove(self.StudentsList[i])

        # save data
        fm.StudentsData['Students'] = self.StudentsList
        with open(os.path.join("UserData", "Students.json"), "w") as file:
            json.dump(fm.StudentsData, file)

        # print current list
        print(f'There are: \n{", ".join(self.StudentsList)} \nin the list.\n')

    def AddNewObject(self, name: str):
        # program data
        self.ObjectsList.append(name)

        # save data
        fm.ObjectsData['Objects'] = self.ObjectsList
        with open(os.path.join("UserData", "Objects.json")) as file:
            json.dump(fm.ObjectsData, file)

        # print current list
        print(f'There are: \n{", ".join(self.StudentsList)} \nin the list.\n')

    def RemoveObject(self, name: str):
        # debug
        if len(self.StudentsList) > 1:
            self.ListDebugNum = 1
        else:
            self.ListDebugNum = 0

        # program data
        for i in range(len(self.ObjectsList) - self.ListDebugNum):
            if self.ObjectsList[i] == name:
                self.ObjectsList.remove(self.ObjectsList[i])
            i += 1

        # save data
        fm.ObjectsData['Objects'] = self.ObjectsList
        with open(os.path.join("UserData", "Objects.json"), "w") as file:
            json.dump(fm.ObjectsData, file)

        # print current list
        print(f'There are: \n{", ".join(self.StudentsList)} \nin the list.\n')

    def Match(self):
        # get the list which is used to be the range
        if len(self.StudentsList) > len(self.ObjectsList):
            self.ListUsedToBeRange = self.cur_ObjectsList
        else:
            self.ListUsedToBeRange = self.cur_NamesList

        # match
        for i in range(len(self.ListUsedToBeRange)):
            # random choose
            self.RandomName = random.choice(self.StudentsList)
            self.RandomObject = random.choice(self.ObjectsList)

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
        self.StudentsList = json.load(open((os.path.join("UserData", "Students.json")), encoding='utf8'))['Students']
        self.ObjectsList = json.load(open((os.path.join("UserData", "Objects.json")), encoding='utf8'))['Objects']
        self.cur_NamesList = self.StudentsList
        self.cur_ObjectsList = self.ObjectsList

        # TODO: figure out why why remove data from the cur_ list also clear the original list