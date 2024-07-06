# import python modules
import os
import json

# load files
StudentsListFile = json.load(open(os.path.join("UserData", "Students.json"), encoding='utf8'))

# main
class Core:
    def __init__(self):
        self.StudentsList: list = StudentsListFile['Students']

    def AddNewStudent(self, name: str):
        # program data
        self.StudentsList.append(name)

        # save data
        StudentsListFile['Students'] = self.StudentsList
        with open(os.path.join("UserData", "Students.json"), "w") as file:
            json.dump(StudentsListFile, file)

    def RemoveStudent(self, name: str):
        # program data
        for i in range(len(self.StudentsList) - 1):
            if self.StudentsList[i] == name:
                self.StudentsList.remove(self.StudentsList[i])
            i += 1

        # save data
        StudentsListFile['Students'] = self.StudentsList
        with open(os.path.join("UserData", "Students.json"), "w") as file:
            json.dump(StudentsListFile, file)