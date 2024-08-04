import pygame
import fileManager
import text
import gloabalVars as gv

fM = fileManager.FileManager()
newText = text.newText

class Button():
    def __init__(self, posX: float, posY: float, scale: list, function, isEnabled: bool):
        self.posX = posX
        self.posY = posY
        self.Scale = scale
        self.function = function
        self.image = None

        if scale[0] == 350:
            self.image = fM.button_normal
        elif scale[0] == 150:
            self.image = fM.button_short_normal

        self.image = pygame.transform.scale(self.image, (scale[0], scale[1]))
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)
        self.isFunctionExecuted: bool = False
        self.Text = text
        self.textPos: list = [self.posX + 5, self.posY - 5]
        self.textColor = (255, 255, 255)
        self.textColor_normal = (255, 255, 255)
        self.textColor_chose = (200, 200, 200)
        self.PressingTime: int = 0
        self.isEnabled = isEnabled

    def draw(self, surface, ctx):
        # handle mouse
        mousePos = pygame.mouse.get_pos()

        if self.isEnabled:
            if self.rect.collidepoint(mousePos):
                if pygame.mouse.get_pressed()[0]:
                    if self.Scale[0] == 350:
                        self.image = fM.button_pressed
                    elif self.Scale[0] == 150:
                        self.image = fM.button_short_pressed
                    self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))
                    self.textPos = [self.posX, self.posY + 6]
                    self.textColor = self.textColor_chose

                    if gv.LeftButtonPressingTime == 0:
                        self.function()
                else:
                    if self.Scale[0] == 350:
                        self.image = fM.button_chose
                    elif self.Scale[0] == 150:
                        self.image = fM.button_short_chose
                    self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))
                    self.textPos = [self.posX, self.posY - 5]
                    self.textColor = self.textColor_chose
                    self.isFunctionExecuted = False

            else:
                if self.Scale[0] == 350:
                    self.image = fM.button_normal
                elif self.Scale[0] == 150:
                    self.image = fM.button_short_normal
                self.textPos = [self.posX, self.posY - 5]
                self.textColor = self.textColor_normal
                self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))
        else:
            if self.Scale[0] == 350:
                self.image = fM.button_chose
                self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))
            elif self.Scale[0] == 150:
                self.image = fM.button_short_chose
                self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))

        # draw
        surface.blit(self.image, (self.rect.x, self.rect.y))

        newText(surface, ctx, fM.default_text_font, self.textColor, self.textPos[0], self.textPos[1], 1, 'center')

class EnterButton():
    def __init__(self, posX: float, posY: float, scale: list, function):
        self.posX = posX
        self.posY = posY
        self.Scale = scale
        self.function = function
        self.image = fM.button_enter_normal
        self.image = pygame.transform.scale(self.image, (scale[0], scale[1]))
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)
        self.isFunctionExecuted: bool = False
        self.PressingTime: int = 0

    def draw(self, surface, ctx):
        # handle mouse
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0]:
                self.image = fM.button_enter_pressed
                self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))

                if gv.LeftButtonPressingTime == 0:
                    self.function()
            else:
                self.image = fM.button_enter_chose
                self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))
                self.isFunctionExecuted = False

        else:
            self.image = fM.button_enter_normal
            self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))

        # draw
        surface.blit(self.image, (self.rect.x, self.rect.y))