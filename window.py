# import modules
import pygame

# import other python files
import fileManager
import button
import text
import gloabalVars as gv
import inputField
from commandLogic import ProcessCommand

# setup
fM = fileManager.FileManager()
Button = button.Button
EnterButton = button.EnterButton
newText = text.newText
inputField = inputField.InputField

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Random Match")
pygame.display.set_icon(fM.icon)

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
        self.PageName: str = "Home"
        self.TestTime: int = 0
        self.ErrorCode: int = -1
        self.ErrorExplanation = fM.Errors['errors']

        # UI elements
        self.bt_GoToMainFn = Button(400, 200, [350, 80], self.GoToMainFnPage, True)
        self.bt_GoToHelp = Button(400, 300, [350, 80], self.GoToHelpPage, True)
        self.bt_StopProgram = Button(400, 400, [350, 80], self.StopProgram, True)
        self.bt_Match = Button(400, 200, [350, 80], self.Command_Match, True)
        self.bt_Add = Button(300, 300, [150, 80], self.GoToAddPage, True)
        self.bt_Remove = Button(500, 300, [150, 80], self.GoToRemovePage, True)
        self.bt_Load = Button(300, 400, [150, 80], self.FunctionNotAvailable, True)
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

        self.InputField = inputField(400, 200)

    def update(self):
        self.clock.tick(60)
        # print(self.command)

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

        newText(screen, "Random Match", fM.default_text_font, (0, 0, 0), 400, 100, 2, 'center')
        newText(screen, "©2024 Lonely Work All Rights Reserved. DO NOT DISTRIBUTE.", fM.default_text_font, "#FFFFFF", 790, 590, 0.5, 'bottomright')
        newText(screen, "rm-early-test(UI demo) build test-ver-002", fM.dev_text_font, "#FFFFFF", 10, 10, 1, 'topleft')
        # update
        pygame.display.update()

    def DrawPages(self):
        match self.PageName:
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
            case "FnDisabled":
                self.draw_ErrorPage()
                self.ErrorCode = 2
            case "Error":
                self.draw_ErrorPage()
            case _:
                self.draw_ErrorPage()
                self.ErrorCode = 1

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

    def StopProgram(self):
        gv.isProgramRunning = False

    def GoToHomePage(self):
        self.PageName = "Home"

    def draw_HomePage(self):
        self.bt_GoToMainFn.draw(screen, "Main Functions")
        self.bt_GoToHelp.draw(screen, "Help")
        self.bt_StopProgram.draw(screen, "Exit")

    def GoToMainFnPage(self):
        self.PageName = "MainFn"

    def draw_MainFnPage(self):
        self.bt_Match.draw(screen, "Match")
        self.bt_Add.draw(screen, "Add")
        self.bt_Remove.draw(screen, "Remove")
        self.bt_Load.draw(screen, "Load")
        self.bt_Clear.draw(screen, "Clear")
        self.bt_BackToHome.draw(screen, "Back")

    def GoToHelpPage(self):
        self.PageName = "Help"

    def draw_HelpPage(self):
        newText(screen, "All Functions", fM.default_text_font, (0, 0, 0), 400, 175, 1.25, 'center')
        newText(screen, "- match: Match a random object to a random name.", fM.default_text_font, (0, 0, 0), 20, 200, 0.8, 'topleft')
        newText(screen, "- add : Add a new name or object.", fM.default_text_font, (0, 0, 0), 20, 230, 0.8, 'topleft')
        newText(screen, "- remove : Remove a name or object.", fM.default_text_font, (0, 0, 0), 20, 260, 0.8, 'topleft')
        newText(screen, "- clear : Clear the target data.", fM.default_text_font, (0, 0, 0), 20, 290, 0.8, 'topleft')
        newText(screen, "- load: Load data to the target from a file.", fM.default_text_font, (0, 0, 0), 20, 320, 0.8, 'topleft')
        self.bt_BackToHome.draw(screen, "Back")

    def GoToAddPage(self):
        self.command = "add "
        self.PageName = "Add"

    def draw_AddPage(self):
        self.bt_ChooseName.draw(screen, "Name")
        self.bt_ChooseObject.draw(screen, "Object")
        self.bt_Cancel.draw(screen, "Cancel")

    def GoToRemovePage(self):
        self.command = "remove "
        self.PageName = "Remove"

    def draw_RemovePage(self):
        self.bt_ChooseName.draw(screen, "Name")
        self.bt_ChooseObject.draw(screen, "Object")
        self.bt_Cancel.draw(screen, "Cancel")

    def GoToInputWithName(self):
        self.command += "name "
        self.PageName = "Input"

    def GoToInputWithObject(self):
        self.command += "object "
        self.PageName = "Input"

    def draw_InputPage(self):
        self.InputField.draw(screen, "".join(self.userInputString))
        self.bt_InputEnter.draw(screen, "Enter")
        self.bt_Cancel.draw(screen, "Cancel")

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
        self.bt_clear_ChooseName.draw(screen, "Name")
        self.bt_clear_ChooseObject.draw(screen, "Object")
        self.bt_clear_ChooseAll.draw(screen, "All")
        self.bt_Cancel.draw(screen, "Cancel")

    def draw_ConfirmPage(self):
        newText(screen, "Is that all? If is, press confirm button.", fM.default_text_font, (0, 0, 0), 400, 200, 1, 'center')
        self.bt_Confirm.draw(screen, "Confirm")
        self.bt_Cancel.draw(screen, "Cancel")

    def GoToResultPage(self):
        self.PageName = "Result"

    def draw_ResultPage(self):
        newText(screen, gv.ResultMessage, fM.default_text_font, (0, 0, 0), 400, 200, 0.8, 'center')
        self.bt_Cancel.draw(screen, "Continue")

    def GoToLoadPage(self):
        self.PageName = "Load"

    def draw_LoadPage(self):
        pass

    def draw_ErrorPage(self):
        newText(screen, ":(", fM.default_text_font, (255, 255, 255), 150, 230, 4, 'center')
        newText(screen, "Oops, it seems like that something went wrong.", fM.default_text_font, (255, 255, 255), 100, 320, 0.75, 'topleft')
        newText(screen, f"Error code: [{self.ErrorCode} ({self.ErrorExplanation[str(self.ErrorCode)]})]", fM.default_text_font, (255, 255, 255), 100, 350, 0.75, 'topleft')
        self.bt_Cancel.draw(screen, "Continue")

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
        self.GoToConfirmPage()

    def Command_Cancel(self):
        self.command = None
        self.userInputString.clear()
        self.PageName = "MainFn"

    def Command_Process(self):
        try:
            ProcessCommand(self.command)
            self.GoToResultPage()
        except TypeError:
            self.ErrorCode = 3
            self.PageName = "Error"

    def GoToConfirmPage(self):
        self.PageName = "Confirm"

    def PrintTestMessage(self):
        self.TestTime += 1
        print(f"[{self.TestTime}] Test passed!")