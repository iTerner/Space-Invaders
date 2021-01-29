import pygame
import time
import os
import random
from const import RED_SPACE_SHIP, BLUE_SPACE_SHIP, GREEN_SPACE_SHIP, RED_LASER, BLUE_LASER, GREEN_LASER, YELLOW_SPACE_SHIP, YELLOW_LASER, BG, WIN, HEIGHT, WIDTH, PLAYER_VEL, ENEMY_VEL, LASER_VEL
from ship import Ship
from player import Player
from enemy import Enemy
from collision import collide
pygame.font.init()


"""
The game loop
"""


def game_loop():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    lost = False  # flag
    lost_count = 0  # the count of seconds we render the "you lost" message
    enemies = []  # list of the enemies ships
    wave_length = 5  # the count of the enemy ships in each wave
    level = 0  # the current level
    lives = 5  # the number of lives the player has
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    # create a player
    player = Player(300, 550)

    """
    The function draw the window
    """
    def redraw_window():
        WIN.blit(BG, (0, 0))
        # draw the text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        # draw the enemy ships
        for enemy in enemies:
            enemy.draw(WIN)

        # draw the player
        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH // 2 - lost_label.get_width() // 2, 275))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        # check if the player lose
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        # render the "you lost" message for 3 seconds
        if lost:
            if lost_count > FPS * 3:
                quit()
            else:
                continue

        # check if we complete the level
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                # spawn the enemy ships
                enemy = Enemy(random.randrange(50, WIDTH - 100),
                              random.randrange(-1500 * level, -100), random.choice(["red", "green", "blue"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            # quit the game if you click the quit button
            if event.type == pygame.QUIT:
                quit()

        # in order to move diagonaly - meaning pressing two keys in the same time
        keys = pygame.key.get_pressed()
        # move the ship to the left
        if keys[pygame.K_a] and player.x - PLAYER_VEL > 0:
            player.x -= PLAYER_VEL
        # move the ship to the right
        if keys[pygame.K_d] and player.x + PLAYER_VEL + player.get_width() < WIDTH:
            player.x += PLAYER_VEL
        # move the ship to the up
        if keys[pygame.K_w] and player.y - PLAYER_VEL > 0:
            player.y -= PLAYER_VEL
        # move the ship to the down
        if keys[pygame.K_s] and player.y + PLAYER_VEL + player.get_height() + 15 < HEIGHT:
            player.y += PLAYER_VEL
        # create laser when clicking the space bar
        if keys[pygame.K_SPACE]:
            player.shoot()

        # move the enemy ships
        for enemy in enemies:
            enemy.move(ENEMY_VEL)
            enemy.move_lasers(LASER_VEL, player)

            # make the enemy shoot at the player
            # 50% to shoot every second
            if random.randrange(0, 3 * 60) == 1:
                enemy.shoot()

            # check for collision
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            # check if the enemy passed us
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                # remove the specified enemy
                enemies.remove(enemy)

        player.move_lasers(-LASER_VEL, enemies)


"""
The main menu of the game
"""


def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WIN.blit(BG, (0, 0))
        title_label = title_font.render(
            "Press the mouse the begin...", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH // 2 - title_label.get_width() // 2, 275))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # if we pressed any of the nouse button then start the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_loop()

    pygame.quit()


main_menu()
