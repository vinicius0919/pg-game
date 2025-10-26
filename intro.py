import pgzrun
import random
from utils.helpers import calculate_distance
from entities.player import Player
from entities.enemy import Enemy

WIDTH = 800
HEIGHT = 450
Y_LIMITS = (156, 380)

player = Player((WIDTH // 2, HEIGHT // 2))
enemies = [Enemy(f'orc{random.randint(1, 2)}', (random.randint(0, WIDTH), random.randint(*Y_LIMITS))) for _ in range(1)]

background_image = "sky_bridge"

options = {
    "start": False,
    "sound_effects": True,
    "exit": False
}
counter = 0

def on_key_down(key):
    global counter
    if key == keys.UP and counter > 0:
        counter -= 1
    if key == keys.DOWN and counter < 2:
        counter += 1
    if key == keys.RETURN and counter == 2:
        options["exit"] = True
    if key == keys.RETURN and counter == 1:
        options["sound_effects"] = not options["sound_effects"]
    if key == keys.RETURN and counter == 0:
        options["start"] = True
    if key == keys.ESCAPE and options["start"]:
        options["start"] = False

def update():
    if options["exit"]:
        exit()
    if not options["start"]:
        return
    if player.life <= 0:
        options["start"] = False
    player.update()



    for enemy in enemies:
        enemy.update()
        dist = calculate_distance(player.actor.x, player.actor.y, enemy.actor.x, enemy.actor.y)
        if dist < 50:
            print("Attack!")
            player.attack(enemy)
        if dist < 300:
            enemy.follow(player)
        else:
            enemy.stop_following()

        if enemy.life <= 0:
            enemies.remove(enemy)

def draw_menu(counter):
    colors = ["white", "white", "white"]
    colors[counter] = "yellow"
    screen.draw.text("Start Game", center=(WIDTH // 2, HEIGHT // 2 - 50), fontsize=50, color=colors[0])
    screen.draw.text("Sound Effects: " + ("ON" if options["sound_effects"] else "OFF"), center=(WIDTH // 2, HEIGHT // 2 + 10), fontsize=40, color=colors[1])
    screen.draw.text("Exit", center=(WIDTH // 2, HEIGHT // 2 + 70), fontsize=50, color=colors[2])

def draw():
    screen.clear()
    screen.blit(background_image, (0, 0))

    if not options["start"]:
        draw_menu(counter)
        return

    player.draw()
    for enemy in enemies:
        enemy.draw()

pgzrun.go()
