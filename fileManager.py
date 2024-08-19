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
pygame.mixer.init()

class FileManager:
    # rf means the original file
    def __init__(self):
        # images
        self.icon = pygame.image.load(os.path.join("ProgramData", "resources", "icon_original.png"))
        self.splash_Lonely_Work = pygame.image.load(os.path.join("ProgramData", "resources", "splash_Lonely_Work.png"))
        self.splash_lw_mark = pygame.image.load(os.path.join("ProgramData", "resources", "LonelyWork_Mark.png"))
        self.splash_black_block = pygame.image.load(os.path.join("ProgramData", "resources", "splash_black_block.png"))
        self.splash_black_block = pygame.transform.scale(self.splash_black_block, (400, 500))
        self.splash_lw_text = pygame.image.load(os.path.join("ProgramData", "resources", "LonelyWork_Text.png"))
        self.button_normal = pygame.image.load(os.path.join("ProgramData", "resources", "button_normal.png"))
        self.button_chose = pygame.image.load(os.path.join("ProgramData", "resources", "button_chose.png"))
        self.button_pressed = pygame.image.load(os.path.join("ProgramData", "resources", "button_pressed.png"))
        self.button_short_normal = pygame.image.load(os.path.join("ProgramData", "resources", "button_short_normal.png"))
        self.button_short_chose = pygame.image.load(os.path.join("ProgramData", "resources", "button_short_chose.png"))
        self.button_short_pressed = pygame.image.load(os.path.join("ProgramData", "resources", "button_short_pressed.png"))
        self.input_field = pygame.image.load(os.path.join("ProgramData", "resources", "input_field.png"))
        self.button_enter_normal = pygame.image.load(os.path.join("ProgramData", "resources", "button_enter_normal.png"))
        self.button_enter_chose = pygame.image.load(os.path.join("ProgramData", "resources", "button_enter_chose.png"))
        self.button_enter_pressed = pygame.image.load(os.path.join("ProgramData", "resources", "button_enter_pressed.png"))
        self.button_disabled = pygame.image.load(os.path.join("ProgramData", "resources", "button_disabled.png"))
        self.button_short_disabled = pygame.image.load(os.path.join("ProgramData", "resources", "button_short_disabled.png"))
        self.button_lang_next_normal = pygame.image.load(os.path.join("ProgramData", "resources", "button_lang_next_normal.png"))
        self.button_lang_next_chose = pygame.image.load(os.path.join("ProgramData", "resources", "button_lang_next_chose.png"))
        self.button_lang_next_pressed = pygame.image.load(os.path.join("ProgramData", "resources", "button_lang_next_pressed.png"))
        self.button_lang_previous_normal = pygame.image.load(os.path.join("ProgramData", "resources", "button_lang_previous_normal.png"))
        self.button_lang_previous_chose = pygame.image.load(os.path.join("ProgramData", "resources", "button_lang_previous_chose.png"))
        self.button_lang_previous_pressed = pygame.image.load(os.path.join("ProgramData", "resources", "button_lang_previous_pressed.png"))

        # fonts
        self.default_text_font = pygame.font.Font(os.path.join("ProgramData", "resources", "default.ttf"), 35)
        self.dev_text_font = pygame.font.SysFont("Arial", 20, italic=True)

        # additional stuff
        self.LoadFolder = os.listdir(os.path.join("Load"))
        try:
            self.LoadFolder.remove("info")
        except ValueError:
            pass    # remove the note from the list

        self.LangFolder = os.listdir(os.path.join("ProgramData", "lang"))
        self.LangFolder.remove("info.json")
        self.LangInfo = json.load(open(os.path.join("ProgramData", "lang", "info.json"), encoding='utf8'))

        # open file
        self.rf_Names = open(os.path.join("UserData", "Names.json"), encoding='utf8')
        self.rf_Objects = open(os.path.join("UserData", "Objects.json"), encoding='utf8')
        self.rf_Commands = open(os.path.join("ProgramData", "Commands.json"))
        self.rf_CmdExplanation = open(os.path.join("ProgramData", "CommandsExplanation.json"))
        self.rf_Errors = open(os.path.join("ProgramData", "Errors.json"))
        self.rf_Settings = open(os.path.join("UserData", "Settings.json"))

        # json load
        self.NamesData = json.load(self.rf_Names)
        self.ObjectsData = json.load(self.rf_Objects)
        self.CmdList = json.load(self.rf_Commands)
        self.CmdExpl = json.load(self.rf_CmdExplanation)
        self.Errors = json.load(self.rf_Errors)
        self.Settings = json.load(self.rf_Settings)

        # close file
        self.rf_Names.close()
        self.rf_Objects.close()
        self.rf_Commands.close()
        self.rf_CmdExplanation.close()
        self.rf_Errors.close()
        self.rf_Settings.close()

        # lang file
        self.LangFile_msg = json.load(open(os.path.join("ProgramData", "lang", self.Settings["Language"], "message.json"), encoding='utf8'))
        self.LangFile_ui = json.load(open(os.path.join("ProgramData", "lang", self.Settings["Language"], "ui.json"), encoding='utf8'))
        self.LangDisplayNames: list = []
        self.Lang_DisplayNameSetup()

        # sound
        self.mus_Static = os.path.join("ProgramData", "resources", "en_es.ogg")    # copyright by Steve Lacy

    def Lang_Reload(self):
        self.LangFile_msg = json.load(open(os.path.join("ProgramData", "lang", self.Settings["Language"], "message.json"), encoding='utf8'))
        self.LangFile_ui = json.load(open(os.path.join("ProgramData", "lang", self.Settings["Language"], "ui.json"), encoding='utf8'))

    def Lang_DisplayNameSetup(self):
        self.LangDisplayNames.clear()
        for idx, digit in enumerate(self.LangFolder):
            self.LangDisplayNames.append(self.LangInfo[digit])

        return False    # why the fuck return False here?

    def LoadDir_Reload(self):
        self.LoadFolder = os.listdir(os.path.join("Load"))
        try:
            self.LoadFolder.remove("info")
        except ValueError:
            pass

    def Lang_isVerified(self, lang_code) -> str:
        if self.LangInfo['isVerified'][lang_code]:
            return "★"
        else:
            return ""

        # this method returns the verified icon if the target lang is verified