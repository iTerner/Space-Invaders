import pygame
from ship import Ship
from const import YELLOW_SPACE_SHIP, YELLOW_LASER, HEIGHT

"""
Player class
"""


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)  # create a ship using the ship abstract class
        self.ship_img = YELLOW_SPACE_SHIP  # player ship image
        self.laser_img = YELLOW_LASER  # player laser image
        self.mask = pygame.mask.from_surface(
            self.ship_img)  # create mask for collision
        self.max_health = health  # the maximum health for the player

    """
    objs - the enemies. given in order to check for collision while moving
    vel - the velocity of the laser

    The function move the laser according to the given velocity
    """

    def move_lasers(self, vel, objs):
        self.cool_down()
        for laser in self.lasers:
            laser.move(vel)
            # check if the laser is off the screen
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            # check if the laser collide with something
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    """
    The function draw the player
    """

    def draw(self, win):
        super().draw(win)
        self.healthbar(win)

    """
    The function creates the health bar for the palyer
    """

    def healthbar(self, win):
        # red
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y +
                                            self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        # green
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y +
                                            self.ship_img.get_height() + 10, self.ship_img.get_width() * (1 - ((self.max_health - self.health) / self.max_health)), 10))
