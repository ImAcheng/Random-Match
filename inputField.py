import pygame
import fileManager
import text
import gloabalVars as gv
import inputProc

fM = fileManager.FileManager()
newText = text.newText

class InputField:
    def __init__(self, posX, posY):
        self.image = fM.Textures['input_field']
        self.image = pygame.transform.scale(self.image, (400, 48))
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)
        self.posX = posX
        self.posY = posY

        # text
        self.BackSpaceHoldingTime: int = 0

        self.notActualInputChr: list = [
            pygame.K_BACKSPACE,
            pygame.K_RETURN
        ]

        self.text:str = ""

    def draw(self, surface, ctx, get_lang, texture: tuple):
        # self.input_handler()

        surface.blit(self.image, (self.rect.x, self.rect.y))
        self.image = pygame.transform.scale(self.image, (400, 48))

        if ctx == "":
            if gv.InputFieldType == "name":
                newText(surface, get_lang, fM.default_text_font, (200, 200, 200), self.posX - 190, self.posY - 14, 0.5, 'topleft', shaderOn=False)
            elif gv.InputFieldType == "path":
                newText(surface, "Enter file path here.", fM.default_text_font, (200, 200, 200), self.posX - 190, self.posY - 14, 0.5, 'topleft', shaderOn=False)
        else:
            newText(surface, ctx, fM.default_text_font, (0, 0, 0), self.posX - 190, self.posY - 14, 0.5, 'topleft', shaderOn=False)

    def input_handler(self, ev: pygame.Event):
        if ev.type == pygame.KEYDOWN:
            try:
                if ev.key == pygame.K_BACKSPACE and self.text:
                    self.text.pop()
                elif ev.key not in self.notActualInputChr:
                    if self.isShiftHolding():
                        # uppercase
                        if str(chr(ev.key)).isalpha:
                            self.text.append(chr(ev.key - 32))
                            return

                        # symbols
                        match chr(ev.key):
                            case "1":
                                self.text.append("!")
                            case "2":
                                self.text.append("@")
                            case "3":
                                self.text.append("#")
                            case "4":
                                self.text.append("$")
                            case "5":
                                self.text.append("%")
                            case "6":
                                self.text.append("^")
                            case "7":
                                self.text.append("&")
                            case "8":
                                self.text.append("*")
                            case "9":
                                self.text.append("(")
                            case "0":
                                self.text.append(")")
                            case ";":
                                self.text.append(":")
                            case "'":
                                self.text.append("\"")
                            case ",":
                                self.text.append("<")
                            case ".":
                                self.text.append(">")
                            case "/":
                                self.text.append("?")
                            case _:
                                return

                    else:
                        # lowercase
                        self.text.append(chr(ev.key))
            except ValueError:
                pass

    def isShiftHolding(self) -> bool:
            return pygame.key.get_mods() & pygame.KMOD_SHIFT
    
    def isBackSpaceHolding(self) -> bool:
        return pygame.key.get_pressed()[pygame.K_BACKSPACE]

    def autoDeletingWords(self):
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
                self.text.pop()
            except IndexError:
                pass
            self.AutoDeletingWordsDelay = 0