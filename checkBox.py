import json
import os.path

import pygame

import fileManager
import gloabalVars as gv
from text import newText

fM = fileManager.FileManager()

class CheckBox:
    def __init__(self, posX, posY, ctx, target_data, item_name, file: os.path):
        # I think this shit requires too many args,
        # I will fix that one day.
        # TODO: fix this shit (Acheng on Aug. 20th, 2024)

        self.posX = posX
        self.posY = posY
        self.ctx = ctx
        self.target_data = target_data
        self.item_name = item_name
        self.file = file

        self.isChecked = self.target_data[self.item_name]
        self.image = fM.check_box_normal
        self.image = pygame.transform.scale(self.image, (54, 54))
        self.rect = self.image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY

    def draw(self, surface):
        # handle mouse
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            if not self.isChecked:
                self.image = fM.check_box_chose
            else:
                self.image = fM.check_box_chose_checked

            pygame.transform.scale(self.image, (54, 54))

            if pygame.mouse.get_pressed()[0] and not self.isChecked and gv.LeftButtonPressingTime == 0:
                self.isChecked = True
                self.target_data[self.item_name] = True
                with open(self.file, 'w') as file:
                    json.dump(self.target_data, file)

            elif pygame.mouse.get_pressed()[0] and self.isChecked and gv.LeftButtonPressingTime == 0:
                self.isChecked = False
                self.target_data[self.item_name] = False
                with open(self.file, 'w') as file:
                    json.dump(self.target_data, file)

        else:
            if not self.isChecked:
                self.image = fM.check_box_normal
            else:
                self.image = fM.check_box_normal_checked

            pygame.transform.scale(self.image, (54, 54))

        pygame.transform.scale(self.image, (54, 54))

        surface.blit(self.image, (self.rect.x, self.rect.y))
        newText(surface, self.ctx, fM.default_text_font, "#FFFFFF", self.rect.x + 75, self.rect.y + 8, 1, 'topleft')

        '''
        if fM.Settings['Develop_Info']:
            newText(surface, str(self.isChecked), fM.default_text_font, "#FFFFFF", self.rect.x - 5, self.rect.y + 50, 1, 'bottomright')
        '''