import random

import pygame as pg

class Meteor(pg.sprite.Sprite):
    def __init__(self, x, y, speedx, speedy):
        super().__init__()
        size = random.randint(50, 150)
        self.image = pg.transform.scale(pg.image.load("meteor.png"), (size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.speedx = speedx
        self.speedy = speedy
        self.radius = int(self.rect.width * .85 / 2)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy