import json
import os.path
import time

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
        # I think I've already fixed this (Acheng on Aug. 22th, 2024)

        self.posX = posX
        self.posY = posY
        self.ctx = ctx
        self.target_data = target_data
        self.item_name = item_name
        self.file = file
        self.CursorInButton: bool = False

        self.isChecked = self.target_data[self.item_name]
        self.image = fM.Textures['check_box_normal']
        self.image = pygame.transform.scale(self.image, (54, 54))
        self.rect = self.image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY

    def draw(self, surface, ctx, textures: tuple):
        # handle mouse
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            self.CursorInButton = True

            if not self.isChecked:
                self.image = textures[1]
            else:
                self.image = textures[3]

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
            self.CursorInButton = False

            if not self.isChecked:
                self.image = textures[0]
            else:
                self.image = textures[2]

        self.image = pygame.transform.scale(self.image, (54, 54))

        surface.blit(self.image, (self.rect.x, self.rect.y))
        newText(surface, ctx, fM.default_text_font, "#FFFFFF", self.rect.x + 75, self.rect.y + 8, 1, 'topleft')

class ResPacksCheckBox:
    def __init__(self, posX: float, posY: float, target_index: int):
        self.image = fM.Textures['check_box_res_normal']
        self.image = pygame.transform.scale(self.image, (600, 84))

        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY

        self.index = target_index
        self.isUsing = False
        self.settings = fM.Settings
        self.CursorInButton: bool = False

    def draw(self, surface, texture):
        mouse_pos = pygame.mouse.get_pos()

        try:
            self.isUsing = self.index == fM.ResourcePackFolder.index(fM.Settings['using_resource_packs'])
        except ValueError:
            self.isUsing = False

        if self.rect.collidepoint(mouse_pos):
            self.image = texture[1]
            self.CursorInButton = True

            if pygame.mouse.get_pressed()[0] and gv.LeftButtonPressingTime == 0:
                self.CursorInButton = False
                fM.Settings = json.load(open(os.path.join("UserData", "Settings.json")))
                self.settings = fM.Settings
                self.settings['using_resource_packs'] = fM.ResourcePackFolder[self.index]
                with open(os.path.join("UserData", "Settings.json"), mode='w', encoding='utf8') as file:
                    json.dump(self.settings, file)
                    file.close()
                gv.ResNeedsUpdate = True

        elif self.isUsing:
            self.CursorInButton = False
            self.image = texture[2]
        else:
            self.CursorInButton = False
            self.image = texture[0]

        self.image = pygame.transform.scale(self.image, (600, 84))
        surface.blit(self.image, (self.rect.x, self.rect.y))