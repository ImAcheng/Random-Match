# import python modules
import os
import json
import sys

# setup
if getattr(sys, 'frozen', False):
    ScriptDirection = os.path.dirname(sys.executable)
else:
    ScriptDirection = os.path.dirname(os.path.realpath(__file__))

os.chdir(ScriptDirection)

class FileManager:
    # rf means the original file
    def __init__(self):
        # open file
        self.rf_Names = open(os.path.join("UserData", "Names.json"), encoding='utf8')
        self.rf_Objects = open(os.path.join("UserData", "Objects.json"), encoding='utf8')
        self.rf_Commands = open(os.path.join("ProgramData", "Commands.json"))
        self.rf_CmdExplanation = open(os.path.join("ProgramData", "CommandsExplanation.json"))

        # json load
        self.NamesData = json.load(self.rf_Names)
        self.ObjectsData = json.load(self.rf_Objects)
        self.CmdList = json.load(self.rf_Commands)
        self.CmdExpl = json.load(self.rf_CmdExplanation)

        # close file
        self.rf_Names.close()
        self.rf_Objects.close()
        self.rf_Commands.close()
        self.rf_CmdExplanation.close()

print(os.path.dirname(os.path.realpath(__file__)))