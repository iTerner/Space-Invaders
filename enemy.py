import pygame
from ship import Ship
from const import RED_SPACE_SHIP, RED_LASER, BLUE_LASER, BLUE_SPACE_SHIP, GREEN_LASER, GREEN_SPACE_SHIP
from laser import Laser

"""
The class of the enemy ship
"""


class Enemy(Ship):

    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        # call the ship abstract class constructor
        super().__init__(x, y, health)
        # get the image for the ship and laser
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(
            self.ship_img)  # create mask for collision

    """
    The funtion get a velocity and nove the enemy ship
    """

    def move(self, vel):
        self.y += vel

    """
    The function create a laser
    """

    def shoot(self):
        if self.cool_down_counter == 0:
            # create a new laser and add him to the lasers list
            laser = Laser(self.x - 15, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
