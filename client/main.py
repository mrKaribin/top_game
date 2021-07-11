import pygame as pg
import Global as g
from Animation import Animation
from Engine import Engine
from Objects.Player import Player
from Map import Map
from Camera import Camera
import sys
import math

if __name__ == '__main__':
    pg.init()
    dis_info = pg.display.Info()
    dis_size = (dis_info.current_w, dis_info.current_h)
    g.size.screen = dis_size
    g.size.camera = dis_size
    g.screen = pg.display.set_mode(g.size.screen)
    clock = pg.time.Clock()

    g.engine = Engine()
    g.map = Map(g.size.map)
    g.camera = Camera((0, 0), g.size.camera, 80, 200)
    player = Player(g.map.place.center, (50, 50), 100, 360,
                    ((g.state.default, Animation(g.dir.images + 'player', (50, 50), 1)), ))
    g.engine.add_object(player, g.types.level.area)
    g.camera.set_position_over(player)

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
                if event.button == 1:
                    g.buttons.fire = True
                if event.button == 3:
                    g.camera.speed = 1000
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
                if event.button == 1:
                    g.buttons.fire = False
                if event.button == 3:
                    g.camera.speed = 200
                    g.buttons.scope = False

        g.camera.move_to_object(map, player)
        g.screen.blit(g.map.image, g.camera.get_map_place())
        g.engine.update()

        pg.display.update()
        clock.tick(g.camera.fps)
