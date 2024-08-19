import fileManager

fM = fileManager.FileManager()

class LonelyWorkMark:
    def __init__(self):
        self.image = fM.splash_lw_mark
        self.rect = self.image.get_rect()
        self.rect.center = (400, 700)
        self.rect.top = 605
        self.textX = 360

    def draw(self, surface):
        if round(self.rect.y, 1) > 225:
            self.rect.y -= 0.45 * (self.rect.y * 0.1 - 180 * 0.1)
        else:
            self.rect.x -= 0.5 * (self.rect.x * 0.1 - 90 * 0.1)
            self.textX += 0.45 * (-15 - self.textX * 0.1)

        surface.blit(fM.splash_lw_text, (self.rect.x - self.textX, self.rect.y + 20))
        surface.blit(fM.splash_black_block, (self.rect.x - 350, self.rect.y - 40))
        surface.blit(self.image, (self.rect.x, self.rect.y))