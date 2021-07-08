import pygame as pg
import Global as g
from Objects.Player import Player
from Map import Map
from Camera import Camera
import sys
import math

if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode(g.size.screen)
    clock = pg.time.Clock()

    g.map = Map(g.size.map)
    player = Player(g.dir.images + 'player.png', g.map.place.center, (45, 30), 100)
    g.camera = Camera(player.place.center, g.size.camera, 100, 200)
    print(g.map.place.topleft, g.map.place.size)
    print(player.place.topleft, player.place.size)

    lastPos = player.place.topleft
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    g.buttons.up = True
                if event.key == pg.K_s:
                    g.buttons.down = True
                if event.key == pg.K_a:
                    g.buttons.left = True
                if event.key == pg.K_d:
                    g.buttons.right = True
            if event.type == pg.MOUSEBUTTONDOWN:
                g.camera.speed = 0
                if event.button == 1:
                    g.buttons.fire = True
                if event.button == 3:
                    g.buttons.scope = True

            if event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    g.buttons.up = False
                if event.key == pg.K_s:
                    g.buttons.down = False
                if event.key == pg.K_a:
                    g.buttons.left = False
                if event.key == pg.K_d:
                    g.buttons.right = False
            if event.type == pg.MOUSEBUTTONUP:
                g.camera.speed = 200
                if event.button == 1:
                    g.buttons.fire = False
                if event.button == 3:
                    g.buttons.scope = False

        if g.buttons.scope:
            sx, sy = pg.mouse.get_pos()
            px, py = player.place.center
            cx, cy = g.camera.place.topleft
            deg = math.degrees(math.atan2(sx + cx - px, sy + cy - py)) - 90
            player.rotate(deg)
            g.camera.set_shift(int(deg), 0.2)

        if g.buttons.up and g.buttons.right:
            player.move(45)
            if not g.buttons.scope:
                player.rotate(45)
                g.camera.set_shift(45)
        elif g.buttons.up and g.buttons.left:
            player.move(135)
            if not g.buttons.scope:
                player.rotate(135)
                g.camera.set_shift(135)
        elif g.buttons.down and g.buttons.left:
            player.move(225)
            if not g.buttons.scope:
                player.rotate(225)
                g.camera.set_shift(225)
        elif g.buttons.down and g.buttons.right:
            player.move(315)
            if not g.buttons.scope:
                player.rotate(315)
                g.camera.set_shift(315)
        elif g.buttons.right:
            player.move(0)
            if not g.buttons.scope:
                player.rotate(0)
                g.camera.set_shift(0)
        elif g.buttons.up:
            player.move(90)
            if not g.buttons.scope:
                player.rotate(90)
                g.camera.set_shift(90)
        elif g.buttons.left:
            player.move(180)
            if not g.buttons.scope:
                player.rotate(180)
                g.camera.set_shift(180)
        elif g.buttons.down:
            player.move(270)
            if not g.buttons.scope:
                player.rotate(270)
                g.camera.set_shift(270)

        g.camera.move_to_object(map, player)
        screen.blit(g.map.image, g.camera.get_map_place())
        if (place := g.camera.get_object_place(player)) is not False:
            screen.blit(player.image, place)

        pg.display.update()
        clock.tick(g.camera.fps)
