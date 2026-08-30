import pygame
import text
import gloabalVars as gv

fM = gv.fM
newText = text.newText

class Button:
    def __init__(self, posX: float, posY: float, scale: list, function, isEnabled: bool, ctx_lang_key: str = 'bt_lang_not_set'):
        self.posX = posX
        self.posY = posY
        self.Scale = scale
        self.function = function
        self.image = None

        if scale[0] == 350:
            self.image = fM.Textures['button_normal']
        elif scale[0] == 150:
            self.image = fM.Textures['button_short_normal']

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
        self.CursorInButton: bool = False
        self.ctxkey: str = ctx_lang_key

    def draw(self, surface, ctx, textures: tuple) -> None:
        self.mouse_handler(textures)
        
        # draw
        surface.blit(self.image, (self.rect.x, self.rect.y))
        try:
            newText(surface, gv.fM.LangFile_ui[self.ctxkey], fM.default_text_font, self.textColor, self.textPos[0], self.textPos[1], 1, 'center')
        except:
            newText(surface, self.ctxkey, fM.default_text_font, self.textColor, self.textPos[0], self.textPos[1], 1, 'center')

    def mouse_handler(self, textures: tuple) -> None:
        if self.isEnabled:
            if self.rect.collidepoint(gv.mousePos):
                self.CursorInButton = True

                if pygame.mouse.get_pressed()[0]:
                    if self.Scale[0] == 350:
                        self.image = textures[2]
                    elif self.Scale[0] == 150:
                        self.image = textures[5]
                    self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))
                    self.textPos = [self.posX, self.posY + 6]
                    self.textColor = self.textColor_chose

                    if gv.LeftButtonPressingTime == 0:
                        self.CursorInButton = False
                        self.function()
                else:
                    if self.Scale[0] == 350:
                        self.image = textures[1]
                    elif self.Scale[0] == 150:
                        self.image = textures[4]
                    self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))
                    self.textPos = [self.posX, self.posY - 5]
                    self.textColor = self.textColor_chose
                    self.isFunctionExecuted = False

            else:
                self.CursorInButton = False

                if self.Scale[0] == 350:
                    self.image = textures[0]
                elif self.Scale[0] == 150:
                    self.image = textures[3]
                self.textPos = [self.posX, self.posY - 5]
                self.textColor = self.textColor_normal
                self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))
        else:
            if self.Scale[0] == 350:
                self.image = textures[6]
                self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))
            elif self.Scale[0] == 150:
                self.image = textures[7]
                self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))

            self.textPos = [self.posX, self.posY - 5]
            self.textColor = self.textColor_normal

class EnterButton:
    def __init__(self, posX: float, posY: float, scale: list, function):
        self.posX = posX
        self.posY = posY
        self.Scale = scale
        self.function = function
        self.image = fM.Textures['button_enter_normal']
        self.image = pygame.transform.scale(self.image, (scale[0], scale[1]))
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)
        self.isFunctionExecuted: bool = False
        self.PressingTime: int = 0
        self.CursorInButton: bool = False

    def draw(self, surface, ctx, textures: tuple) -> None:
        self.mouse_handler(textures)
        
        # draw
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def mouse_handler(self, textures: tuple) -> None:
        if self.rect.collidepoint(gv.mousePos):
            self.CursorInButton = True

            if pygame.mouse.get_pressed()[0]:
                self.image = textures[2]
                self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))

                if gv.LeftButtonPressingTime == 0:
                    self.CursorInButton = False
                    self.function()
            else:
                self.image = textures[1]
                self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))
                self.isFunctionExecuted = False

        else:
            self.CursorInButton = False

            self.image = textures[0]
            self.image = pygame.transform.scale(self.image, (self.Scale[0], self.Scale[1]))

class LangChoosingButton:
    def __init__(self, posX: float, posY: float, type: str, function):
        self.posX = posX
        self.posY = posY
        self.function = function

        if type == "next":
            self.image = fM.Textures['button_lang_next_normal']
        else:
            self.image = fM.Textures['button_lang_previous_normal']

        self.image = pygame.transform.scale(self.image, (30, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)
        self.isFunctionExecuted: bool = False
        self.PressingTime: int = 0
        self.type = type
        self.CursorInButton: bool = False

    def draw(self, surface, textures: tuple) -> None:
        self.mouse_handler(textures)

        # draw
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def mouse_handler(self, textures) -> None:
        if self.rect.collidepoint(gv.mousePos):
            self.CursorInButton = True
            if pygame.mouse.get_pressed()[0]:
                if self.type == "next":
                    self.image = textures[2]
                elif self.type == "previous":
                    self.image = textures[5]
                self.image = pygame.transform.scale(self.image, (30, 70))

                if gv.LeftButtonPressingTime == 0:
                    self.CursorInButton = False
                    self.function()
            else:
                if self.type == "next":
                    self.image = textures[1]
                elif self.type == "previous":
                    self.image = textures[4]
                self.image = pygame.transform.scale(self.image, (30, 70))
                self.isFunctionExecuted = False

        else:
            self.CursorInButton = False
            if self.type == "next":
                self.image = textures[0]
            elif self.type == "previous":
                self.image = textures[3]
            self.image = pygame.transform.scale(self.image, (30, 70))

class ResChoosingButton:
    def __init__(self, posX, posY, direction, function, **kwargs):
        if direction == "up":
            self.image = fM.Textures['button_go_previous_normal']
        elif direction == "down":
            self.image = fM.Textures['button_go_next_normal']

        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)

        self.direction = direction
        self.fn = function

        self.CursorInButton: bool = False
        self.isEnabled = kwargs.get("isEnabled", True)

    def draw(self, surface, texture) -> None:
        self.mouse_handler(texture)
        
        # draw
        self.image = pygame.transform.scale(self.image, (64, 64))
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def mouse_handler(self, texture: tuple) -> None:
        if self.isEnabled:
            if self.rect.collidepoint(gv.mousePos):
                self.CursorInButton = True

                if pygame.mouse.get_pressed()[0]:
                    if self.direction == "up":
                        self.image = texture[2]
                    else:
                        self.image = texture[5]

                    if gv.LeftButtonPressingTime == 0:
                        self.fn()
                else:
                    if self.direction == "up":
                        self.image = texture[1]
                    else:
                        self.image = texture[4]
            else:
                self.CursorInButton = False

                if self.direction == "up":
                    self.image = texture[0]
                else:
                    self.image = texture[3]
        else:
            if self.direction == "up":
                self.image = texture[1]
            else:
                self.image = texture[4]

            self.CursorInButton = False