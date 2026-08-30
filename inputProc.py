import pygame


keyDownSet: set = set()
def getKeyDown(key: pygame.key) -> bool:
    if key in keyDownSet:
        keyDownSet.remove(key)
        return True

    return False