# import modules
import json
import os.path
import time
import pygame

from pygame import set_error

# import other python files
import fileManager
import button
import text
import gloabalVars as gv
import inputField
from commandLogic import ProcessCommand
import enores
from animation import LonelyWorkMark
from checkBox import CheckBox, ResPacksCheckBox

# setup
fM = fileManager.FileManager()
Button = button.Button
EnterButton = button.EnterButton
LangButton = button.LangChoosingButton
ResButton = button.ResChoosingButton
newText = text.newText
inputField = inputField.InputField
checkBox = CheckBox
resCB = ResPacksCheckBox

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Random Match")
pygame.display.set_icon(fM.icon)
LW_mark = LonelyWorkMark()

class Window:
    def __init__(self):
        # vars
        self.clock = pygame.time.Clock()
        self.userInputString: list = []
        self.command: str = None
        self.key_pressed = pygame.key.get_pressed()
        self.BackSpaceHoldingTime: int = 0
        self.AbleToAutoDeletingWords: bool = False
        self.AutoDeletingWordsDelay: int = 0
        self.PageName: str = "Splash"
        self.TestTime: int = 0
        self.ErrorCode: int = -1
        self.ErrorExplanation = fM.Errors['errors']
        self.LoadDirIndex: int = 0
        self.LangDirIndex: int = fM.LangFolder.index(fM.Settings['Language'])
        self.DevInfo = fM.Settings['Develop_Info']
        self.SplashPlayingTime: int = 0
        self.inProgram: bool = False
        self.isStaticPlayed: bool = False
        self.selected_lang = fM.Settings['Language']
        self.PlayNewSplash: bool = fM.Settings['New_Splash']
        self.play_enores_snd: bool = fM.Settings['enores_snd']
        self.MatchedListIndex: int = 0

        self.NormalButtonTextures: tuple = (fM.Textures['button_normal'], fM.Textures['button_chose'], fM.Textures['button_pressed'],
                                            fM.Textures['button_short_normal'], fM.Textures['button_short_chose'], fM.Textures['button_short_pressed'],
                                            fM.Textures['button_disabled'], fM.Textures['button_short_disabled'])
        self.EnterButtonTextures: tuple = (fM.Textures['button_enter_normal'],
                                           fM.Textures['button_enter_chose'],
                                           fM.Textures['button_enter_pressed'])
        self.LangChooseButtonTextures: tuple = (fM.Textures['button_lang_next_normal'], fM.Textures['button_lang_next_chose'], fM.Textures['button_lang_next_pressed'],
                                                fM.Textures['button_lang_previous_normal'], fM.Textures['button_lang_previous_chose'], fM.Textures['button_lang_previous_pressed'])
        self.InputFieldTextures: tuple = (fM.Textures['input_field'])
        self.CheckBoxTextures: tuple = (fM.Textures['check_box_normal'], fM.Textures['check_box_chose'],
                                        fM.Textures['check_box_normal_checked'], fM.Textures['check_box_chose_checked'])
        self.ResButtonTextures: tuple = (fM.Textures['button_go_previous_normal'], fM.Textures['button_go_previous_chosen'], fM.Textures['button_go_previous_pressed'],
                                         fM.Textures['button_go_next_normal'], fM.Textures['button_go_next_chosen'], fM.Textures['button_go_next_pressed'])
        self.ResCheckBoxTextures: tuple = (fM.Textures['check_box_res_normal'],
                                           fM.Textures['check_box_res_chosen'],
                                           fM.Textures['check_box_res_using'])

        # settings
        self.settings_content = fM.Settings

        # UI elements
        self.bt_GoToMainFn = Button(400, 200, [350, 80], self.GoToMainFnPage, True)
        self.bt_GoToHelp = Button(400, 300, [350, 80], self.GoToHelpPage, True)
        self.bt_GoToSetting = Button(400, 400, [350, 80], self.GoToSettingsPage, True)
        self.bt_StopProgram = Button(400, 500, [350, 80], self.StopProgram, True)
        self.bt_Match = Button(400, 200, [350, 80], self.GoToMatchPage, True)
        self.bt_Match_AtoB = Button(400, 200, [350, 80], self.Command_Match, True)
        self.bt_Add = Button(300, 300, [150, 80], self.GoToAddPage, True)
        self.bt_Remove = Button(500, 300, [150, 80], self.GoToRemovePage, True)
        self.bt_Load = Button(300, 400, [150, 80], self.GoToLoadPage, True)
        self.bt_Clear = Button(500, 400, [150, 80], self.GoToCleanPage, True)
        self.bt_BackToHome = Button(400, 500, [350, 80], self.GoToHomePage, True)
        self.bt_ChooseName = Button(400, 200, [350, 80], self.GoToInputWithName, True)
        self.bt_ChooseObject = Button(400, 300, [350, 80], self.GoToInputWithObject, True)
        self.bt_clear_ChooseName = Button(400, 200, [350, 80], self.Command_Clear_Name, True)
        self.bt_clear_ChooseObject = Button(400, 300, [350, 80], self.Command_Clear_Object, True)
        self.bt_clear_ChooseAll = Button(400, 400, [350, 80], self.Command_Clear_All, True)
        self.bt_Cancel = Button(400, 500, [350, 80], self.Command_Cancel, True)
        self.bt_Confirm = Button(400, 300, [350, 80], self.Command_Process, True)
        self.bt_InputEnter = EnterButton(573, 260, [54, 54], self.Process_Input_Field_Ctx)
        self.bt_Browse_File_Next = Button(500, 300, [150, 80], self.LoadDirNext, True)
        self.bt_Browse_File_Previous = Button(300, 300, [150, 80], self.LoadDirPrevious, True)
        self.bt_Load_File_Select = Button(400, 400, [350, 80], self.Command_Load_Target_File, True)
        self.bt_load_ChooseName = Button(400, 200, [350, 80], self.GoToFileBrowserWithName, True)
        self.bt_load_ChooseObject = Button(400, 300, [350, 80], self.GoToFileBrowserWithObject, True)
        self.bt_easter_egg = Button(700, 500, [150, 80], self.GoToFixesPage, True)
        self.bt_setting_lang = Button(400, 200, [350, 80], self.GoToSettingLangPage, True)
        self.bt_return_settings = Button(400, 500, [350, 80], self.ReturnToSettings, True)
        self.bt_lang_select = Button(400, 400, [350, 80], self.LangSelect, True)
        self.bt_previous_lang = LangButton(600, 230, "previous", self.PreviousLang)
        self.bt_next_lang = LangButton(600, 305, "next", self.NextLang)
        self.bt_GoToSettingAdvanced = Button(400, 400, [350, 80], self.GoToSettingsAdvancedPage, True)
        self.bt_GoToResourcePacks = Button(400, 300, [350, 80], self.GoToSettingsResourcePacksPage, True)
        self.bt_ResPrevious = ResButton(700, 200, "up", self.ResPrevious)
        self.bt_ResNext = ResButton(700, 400, "down", self.ResNext)
        self.bt_MatchedPrevious = ResButton(700, 250, "up", self.MatchedList_Previous)
        self.bt_MatchedNext = ResButton(700, 350, "down", self.MatchedList_Next)
        self.InputField = inputField(400, 200)
        self.cb_DevInfo = checkBox(175, 170, "Dev Info", self.settings_content, 'Develop_Info', os.path.join("UserData", "Settings.json"))
        self.cb_NewSplashAnimation = checkBox(175, 240, "New Splash Animation", self.settings_content, "New_Splash", os.path.join("UserData", "Settings.json"))
        self.cb_enoresSound = checkBox(175, 310, "Super secret sound", self.settings_content, "enores_snd", os.path.join("UserData", "Settings.json"))
        self.cb_Res1 = resCB(57, 178, 0)
        self.cb_Res2 = resCB(57, 263, 0)
        self.cb_Res3 = resCB(57, 348, 0)

    def update(self):
        self.clock.tick(60)

        # get input
        if pygame.mouse.get_pressed()[0]:
            gv.LeftButtonPressingTime += 1
        else:
            gv.LeftButtonPressingTime = 0   # handle the repeating executing command problem

        # handle the holding backspace function
        self.AutoDeletingWords()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                gv.isProgramRunning = False

            if ev.type == pygame.KEYDOWN:
                # reload textures test key
                if ev.key == pygame.K_r:
                    fM.Resource_Pack_Reload()
                    self.ReloadTextures()

            # user input
            # keyboard input system
            if self.PageName == "Input":
                if ev.type == pygame.KEYDOWN:
                    NotActualInputChr: list = [
                        ev.key == pygame.K_BACKSPACE,
                        ev.key == pygame.K_RETURN
                    ]

                    NotAlphabet: list = [
                        ev.key < 65,
                        ev.key < 90 and ev.key < 97,
                        ev.key > 122
                    ]

                    try:
                        if ev.key == pygame.K_BACKSPACE and self.userInputString:
                            self.userInputString.pop()
                        elif not any(NotActualInputChr):
                            if self.isShiftHolding():
                                # uppercase
                                if not any(NotAlphabet):
                                    self.userInputString.append(chr(ev.key - 32))

                                # symbols
                                if chr(ev.key) == "1":
                                    self.userInputString.append("!")
                                if chr(ev.key) == "2":
                                    self.userInputString.append("@")
                                if chr(ev.key) == "3":
                                    self.userInputString.append("#")
                                if chr(ev.key) == "4":
                                    self.userInputString.append("$")
                                if chr(ev.key) == "5":
                                    self.userInputString.append("%")
                                if chr(ev.key) == "6":
                                    self.userInputString.append("^")
                                if chr(ev.key) == "7":
                                    self.userInputString.append("&")
                                if chr(ev.key) == "8":
                                    self.userInputString.append("*")
                                if chr(ev.key) == "9":
                                    self.userInputString.append("(")
                                if chr(ev.key) == "0":
                                    self.userInputString.append(")")
                                if chr(ev.key) == ";":
                                    self.userInputString.append(":")
                                if chr(ev.key) == "'":
                                    self.userInputString.append(chr(34))
                                if chr(ev.key) == ",":
                                    self.userInputString.append("<")
                                if chr(ev.key) == ".":
                                    self.userInputString.append(">")
                                if chr(ev.key) == "/":
                                    self.userInputString.append("?")

                            else:
                                # lowercase
                                self.userInputString.append(chr(ev.key))
                    except ValueError:
                        pass

        # window
        screen.fill('#aabdc1')

        # draw pages
        self.DrawPages()

        if self.inProgram:
            screen.blit(fM.Textures['title_random_match'], (163, 60))
            newText(screen, "©2024 Lonely Work (Lonely Acheng) All Rights Reserved.", fM.default_text_font, "#FFFFFF", 790, 590, 0.5, 'bottomright', shaderOn=False)
            newText(screen, f"Random Match Release 2.1.1", fM.default_text_font, "#FFFFFF", 10, 10, 0.6, 'topleft')

        if self.DevInfo:
            self.draw_DevInfo()

        self.CursorStatementCheckAndChange()

        # update
        pygame.display.update()
        self.SolveEnglishOrSpanish()

    def DrawPages(self):
        try:
            match self.PageName:
                case "Splash":
                    self.draw_Splash()
                case "Home":
                    self.draw_HomePage()
                case "MainFn":
                    self.draw_MainFnPage()
                case "Help":
                    self.draw_HelpPage()
                case "Add":
                    self.draw_AddPage()
                case "Remove":
                    self.draw_RemovePage()
                case "Input":
                    self.draw_InputPage()
                case "Clean":
                    self.draw_ClearPage()
                case "Confirm":
                    self.draw_ConfirmPage()
                case "Result":
                    self.draw_ResultPage()
                case "Load":
                    self.draw_LoadPage()
                case "Browse":
                    self.draw_LoadFileBrowser()
                case "Fixes":
                    self.draw_FixesPage()
                case "Settings":
                    self.draw_SettingsPage()
                case "Settings_Lang":
                    self.draw_LangPage()
                case "Settings_Advanced":
                    self.draw_SettingsAdvanced()
                case "Settings_ResourcePacks":
                    self.draw_SettingsResourcePacks()
                case "Match_Options":
                    self.draw_MatchOptions()
                case "Match_AtoB":
                    self.draw_Match_AtoB_RandResult_Page()

                case "FnDisabled":
                    self.draw_ErrorPage()
                    self.ErrorCode = 2
                case "Error":
                    self.draw_ErrorPage()
                case _:
                    self.draw_ErrorPage()
                    self.ErrorCode = 1
        except Exception as error:
            self.draw_ErrorPage()
            self.ErrorCode = 0
            gv.detected_unknown_error = error

    def isShiftHolding(self) -> bool:
        return pygame.key.get_mods() & pygame.KMOD_SHIFT

    def isBackSpaceHolding(self) -> bool:
        return pygame.key.get_pressed()[pygame.K_BACKSPACE]

    def AutoDeletingWords(self):
        if self.isBackSpaceHolding():
            self.BackSpaceHoldingTime += 1
        else:
            self.BackSpaceHoldingTime = 0

        if self.isBackSpaceHolding() and self.BackSpaceHoldingTime >= 30:
            self.AbleToAutoDeletingWords = True
            self.AutoDeletingWordsDelay += 1
        else:
            self.AbleToAutoDeletingWords = False
            self.AutoDeletingWordsDelay = 0

        if self.AbleToAutoDeletingWords and self.AutoDeletingWordsDelay > 2:
            try:
                self.userInputString.pop()
            except IndexError:
                pass
            self.AutoDeletingWordsDelay = 0

    def draw_Splash(self):
        if self.SplashPlayingTime < 240:
            if self.PlayNewSplash:
                screen.blit(pygame.transform.scale(fM.splash_black_block, (800, 600)), (0, 0))
                LW_mark.draw(screen)
            else:
                screen.blit(fM.splash_Lonely_Work, (0, 0))
        self.SplashPlayingTime += 1

        if self.SplashPlayingTime >= 240:
            self.inProgram = True
            self.PageName = "Home"

    def StopProgram(self):
        gv.isProgramRunning = False

    def GoToFixesPage(self):
        self.PageName = "Fixes"

    def draw_FixesPage(self):
        newText(screen, "Uhh... I just removed something that I forgot to delete.", fM.default_text_font, (0, 0, 0), 400, 200, 0.7, 'center')
        newText(screen, "Also, I do actually forgot to rename the version, too.", fM.default_text_font, (0, 0, 0), 400, 230, 0.7, 'center')
        newText(screen, "Anyways, I fixed them.", fM.default_text_font, (0, 0, 0), 400, 260, 0.7, 'center')
        self.bt_BackToHome.draw(screen, fM.LangFile_ui['bt_return'], self.NormalButtonTextures)

    def GoToHomePage(self):
        self.PageName = "Home"

    def draw_HomePage(self):
        self.bt_GoToMainFn.draw(screen, fM.LangFile_ui['bt_mainFn'], self.NormalButtonTextures)
        self.bt_GoToHelp.draw(screen, fM.LangFile_ui['bt_help'], self.NormalButtonTextures)
        self.bt_GoToSetting.draw(screen, fM.LangFile_ui['bt_setting'], self.NormalButtonTextures)
        self.bt_StopProgram.draw(screen, fM.LangFile_ui['bt_stop'], self.NormalButtonTextures)

    def GoToMainFnPage(self):
        self.PageName = "MainFn"

    def draw_MainFnPage(self):
        self.bt_Match.draw(screen, fM.LangFile_ui['bt_match'], self.NormalButtonTextures)
        self.bt_Add.draw(screen, fM.LangFile_ui['bt_add'], self.NormalButtonTextures)
        self.bt_Remove.draw(screen, fM.LangFile_ui['bt_remove'], self.NormalButtonTextures)
        self.bt_Load.draw(screen, fM.LangFile_ui['bt_load'], self.NormalButtonTextures)
        self.bt_Clear.draw(screen, fM.LangFile_ui['bt_clear'], self.NormalButtonTextures)
        self.bt_BackToHome.draw(screen, fM.LangFile_ui['bt_return'], self.NormalButtonTextures)

    def GoToHelpPage(self):
        self.PageName = "Help"

    def draw_HelpPage(self):
        newText(screen, fM.LangFile_ui['title_allFn'], fM.default_text_font, (0, 0, 0), 400, 175, 1.25, 'center', shaderOn=False)
        newText(screen, f"- {fM.LangFile_ui['bt_match']}: {fM.LangFile_msg['help_match']}", fM.default_text_font, "#FFFFFF", 20, 200, 0.8, 'topleft')
        newText(screen, f"- {fM.LangFile_ui['bt_add']}: {fM.LangFile_msg['help_add']}", fM.default_text_font, "#FFFFFF", 20, 230, 0.8, 'topleft')
        newText(screen, f"- {fM.LangFile_ui['bt_remove']}: {fM.LangFile_msg['help_remove']}", fM.default_text_font, "#FFFFFF", 20, 260, 0.8, 'topleft')
        newText(screen, f"- {fM.LangFile_ui['bt_clear']}: {fM.LangFile_msg['help_clear']}", fM.default_text_font, "#FFFFFF", 20, 290, 0.8, 'topleft')
        newText(screen, f"- {fM.LangFile_ui['bt_load']}: {fM.LangFile_msg['help_load']}", fM.default_text_font, "#FFFFFF", 20, 320, 0.8, 'topleft')
        self.bt_BackToHome.draw(screen, fM.LangFile_ui['bt_return'], self.NormalButtonTextures)

    def GoToAddPage(self):
        self.command = "add "
        self.PageName = "Add"
        gv.InputFieldType = "name"

    def draw_AddPage(self):
        self.bt_ChooseName.draw(screen, fM.LangFile_ui['bt_toName'], self.NormalButtonTextures)
        self.bt_ChooseObject.draw(screen, fM.LangFile_ui['bt_toObj'], self.NormalButtonTextures)
        self.bt_Cancel.draw(screen, fM.LangFile_ui['bt_cancel'], self.NormalButtonTextures)

    def GoToRemovePage(self):
        self.command = "remove "
        self.PageName = "Remove"
        gv.InputFieldType = "name"

    def draw_RemovePage(self):
        self.bt_ChooseName.draw(screen, fM.LangFile_ui['bt_fromName'], self.NormalButtonTextures)
        self.bt_ChooseObject.draw(screen, fM.LangFile_ui['bt_fromObj'], self.NormalButtonTextures)
        self.bt_Cancel.draw(screen, fM.LangFile_ui['bt_cancel'], self.NormalButtonTextures)

    def GoToInputWithName(self):
        self.command += "name "
        self.PageName = "Input"

    def GoToInputWithObject(self):
        self.command += "object "
        self.PageName = "Input"

    def draw_InputPage(self):
        self.InputField.draw(screen, "".join(self.userInputString), fM.LangFile_ui['input_name'], self.InputFieldTextures)
        self.bt_InputEnter.draw(screen, "Enter", self.EnterButtonTextures)
        self.bt_Cancel.draw(screen, fM.LangFile_ui['bt_cancel'], self.NormalButtonTextures)

        if gv.InputFieldType == "path":
            newText(screen, "You can't use copy & paste due to some skill issues.", fM.default_text_font, "#0F0F0F", 400, 320, 0.6, 'center')
            newText(screen, "But, we're trying to develop a new way to explore files now.", fM.default_text_font, "#0F0F0F", 400, 350, 0.6, 'center')

    def Process_Input_Field_Ctx(self):
        if "".join(self.userInputString) != "":
            self.command += "".join(self.userInputString)
            self.PageName = "Confirm"
        else:
            self.ErrorCode = 3
            self.PageName = "Error"

        # I'm so freakin smart. I complete the whole input and process system with this shit.

    def GoToCleanPage(self):
        self.command = "clear "
        self.PageName = "Clean"

    def draw_ClearPage(self):
        self.bt_clear_ChooseName.draw(screen, fM.LangFile_ui['bt_justName'], self.NormalButtonTextures)
        self.bt_clear_ChooseObject.draw(screen, fM.LangFile_ui['bt_justObj'], self.NormalButtonTextures)
        self.bt_clear_ChooseAll.draw(screen, fM.LangFile_ui['bt_all'], self.NormalButtonTextures)
        self.bt_Cancel.draw(screen, fM.LangFile_ui['bt_cancel'], self.NormalButtonTextures)

    def draw_ConfirmPage(self):
        newText(screen, fM.LangFile_msg['msg_confirm'], fM.default_text_font, "#FFFFFF", 400, 200, 1, 'center')
        self.bt_Confirm.draw(screen, fM.LangFile_ui['bt_confirm'], self.NormalButtonTextures)
        self.bt_Cancel.draw(screen, fM.LangFile_ui['bt_cancel'], self.NormalButtonTextures)

    def GoToResultPage(self):
        self.PageName = "Result"

    def draw_ResultPage(self):
        newText(screen, fM.LangFile_msg[gv.ResultMessage], fM.default_text_font, "#FFFFFF", 400, 200, 0.8, 'center')
        self.bt_Cancel.draw(screen, fM.LangFile_ui['bt_continue'], self.NormalButtonTextures)

    def GoToLoadPage(self):
        self.command = "load "
        self.PageName = "Load"
        gv.InputFieldType = "path"
        fM.LoadDir_Reload()

    def draw_LoadPage(self):
        self.bt_load_ChooseName.draw(screen, fM.LangFile_ui['bt_toName'], self.NormalButtonTextures)
        self.bt_load_ChooseObject.draw(screen, fM.LangFile_ui['bt_toObj'], self.NormalButtonTextures)
        self.bt_Cancel.draw(screen, fM.LangFile_ui['bt_cancel'], self.NormalButtonTextures)

    def GoToBrowseFilePage(self):
        self.PageName = "Browse"

    def draw_LoadFileBrowser(self):
        try:
            newText(screen, fM.LoadFolder[self.LoadDirIndex], fM.default_text_font, "#FFFFFF", 400, 220, 1, 'center')
            newText(screen, fM.LangFile_msg['msg_fileBrowser'], fM.default_text_font, "#000000", 400, 165, 0.8, 'center', shaderOn=False)
            self.bt_Browse_File_Next.draw(screen, "→", self.NormalButtonTextures)
            self.bt_Browse_File_Previous.draw(screen, "←", self.NormalButtonTextures)
            self.bt_Load_File_Select.draw(screen, fM.LangFile_ui['bt_select'], self.NormalButtonTextures)
            self.bt_Cancel.draw(screen, fM.LangFile_ui['bt_cancel'], self.NormalButtonTextures)
        except IndexError:
            self.ErrorCode = 4
            self.PageName = "Error"

        if self.LoadDirIndex == 0:
            self.bt_Browse_File_Previous.isEnabled = False
        else:
            self.bt_Browse_File_Previous.isEnabled = True

        if self.LoadDirIndex == len(fM.LoadFolder) - 1:
            self.bt_Browse_File_Next.isEnabled = False
        else:
            self.bt_Browse_File_Next.isEnabled = True

    def draw_ErrorPage(self):
        screen.fill('#aabdc1')
        newText(screen, ":(", fM.default_text_font, (255, 255, 255), 150, 230, 4, 'center', shaderOn=False)
        newText(screen, fM.LangFile_msg['msg_error_appears'], fM.default_text_font, (255, 255, 255), 100, 320, 0.75, 'topleft')
        newText(screen, f"{fM.LangFile_msg['msg_error_code']}: [{self.ErrorCode} ({self.ErrorExplanation[str(self.ErrorCode)]})]", fM.default_text_font, (255, 255, 255), 100, 350, 0.75, 'topleft')
        self.bt_BackToHome.draw(screen, fM.LangFile_ui['bt_continue'], self.NormalButtonTextures)

    def FunctionNotAvailable(self):
        self.PageName = "FnDisabled"

    def Command_Clear_Name(self):
        self.command += "name"
        self.GoToConfirmPage()

    def Command_Clear_Object(self):
        self.command += "object"
        self.GoToConfirmPage()

    def Command_Clear_All(self):
        self.command += "all"
        self.GoToConfirmPage()

    def Command_Match(self):
        self.command = "match"
        self.GoToMatchAtoB_Result_Page()

    def Command_Cancel(self):
        self.command = None
        self.userInputString.clear()
        gv.ResultMessage = None
        gv.Matched_Groups.clear()
        self.MatchedListIndex = 0
        self.PageName = "MainFn"

    def Command_Process(self):
        try:
            ProcessCommand(self.command)
            self.GoToResultPage()
        except TypeError:
            self.ErrorCode = 3
            self.PageName = "Error"

    def LoadDirNext(self):
        if self.LoadDirIndex < len(fM.LoadFolder) - 1:
            self.LoadDirIndex += 1

    def LoadDirPrevious(self):
        if self.LoadDirIndex > 0:
            self.LoadDirIndex -= 1

    def Command_Load_Target_File(self):
        self.command += fM.LoadFolder[self.LoadDirIndex]
        self.GoToConfirmPage()

    def GoToFileBrowserWithName(self):
        self.command += "name "
        self.PageName = "Browse"

    def GoToFileBrowserWithObject(self):
        self.command += "object "
        self.PageName = "Browse"

    def GoToConfirmPage(self):
        self.PageName = "Confirm"

    def draw_DevInfo(self):
        newText(screen, f"[Dev Info]", fM.dev_text_font, "#d8d8d8", 790, 30, 1, 'bottomright', shaderOn=False)
        newText(screen, f"command: {self.command}", fM.dev_text_font, "#d8d8d8", 790, 50, 1, 'bottomright', shaderOn=False)
        newText(screen, f"LeftButtonPressingTime: {gv.LeftButtonPressingTime}", fM.dev_text_font, "#d8d8d8", 790, 70, 1, 'bottomright', shaderOn=False)
        newText(screen, f"isCursorInAnyButton: {self.CursorStatementCheckAndChange()}", fM.dev_text_font, "#d8d8d8", 790, 90, 1, 'bottomright', shaderOn=False)
        newText(screen, f"PageName: {self.PageName}", fM.dev_text_font, "#d8d8d8", 790, 110, 1, 'bottomright', shaderOn=False)
        newText(screen, f"LastDetectedUnknownError: {gv.detected_unknown_error}", fM.dev_text_font, "#d8d8d8", 790, 130, 1, 'bottomright', shaderOn=False)

    def PrintTestMessage(self):
        self.TestTime += 1
        print(f"[{self.TestTime}] Test passed!")

    def GoToSettingsPage(self):
        self.PageName = "Settings"

    def draw_SettingsPage(self):
        self.bt_setting_lang.draw(screen, fM.LangFile_ui['bt_lang'], self.NormalButtonTextures)
        self.bt_GoToSettingAdvanced.draw(screen, fM.LangFile_ui['bt_setting_advanced'], self.NormalButtonTextures)
        self.bt_GoToResourcePacks.draw(screen, fM.LangFile_ui['bt_setting_respack'], self.NormalButtonTextures)
        self.bt_BackToHome.draw(screen, fM.LangFile_ui['bt_return'], self.NormalButtonTextures)

    def GoToSettingLangPage(self):
        with open(os.path.join("UserData", "Settings.json"), encoding='utf8', mode='r') as file:
            j = json.load(file)
            self.LangDirIndex = fM.LangFolder.index(j['Language'])
            file.close()
        self.PageName = "Settings_Lang"

    def ReturnToSettings(self):
        self.PageName = "Settings"

    def draw_LangPage(self):
        newText(screen, fM.LangFile_msg['msg_lang'], fM.default_text_font, "#000000", 400, 165, 0.8, 'center', shaderOn=False)

        # draw langs
        if self.LangDirIndex > 0:
            newText(screen, fM.LangDisplayNames[self.LangDirIndex - 1], fM.default_text_font, "#dbe1e5", 400, 210, 0.7, 'center')
            newText(screen, fM.Lang_isVerified(fM.LangFolder[self.LangDirIndex - 1]), fM.default_text_font, "#dac500", 200, 210, 0.4, 'center')
        newText(screen, fM.LangDisplayNames[self.LangDirIndex], fM.default_text_font, "#FFFFFF", 400, 250, 1.1, 'center')
        newText(screen, fM.Lang_isVerified(fM.LangFolder[self.LangDirIndex]), fM.default_text_font, "#ffe600", 200, 250, 0.8, 'center')
        if self.LangDirIndex < len(fM.LangFolder) - 1:
            newText(screen, fM.LangDisplayNames[self.LangDirIndex + 1], fM.default_text_font, "#dbe1e5", 400, 290, 0.7, 'center')
            newText(screen, fM.Lang_isVerified(fM.LangFolder[self.LangDirIndex + 1]), fM.default_text_font, "#dac500", 200, 290, 0.4, 'center')

        self.bt_previous_lang.draw(screen, self.LangChooseButtonTextures)
        self.bt_next_lang.draw(screen, self.LangChooseButtonTextures)
        self.bt_lang_select.draw(screen, fM.LangFile_ui['bt_select'], self.NormalButtonTextures)
        self.bt_return_settings.draw(screen, fM.LangFile_ui['bt_return'], self.NormalButtonTextures)

    def LangSelect(self):
        fM.Settings = json.load(open(os.path.join("UserData", "Settings.json")))
        self.settings_content = fM.Settings
        self.settings_content['Language'] = fM.LangFolder[self.LangDirIndex]
        self.selected_lang = fM.LangFolder[self.LangDirIndex]

        with open(os.path.join("UserData", "Settings.json"), mode='w') as file:
            json.dump(self.settings_content, file)
            file.close()

        fM.Lang_Reload()

    def NextLang(self):
        if self.LangDirIndex < len(fM.LangFolder) - 1:
            self.LangDirIndex += 1

    def PreviousLang(self):
        if self.LangDirIndex > 0:
            self.LangDirIndex -= 1

    def SolveEnglishOrSpanish(self):
        if self.play_enores_snd:
            if not self.isStaticPlayed and self.selected_lang == "es_sp" and self.PageName == "Settings_Lang":
                enores.play()
                self.isStaticPlayed = True
            elif self.selected_lang != "es_sp" or self.PageName != "Settings_Lang":
                enores.stop()
                self.isStaticPlayed = False

    def GoToSettingsAdvancedPage(self):
        self.PageName = "Settings_Advanced"

    def draw_SettingsAdvanced(self):
        self.cb_DevInfo.draw(screen, fM.LangFile_ui['cb_dev_info'], self.CheckBoxTextures)
        self.DevInfo = self.cb_DevInfo.isChecked
        self.cb_NewSplashAnimation.draw(screen, fM.LangFile_ui['cb_new_splash'], self.CheckBoxTextures)
        self.cb_enoresSound.draw(screen, fM.LangFile_ui['cb_en_or_es_snd'], self.CheckBoxTextures)
        self.play_enores_snd = self.cb_enoresSound.isChecked
        self.bt_return_settings.draw(screen, fM.LangFile_ui['bt_return'], self.NormalButtonTextures)

    def GoToSettingsResourcePacksPage(self):
        self.PageName = "Settings_ResourcePacks"

    def draw_SettingsResourcePacks(self):
        newText(screen, fM.LangFile_ui['title_allRes'], fM.default_text_font, "#000000", 400, 155, 0.75, 'center', shaderOn=False)

        self.bt_ResPrevious.draw(screen, self.ResButtonTextures)
        self.bt_ResNext.draw(screen, self.ResButtonTextures)

        self.cb_Res1.draw(screen, self.ResCheckBoxTextures)
        if fM.ResourcePackFolderIndex + 1 < len(fM.ResourcePackFolder): self.cb_Res2.draw(screen, self.ResCheckBoxTextures)
        if fM.ResourcePackFolderIndex + 2 < len(fM.ResourcePackFolder): self.cb_Res3.draw(screen, self.ResCheckBoxTextures)

        self.cb_Res1.index = fM.ResourcePackFolderIndex
        self.cb_Res2.index = fM.ResourcePackFolderIndex + 1
        self.cb_Res3.index = fM.ResourcePackFolderIndex + 2

        if gv.ResNeedsUpdate:
            time.sleep(0.5)
            fM.Resource_Pack_Reload()
            time.sleep(0.5)
            self.ReloadTextures()
            gv.ResNeedsUpdate = False

        try:
            screen.blit(pygame.transform.scale(fM.ResPacksIcons[fM.ResourcePackFolderIndex], (80, 80)), (150, 180))
            newText(screen, fM.ResourcePackFolder[fM.ResourcePackFolderIndex], fM.default_text_font, fM.ResPacksDatas[fM.ResourcePackFolderIndex]['name_color'], 240, 180, 0.7, 'topleft')
            newText(screen, fM.ResPacksDatas[fM.ResourcePackFolderIndex]['introduction_line1'], fM.default_text_font, fM.ResPacksDatas[fM.ResourcePackFolderIndex]['introduction_color_line1'], 240, 210, 0.5, 'topleft', shaderOn=False)
            newText(screen, fM.ResPacksDatas[fM.ResourcePackFolderIndex]['introduction_line2'], fM.default_text_font, fM.ResPacksDatas[fM.ResourcePackFolderIndex]['introduction_color_line2'], 240, 230, 0.5, 'topleft', shaderOn=False)

            screen.blit(pygame.transform.scale(fM.ResPacksIcons[fM.ResourcePackFolderIndex + 1], (80, 80)), (150, 265))
            newText(screen, fM.ResourcePackFolder[fM.ResourcePackFolderIndex + 1], fM.default_text_font, fM.ResPacksDatas[fM.ResourcePackFolderIndex + 1]['name_color'], 240, 265, 0.7, 'topleft')
            newText(screen, fM.ResPacksDatas[fM.ResourcePackFolderIndex + 1]['introduction_line1'], fM.default_text_font, fM.ResPacksDatas[fM.ResourcePackFolderIndex + 1]['introduction_color_line1'], 240, 295, 0.5, 'topleft', shaderOn=False)
            newText(screen, fM.ResPacksDatas[fM.ResourcePackFolderIndex + 1]['introduction_line2'], fM.default_text_font, fM.ResPacksDatas[fM.ResourcePackFolderIndex + 1]['introduction_color_line2'], 240, 315, 0.5, 'topleft', shaderOn=False)

            screen.blit(pygame.transform.scale(fM.ResPacksIcons[fM.ResourcePackFolderIndex + 2], (80, 80)), (150, 350))
            newText(screen, fM.ResourcePackFolder[fM.ResourcePackFolderIndex + 2], fM.default_text_font, fM.ResPacksDatas[fM.ResourcePackFolderIndex + 2]['name_color'], 240, 350, 0.7, 'topleft')
            newText(screen, fM.ResPacksDatas[fM.ResourcePackFolderIndex + 2]['introduction_line1'], fM.default_text_font, fM.ResPacksDatas[fM.ResourcePackFolderIndex + 2]['introduction_color_line1'], 240, 380, 0.5, 'topleft', shaderOn=False)
            newText(screen, fM.ResPacksDatas[fM.ResourcePackFolderIndex + 2]['introduction_line2'], fM.default_text_font, fM.ResPacksDatas[fM.ResourcePackFolderIndex + 2]['introduction_color_line2'], 240, 400, 0.5, 'topleft', shaderOn=False)
        except IndexError:
            pass

        self.bt_return_settings.draw(screen, fM.LangFile_ui['bt_return'], self.NormalButtonTextures)

    def ResPrevious(self):
        if fM.ResourcePackFolderIndex > 0:
            fM.ResourcePackFolderIndex -= 1

    def ResNext(self):
        if fM.ResourcePackFolderIndex + 1 < len(fM.ResourcePackFolder):
            fM.ResourcePackFolderIndex += 1

    def CursorStatementCheckAndChange(self):
        # fuck this, it must be the shittest code in the world
        # Actually, I used ChatGPT to make the list bcuz I'm lazy hahaha
        scsList: list = [
            self.bt_GoToMainFn.CursorInButton,
            self.bt_GoToHelp.CursorInButton,
            self.bt_GoToSetting.CursorInButton,
            self.bt_StopProgram.CursorInButton,
            self.bt_Match.CursorInButton,
            self.bt_Add.CursorInButton,
            self.bt_Remove.CursorInButton,
            self.bt_Load.CursorInButton,
            self.bt_Clear.CursorInButton,
            self.bt_BackToHome.CursorInButton,
            self.bt_ChooseName.CursorInButton,
            self.bt_ChooseObject.CursorInButton,
            self.bt_clear_ChooseName.CursorInButton,
            self.bt_clear_ChooseObject.CursorInButton,
            self.bt_clear_ChooseAll.CursorInButton,
            self.bt_Cancel.CursorInButton,
            self.bt_Confirm.CursorInButton,
            self.bt_InputEnter.CursorInButton,
            self.bt_Browse_File_Next.CursorInButton,
            self.bt_Browse_File_Previous.CursorInButton,
            self.bt_Load_File_Select.CursorInButton,
            self.bt_load_ChooseName.CursorInButton,
            self.bt_load_ChooseObject.CursorInButton,
            self.bt_easter_egg.CursorInButton,
            self.bt_setting_lang.CursorInButton,
            self.bt_return_settings.CursorInButton,
            self.bt_lang_select.CursorInButton,
            self.bt_previous_lang.CursorInButton,
            self.bt_next_lang.CursorInButton,
            self.bt_GoToSettingAdvanced.CursorInButton,
            self.bt_GoToResourcePacks.CursorInButton,
            self.cb_DevInfo.CursorInButton,
            self.cb_NewSplashAnimation.CursorInButton,
            self.cb_enoresSound.CursorInButton,
            self.bt_ResNext.CursorInButton,
            self.bt_ResPrevious.CursorInButton,
            self.cb_Res1.CursorInButton,
            self.cb_Res2.CursorInButton,
            self.cb_Res3.CursorInButton,
            self.bt_Match_AtoB.CursorInButton,
            self.bt_MatchedPrevious.CursorInButton,
            self.bt_MatchedNext.CursorInButton,
        ]

        if any(scsList):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            return True
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return False

    def ReloadTextures(self):
        self.NormalButtonTextures: tuple = (fM.Textures['button_normal'], fM.Textures['button_chose'], fM.Textures['button_pressed'],
                                            fM.Textures['button_short_normal'], fM.Textures['button_short_chose'], fM.Textures['button_short_pressed'],
                                            fM.Textures['button_disabled'], fM.Textures['button_short_disabled'])
        self.EnterButtonTextures: tuple = (fM.Textures['button_enter_normal'],
                                           fM.Textures['button_enter_chose'],
                                           fM.Textures['button_enter_pressed'])
        self.LangChooseButtonTextures: tuple = (fM.Textures['button_lang_next_normal'], fM.Textures['button_lang_next_chose'], fM.Textures['button_lang_next_pressed'],
                                                fM.Textures['button_lang_previous_normal'], fM.Textures['button_lang_previous_chose'], fM.Textures['button_lang_previous_pressed'])
        self.InputFieldTextures: tuple = (fM.Textures['input_field'])
        self.CheckBoxTextures: tuple = (fM.Textures['check_box_normal'], fM.Textures['check_box_chose'],
                                        fM.Textures['check_box_normal_checked'], fM.Textures['check_box_chose_checked'])
        self.ResButtonTextures: tuple = (fM.Textures['button_go_previous_normal'], fM.Textures['button_go_previous_chosen'], fM.Textures['button_go_previous_pressed'],
                                         fM.Textures['button_go_next_normal'], fM.Textures['button_go_next_chosen'], fM.Textures['button_go_next_pressed'])
        self.ResCheckBoxTextures: tuple = (fM.Textures['check_box_res_normal'],
                                           fM.Textures['check_box_res_chosen'],
                                           fM.Textures['check_box_res_using'])

        print("\nTextures Updated\n")

    def GoToMatchPage(self):
        self.PageName = "Match_Options"

    def draw_MatchOptions(self):
        self.bt_Match_AtoB.draw(screen, fM.LangFile_ui['bt_match_a_to_b'], self.NormalButtonTextures)
        self.bt_Cancel.draw(screen, fM.LangFile_ui['bt_return'], self.NormalButtonTextures)

    def GoToMatchAtoB_Result_Page(self):
        ProcessCommand(self.command)
        self.PageName = "Match_AtoB"

    def draw_Match_AtoB_RandResult_Page(self):
        newText(screen, fM.LangFile_ui['title_matched_result'], fM.default_text_font, "#000000", 400, 165, 1, 'center', shaderOn=False)
        self.bt_MatchedPrevious.draw(screen, self.ResButtonTextures)
        self.bt_MatchedNext.draw(screen, self.ResButtonTextures)

        try:
            if self.MatchedListIndex > 0:
                newText(screen, gv.Matched_Groups[self.MatchedListIndex - 1][0], fM.default_text_font, "#F0F0F0", 390, 250, 0.75, 'bottomright')
                newText(screen, gv.Matched_Groups[self.MatchedListIndex - 1][1], fM.default_text_font, "#F0F0F0", 410, 250, 0.75, 'bottomleft')
            newText(screen, gv.Matched_Groups[self.MatchedListIndex][0], fM.default_text_font, "#FFFFFF", 390, 300, 1, 'bottomright')
            newText(screen, gv.Matched_Groups[self.MatchedListIndex][1], fM.default_text_font, "#FFFFFF", 410, 300, 1, 'bottomleft')
            if self.MatchedListIndex < len(gv.Matched_Groups) - 1:
                newText(screen, gv.Matched_Groups[self.MatchedListIndex + 1][0], fM.default_text_font, "#F0F0F0", 390, 340, 0.75, 'bottomright')
                newText(screen, gv.Matched_Groups[self.MatchedListIndex + 1][1], fM.default_text_font, "#F0F0F0", 410, 340, 0.75, 'bottomleft')
        except IndexError:
            self.PageName = "Error"
            self.ErrorCode = 5

        if self.MatchedListIndex == 0:
            self.bt_MatchedPrevious.isEnabled = False
        else:
            self.bt_MatchedPrevious.isEnabled = True

        if self.MatchedListIndex == len(gv.Matched_Groups) - 1:
            self.bt_MatchedNext.isEnabled = False
        else:
            self.bt_MatchedNext.isEnabled = True

        self.bt_Cancel.draw(screen, fM.LangFile_ui['bt_continue'], self.NormalButtonTextures)

    def MatchedList_Previous(self):
        self.MatchedListIndex -= 1

    def MatchedList_Next(self):
        self.MatchedListIndex += 1