import pgzrun
import random
from utils.helpers import calculate_distance
from entities.player import Player
from entities.enemy import Enemy
WIDTH = 800
HEIGHT = 450
Y_LIMITS = (156, 380)
level = 1
player = Player((WIDTH // 2, HEIGHT // 2))
enemies = [Enemy(f'orc1', (random.randint(0, WIDTH), random.randint(*Y_LIMITS))) for _ in range(1)]

background_image = "sky_bridge"

options = {
    "start": False,
    "sound_effects": True,
    "exit": False
}
counter = 0
is_sword_playing = False
def reset_sword():
    global is_sword_playing
    is_sword_playing = False

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
        if options["sound_effects"]:
            music.play("walen_gameboy_(freetouse.com)")
        else:
            music.stop()
    if key == keys.RETURN and counter == 0:
        options["start"] = True
    if key == keys.ESCAPE and options["start"]:
        options["start"] = False

def update():
    global level
    global is_sword_playing

    if options["exit"]:
        exit()
    if not options["start"]:
        return
    if player.life <= 0:
        options["start"] = False
        player.life = 100
        level = 1
        enemies.clear()
    if len(enemies) == 0:
        level += 1
        for _ in range(level):
            enemies.append(Enemy(f'orc{random.randint(1, 2)}', (random.randint(0, WIDTH), random.randint(*Y_LIMITS))))
    player.update()
    if keyboard.space:
        player.is_attacking = True
        print(is_sword_playing)
        if not is_sword_playing and options["sound_effects"]:
            sounds.sword.play()
            is_sword_playing = True
            clock.schedule_unique(reset_sword, sounds.sword.get_length()/3)
    for enemy in enemies:
        enemy.update()
        dist = calculate_distance(player.actor.x, player.actor.y, enemy.actor.x, enemy.actor.y)
        if dist < 50 and player.is_attacking:
            player.attack(enemy)


        if dist < 10 and not enemy.is_attacking:
            enemy.is_attacking = True
            enemy.attack(player)
            # enemy.is_attacking = False
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
    screen.draw.text(f'Player Life: {player.life}', topleft=(11, 11), fontsize=30, color="black")
    screen.draw.text(f'Player Life: {player.life}', topleft=(10, 10), fontsize=30, color="yellow")
    player.draw()
    for enemy in enemies:
        enemy.draw()
        screen.draw.text(f'{enemy.life}', topleft=(enemy.actor.x-10, enemy.actor.y - 35), fontsize=30, color="red" if enemy.life < 20 else "green")

music.play("walen_gameboy_(freetouse.com)")
music.set_volume(0.15)


pgzrun.go()
