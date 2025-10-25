import time
from pgzero.keyboard import keyboard
from .character import Character

class Player(Character):
    def __init__(self, pos):
        idle_frames = [f'idle{i:02}' for i in range(1, 41)]
        animations = {
            "up": [f'run{i:02}' for i in range(1, 9)],
            "left": [f'run{i:02}' for i in range(9, 17)],
            "right": [f'run{i:02}' for i in range(17, 25)],
            "down": [f'run{i:02}' for i in range(25, 33)],
        }
        super().__init__("player", pos, idle_frames, animations, speed=5)

    def update(self):
        moved = False

        if keyboard.left or keyboard.a:
            self.actor.x -= self.speed
            self.direction = "left"
            moved = True
        elif keyboard.right or keyboard.d:
            self.actor.x += self.speed
            self.direction = "right"
            moved = True
        elif keyboard.up or keyboard.w:
            self.actor.y -= self.speed
            self.direction = "up"
            moved = True
        elif keyboard.down or keyboard.s:
            self.actor.y += self.speed
            self.direction = "down"
            moved = True

        if moved:
            self._animate(self.animations[self.direction])
        else:
            self._animate(self.idle_frames)
