import pygame

def newText(surface, ctx, font, color, posX, posY, scale, align):
    image = font.render(ctx, True, color)
    width = image.get_width()
    height = image.get_height()
    image = pygame.transform.scale(image, (width*scale, height*scale))
    rect = None
    if align == 'center':
        rect = image.get_rect(center= (posX, posY))
    elif align == 'topleft':
        rect = image.get_rect(topleft= (posX, posY))
    elif align == 'bottomright':
        rect = image.get_rect(bottomright= (posX, posY))
    surface.blit(image, rect)