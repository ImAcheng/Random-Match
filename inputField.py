import pygame
import fileManager
import text
import gloabalVars as gv

fM = fileManager.FileManager()
newText = text.newText

class InputField():
    def __init__(self, posX, posY):
        self.image = fM.input_field
        self.image = pygame.transform.scale(self.image, (400, 48))
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)
        self.posX = posX
        self.posY = posY

    def draw(self, surface, ctx):
        surface.blit(self.image, (self.rect.x, self.rect.y))

        if ctx == "":
            if gv.InputFieldType == "name":
                newText(surface, "Enter name here.", fM.default_text_font, (200, 200, 200), self.posX - 190, self.posY - 14, 0.5, 'topleft')
            elif gv.InputFieldType == "path":
                newText(surface, "Enter file path here.", fM.default_text_font, (200, 200, 200), self.posX - 190, self.posY - 14, 0.5, 'topleft')
        else:
            newText(surface, ctx, fM.default_text_font, (0, 0, 0), self.posX - 190, self.posY - 14, 0.5, 'topleft')