# import python modules
import os
import json

# rf means the original file

class FileManager:
    def __init__(self):
        # open file
        self.rf_Students = open(os.path.join("UserData", "Students.json"), encoding='utf8')
        self.rf_Objects = open(os.path.join("UserData", "Objects.json"), encoding='utf8')

        # json load
        self.StudentsData = json.load(self.rf_Students)
        self.ObjectsData = json.load(self.rf_Objects)

        # close file
        self.rf_Students.close()
        self.rf_Objects.close()