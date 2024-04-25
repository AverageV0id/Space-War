import random

import pygame as pg
from space_ship import SpaceShip
from meteor import Meteor
from bulet import Bullet
from helth_bar import HelthBar

pg.init()
pg.font.init()

font = pg.font.SysFont("None", 100)

W = 900
H = 900

screen = pg.display.set_mode((W, H))

score = 0
run = True

player = SpaceShip(450, 450)
helth_bar = HelthBar(450, 100)
all_sprite = pg.sprite.Group(player, helth_bar)
meteors = pg.sprite.Group()
bullets = pg.sprite.Group()

pg.time.set_timer(pg.USEREVENT, 300)
clock = pg.time.Clock()

pg.mouse.set_visible(False)

while run:

    screen.blit(pg.image.load("bg.jpg"), (0, 0))

    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.USEREVENT:
            meteor = Meteor(random.randint(0, W), -10, random.randint(-3, 3), random.randint(2, 8))
            all_sprite.add(meteor)
            meteors.add(meteor)

        if event.type == pg.MOUSEBUTTONUP:
            bullet = Bullet(player.rect.centerx, player.rect.y)
            all_sprite.add(bullet)
            bullets.add(bullet)

    hits = pg.sprite.groupcollide(bullets, meteors, True, True, pg.sprite.collide_circle)

    if hits:
        score += 1

    if pg.sprite.groupcollide([player], meteors, False, True, pg.sprite.collide_circle):
        helth_bar.width -= 30
    for m in meteors:
        if 0 < m.rect.x < W and m.rect.y > H:
            m.kill()

    score_text = font.render(f"{score}", False, "white")
    screen.blit(score_text, (W // 2 - score_text.get_width() // 2, 100))

    all_sprite.draw(screen)
    all_sprite.update()

    pg.display.update()