import pygame
from laser import Laser
from const import HEIGHT

"""
abstract ship class
"""


class Ship:

    COOLDOWN = 30  # half a second

    def __init__(self, x, y, health=100):
        self.x = x  # x position of the ship
        self.y = y  # y position of the ship
        self.health = health  # the health of the ship with default health value of 100
        self.ship_img = None  # the image of the ship
        self.laser_img = None  # the image of the laser
        self.lasers = []  # the lasers the ship fired
        self.cool_down_counter = 0  # cool down for shooting the lasers

    """
    The function draw the ship
    """

    def draw(self, win):
        win.blit(self.ship_img, (self.x, self.y))
        # draw the lasers
        for laser in self.lasers:
            laser.draw(win)

    """
    obj - the player. given in order to check for collision while moving
    vel - the velocity of the laser

    The function move the laser according to the given velocity
    """

    def move_lasers(self, vel, obj):
        self.cool_down()
        for laser in self.lasers:
            laser.move(vel)
            # check if the laser is off the screen
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            # check if the laser collide with the player
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    """
    The funtion returns the width of the ship image
    """

    def get_width(self):
        return self.ship_img.get_width()

    """
    The funtion returns the height of the ship image
    """

    def get_height(self):
        return self.ship_img.get_height()

    """
    The funtion handles the cool down 
    """

    def cool_down(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    """
    The function create a laser
    """

    def shoot(self):
        if self.cool_down_counter == 0:
            # create a new laser and add him to the lasers list
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
