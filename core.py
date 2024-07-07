# import python modules
import os
import json

# import json files
import fileManager
fm = fileManager.FileManager()

# main
class Core:
    def __init__(self):
        self.StudentsList: list = fm.StudentsData['Students']
        self.ObjectsList: list = fm.ObjectsData['Objects']
        self.StudentToRemove: str = None
        self.ListDebugNum: int = 0

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