#player
from settings import *

class player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        # lists of images for each direction
        self.images = {
            'up': [pygame.transform.scale(pygame.image.load(f'../images/mizu/U{i}.png').convert_alpha(), (50, 80)) for i in range(3)],
            'down': [pygame.transform.scale(pygame.image.load(f'../images/mizu/D{i}.png').convert_alpha(), (50, 80)) for i in range(3)],
            'left': [pygame.transform.scale(pygame.image.load(f'../images/mizu/L{i}.png').convert_alpha(), (50, 80)) for i in range(3)],
            'right': [pygame.transform.scale(pygame.image.load(f'../images/mizu/R{i}.png').convert_alpha(), (50, 80)) for i in range(3)],
        }

        self.direction_facing = 'down'
        self.frame_index = 0
        self.image = self.images[self.direction_facing][self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # movement
        self.direction = pygame.Vector2()
        self.speed = 300
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

            if self.direction.x > 0:
                self.direction_facing = 'right'
            elif self.direction.x < 0:
                self.direction_facing = 'left'
            elif self.direction.y < 0:
                self.direction_facing = 'up'
            elif self.direction.y > 0:
                self.direction_facing = 'down'

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

    def animate(self):
        if self.direction.length() > 0:
            # move to next frame, looping automatically
            self.frame_index = (self.frame_index + 1) % len(self.images[self.direction_facing])
        else:
            self.frame_index = 0
        self.image = self.images[self.direction_facing][self.frame_index]

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate()