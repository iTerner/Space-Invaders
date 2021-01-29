import pygame
from collision import collide

"""
Laser class
"""


class Laser:
    def __init__(self, x, y, img):
        self.x = x  # the x value of the laser
        self.y = y  # the y value of the laser
        self.img = img  # laser image
        self.mask = pygame.mask.from_surface(
            self.img)  # mask for laser collistion

    """
    The funtion draw the laser
    """

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    """
    The function move the laser using the given velocity
    """

    def move(self, vel):
        self.y += vel

    """
    The function checks if the laser is off screen
    """

    def off_screen(self, height):
        return not (self.y <= height and self.y > 0)

    """
    The function check if the laser collide with something
    """

    def collision(self, obj):
        return collide(obj, self)
