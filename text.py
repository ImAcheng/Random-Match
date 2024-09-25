import pygame

def newText(surface, ctx, font, color, posX, posY, scale, align, **kwargs):
    image = font.render(ctx, True, color)
    shader = font.render(ctx, True, (100, 100, 100))
    width = image.get_width()
    height = image.get_height()
    shaderOn = kwargs.get('shaderOn', bool)

    image = pygame.transform.scale(image, (width*scale, height*scale))
    shader = pygame.transform.scale(shader, (width*scale, height*scale))
    rect = None
    s_rect = None
    match align:
        case 'center':
            rect = image.get_rect(center= (posX, posY))
            s_rect = shader.get_rect(center= (posX + 2.5, posY + 2.5))
        case 'topleft':
            rect = image.get_rect(topleft= (posX, posY))
            s_rect = shader.get_rect(topleft=(posX + 2.5, posY + 2.5))
        case 'bottomright':
            rect = image.get_rect(bottomright= (posX, posY))
            s_rect = shader.get_rect(bottomright=(posX + 2.5, posY + 2.5))
        case 'bottomleft':
            rect = image.get_rect(bottomleft= (posX, posY))
            s_rect = shader.get_rect(bottomleft=(posX + 2.5, posY + 2.5))

    if shaderOn: surface.blit(shader, s_rect)
    surface.blit(image, rect)