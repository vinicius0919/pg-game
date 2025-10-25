import pgzrun
import random
from utils.helpers import calculate_distance
from entities.player import Player
from entities.enemy import Enemy

WIDTH = 800
HEIGHT = 450
Y_LIMITS = (156, 380)

player = Player((WIDTH // 2, HEIGHT // 2))
enemies = [Enemy(f'orc{random.randint(1, 2)}', (random.randint(0, WIDTH), random.randint(*Y_LIMITS))) for _ in range(5)]

background_image = "sky_bridge"

def update():
    player.update()
    # VERIFY IF PLAYER IS INSIDE THE LIMITS
    if player.actor.y < Y_LIMITS[0]:
        player.actor.y = Y_LIMITS[0]
    elif player.actor.y > Y_LIMITS[1]:
        player.actor.y = Y_LIMITS[1]
    
    #VERIFY IF PLAYER IS IN X LIMITS
    if player.actor.x < 0:
        player.actor.x = 0
    elif player.actor.x > WIDTH:
        player.actor.x = WIDTH
    for enemy in enemies:
        #VERIFY IF ENEMY IS INSIDE THE LIMITS
        if enemy.actor.y < Y_LIMITS[0]:
            enemy.actor.y = Y_LIMITS[0]
        elif enemy.actor.y > Y_LIMITS[1]:
            enemy.actor.y = Y_LIMITS[1]
        #VERIFY IF ENEMY IS IN X LIMITS
        if enemy.actor.x < 0:
            enemy.actor.x = 0
        elif enemy.actor.x > WIDTH:
            enemy.actor.x = WIDTH

        dist = calculate_distance(player.actor.x, player.actor.y, enemy.actor.x, enemy.actor.y)
        if dist < 300:
            enemy.follow(player)
        else:
            enemy.stop_following()
        enemy.update()

def draw():
    screen.clear()
    screen.blit(background_image, (0, 0))
    player.draw()
    for enemy in enemies:
        enemy.draw()

pgzrun.go()
