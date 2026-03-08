from settings import *

class collision_sprite(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill(dark_blue)
        self.rect = self.image.get_rect(center = pos)
