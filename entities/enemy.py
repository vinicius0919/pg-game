import time
from random import randint
from .character import Character

class Enemy(Character):
    def __init__(self, name, pos):
        idle_frames = [f'{name}_idle{i:02}' for i in range(1, 5)]
        animations = {
            "up": [f'{name}_run{i:02}' for i in range(9, 17)],
            "left": [f'{name}_run{i:02}' for i in range(17, 25)],
            "right": [f'{name}_run{i:02}' for i in range(25, 32)],
            "down": [f'{name}_run{i:02}' for i in range(1, 9)],
        }
        super().__init__(name, pos, idle_frames, animations, speed=1, damage=5, life=50)
        self.following = False

    def follow(self, target):
        self.following = True
        self.target = target

    def stop_following(self):
        self.following = False

    def update(self):
        if self.following:
            dx = self.target.actor.x - self.actor.x
            dy = self.target.actor.y - self.actor.y

            if abs(dx) > abs(dy):
                self.direction = "right" if dx > 0 else "left"
                self.actor.x += self.speed if dx > 0 else -self.speed
            else:
                self.direction = "down" if dy > 0 else "up"
                self.actor.y += self.speed if dy > 0 else -self.speed

            self._animate(self.animations[self.direction])
        else:
            super().update()
