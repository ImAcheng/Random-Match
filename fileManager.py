# import python modules
import os
import json
import sys
import pygame

# setup
if getattr(sys, 'frozen', False):
    ScriptDirection = os.path.dirname(sys.executable)
else:
    ScriptDirection = os.path.dirname(os.path.realpath(__file__))

os.chdir(ScriptDirection)

pygame.font.init()

class FileManager:
    # rf means the original file
    def __init__(self):
        # images
        self.icon = pygame.image.load(os.path.join("ProgramData", "resources", "icon_original.png"))
        self.button_normal = pygame.image.load(os.path.join("ProgramData", "resources", "button_normal.png"))
        self.button_chose = pygame.image.load(os.path.join("ProgramData", "resources", "button_chose.png"))
        self.button_pressed = pygame.image.load(os.path.join("ProgramData", "resources", "button_pressed.png"))
        self.button_short_normal = pygame.image.load(os.path.join("ProgramData", "resources", "button_short_normal.png"))
        self.button_short_chose = pygame.image.load(os.path.join("ProgramData", "resources", "button_short_chose.png"))
        self.button_short_pressed = pygame.image.load(os.path.join("ProgramData", "resources", "button_short_pressed.png"))
        self.input_field = pygame.image.load(os.path.join("ProgramData", "resources", "input_field.png"))

        # fonts
        self.default_text_font = pygame.font.Font(os.path.join("ProgramData", "resources", "default.ttf"), 35)
        self.dev_text_font = pygame.font.SysFont("Arial", 20, italic=True)

        # open file
        self.rf_Names = open(os.path.join("UserData", "Names.json"), encoding='utf8')
        self.rf_Objects = open(os.path.join("UserData", "Objects.json"), encoding='utf8')
        self.rf_Commands = open(os.path.join("ProgramData", "Commands.json"))
        self.rf_CmdExplanation = open(os.path.join("ProgramData", "CommandsExplanation.json"))
        self.rf_Errors = open(os.path.join("ProgramData", "Errors.json"))

        # json load
        self.NamesData = json.load(self.rf_Names)
        self.ObjectsData = json.load(self.rf_Objects)
        self.CmdList = json.load(self.rf_Commands)
        self.CmdExpl = json.load(self.rf_CmdExplanation)
        self.Errors = json.load(self.rf_Errors)

        # close file
        self.rf_Names.close()
        self.rf_Objects.close()
        self.rf_Commands.close()
        self.rf_CmdExplanation.close()
        self.rf_Errors.close()