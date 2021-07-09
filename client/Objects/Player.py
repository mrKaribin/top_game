import pygame as pg
import math

import Global as g
from Objects.Object import Object


class Player(Object):
    def __init__(self, image_url: str, center_pos: tuple, size: tuple, speed):
        super().__init__(center_pos, size, speed, image_url)
        self.image_angle = 0
        self.image_rotate_speed = 500

    def repaint(self):
        pass

    def check_events(self):
        if g.buttons.scope:
            sx, sy = pg.mouse.get_pos()
            px, py = self.place.center
            cx, cy = g.camera.place.topleft
            deg = math.degrees(math.atan2(sx + cx - px, sy + cy - py)) - 90
            dist = math.sqrt(abs((2 * (sx + cx - px) + 2 * (sy + cy - py))))
            print(f'Distance = {dist}')
            coef = dist / g.camera.place.size[0] / 2
            g.camera.set_shift(int(deg), coef * 0.3)
            # g.camera.speed = 1 + int(1000 * coef)
            self.rotate(deg)

        if g.buttons.up and g.buttons.right:
            self.move(45)
            if not g.buttons.scope:
                #self.rotate(45)
                g.camera.set_shift(45)
        elif g.buttons.up and g.buttons.left:
            self.move(135)
            if not g.buttons.scope:
                #self.rotate(135)
                g.camera.set_shift(135)
        elif g.buttons.down and g.buttons.left:
            self.move(225)
            if not g.buttons.scope:
                #self.rotate(225)
                g.camera.set_shift(225)
        elif g.buttons.down and g.buttons.right:
            self.move(315)
            if not g.buttons.scope:
                #self.rotate(315)
                g.camera.set_shift(315)
        elif g.buttons.right:
            self.move(0)
            if not g.buttons.scope:
                #self.rotate(0)
                g.camera.set_shift(0)
        elif g.buttons.up:
            self.move(90)
            if not g.buttons.scope:
                #self.rotate(90)
                g.camera.set_shift(90)
        elif g.buttons.left:
            self.move(180)
            if not g.buttons.scope:
                #self.rotate(180)
                g.camera.set_shift(180)
        elif g.buttons.down:
            self.move(270)
            if not g.buttons.scope:
                #self.rotate(270)
                g.camera.set_shift(270)

        center = self.place.center
        self.image_angle -= self.image_rotate_speed / g.camera.fps
        self.image = pg.transform.rotate(self.org_image, self.image_angle)
        self.place = self.image.get_rect(center=center)
