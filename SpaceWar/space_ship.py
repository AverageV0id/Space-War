import pygame as pg


class SpaceShip(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("space_ship.png"), (100, 100))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        self.rect.x = mouse_x
        self.rect.y = mouse_y
