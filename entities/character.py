import time
from pgzero.actor import Actor

class Character:
    def __init__(self, name, pos, idle_frames, animations, speed=2):
        self.name = name
        self.actor = Actor(idle_frames[0], pos=pos)
        self.idle_frames = idle_frames
        self.animations = animations  # dict: {'up': [], 'down': [], 'left': [], 'right': []}
        self.current_frame_index = 0
        self.animation_speed = 0.1
        self.last_frame_time = time.time()
        self.speed = speed
        self.direction = "idle"

    def _animate(self, frames):
        """Avança o frame da animação atual."""
        now = time.time()
        if now - self.last_frame_time > self.animation_speed:
            self.current_frame_index = (self.current_frame_index + 1) % len(frames)
            self.actor.image = frames[self.current_frame_index]
            self.last_frame_time = now

    def update(self):
        """Atualiza a animação idle se nenhum movimento estiver ativo."""
        self._animate(self.idle_frames)

    def draw(self):
        self.actor.draw()
