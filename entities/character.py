import time
from pgzero.actor import Actor


WIDTH = 800
HEIGHT = 450
Y_LIMITS = (156, 380)

class Character:
    def __init__(self, name, pos, idle_frames, animations, speed=2, cooldown_time=1, damage=10, life=100):
        self.name = name
        self.actor = Actor(idle_frames[0], pos=pos)
        self.idle_frames = idle_frames
        self.animations = animations  # dict: {'up': [], 'down': [], 'left': [], 'right': []}
        self.current_frame_index = 0
        self.animation_speed = 0.1
        self.last_frame_time = time.time()
        self.speed = speed
        self.direction = "idle"
        self.life = life
        self.damage = damage
        self.cooldown_time = cooldown_time  # segundos
        self.last_attack_time = 0
        self.is_attacking = False
        self.is_defending = False

    def attack(self, target):
        """Realiza um ataque ao alvo."""
        if self.is_attacking and time.time() - self.last_attack_time > self.cooldown_time:
            self.last_attack_time = time.time()
            target.take_damage(self.damage)

    def take_damage(self, amount):
        """Aplica dano ao personagem."""
        self.life -= amount
        if self.life < 0 and not self.is_defending:
            self.life = 0

    def _animate(self, frames):
        """Avança o frame da animação atual."""
        now = time.time()
        if now - self.last_frame_time > self.animation_speed:
            self.current_frame_index = (self.current_frame_index + 1) % len(frames)
            self.actor.image = frames[self.current_frame_index]
            self.last_frame_time = now

    def update(self):
        """Atualiza a animação idle se nenhum movimento estiver ativo."""
        if self.actor.y < Y_LIMITS[0]:
            self.actor.y = Y_LIMITS[0]
        elif self.actor.y > Y_LIMITS[1]:
            self.actor.y = Y_LIMITS[1]
        if self.actor.x < 0:
            self.actor.x = 0
        elif self.actor.x > WIDTH:
            self.actor.x = WIDTH
        
        if self.is_attacking:
            if self.direction == "idle":
                self.direction = "down"
            attack_frames = self.animations.get(f'attack_{self.direction}', [])
            if attack_frames:
                self._animate(attack_frames)
                if self.current_frame_index == len(attack_frames) - 1:
                    self.is_attacking = False
                    self.current_frame_index = 0
        else:
            self._animate(self.idle_frames)

    def draw(self):
        self.actor.draw()
