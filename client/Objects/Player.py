import pygame as pg
import math

import Global as g
from Objects.Object import Object


class Player(Object):
    def __init__(self, center_pos: tuple, hitbox_size: tuple, speed: int = 0, angle_speed: int = 0, image: tuple = None,
                 state: int = g.state.default):
        super().__init__(center_pos, hitbox_size, speed, angle_speed, image, state)
        self.image_angle = 0
        self.image_rotate_speed = 500

    def repaint(self):
        pass

    def check_events(self):
        if g.buttons.scope:
            sx, sy = pg.mouse.get_pos()
            px, py = self.place.center
            cx, cy = g.camera.place.topleft
            dx, dy = sx + cx - px, sy + cy - py
            deg = math.degrees(math.atan2(dx, dy)) - 90
            dist = math.sqrt(dx ** 2 + dy ** 2)
            coef = dist / g.camera.place.size[0]
            #print(f'Distance = {dist}, Coef = {coef}, dx = {dx}, dy = {dy}')
            g.camera.set_shift(int(deg), coef * 0.4)
            self.rotate(deg)

        if g.buttons.up and g.buttons.right:
            self.move(45)
            if not g.buttons.scope:
                self.rotate(45)
                g.camera.set_shift(45)
        elif g.buttons.up and g.buttons.left:
            self.move(135)
            if not g.buttons.scope:
                self.rotate(135)
                g.camera.set_shift(135)
        elif g.buttons.down and g.buttons.left:
            self.move(225)
            if not g.buttons.scope:
                self.rotate(225)
                g.camera.set_shift(225)
        elif g.buttons.down and g.buttons.right:
            self.move(315)
            if not g.buttons.scope:
                self.rotate(315)
                g.camera.set_shift(315)
        elif g.buttons.right:
            self.move(0)
            if not g.buttons.scope:
                self.rotate(0)
                g.camera.set_shift(0)
        elif g.buttons.up:
            self.move(90)
            if not g.buttons.scope:
                self.rotate(90)
                g.camera.set_shift(90)
        elif g.buttons.left:
            self.move(180)
            if not g.buttons.scope:
                self.rotate(180)
                g.camera.set_shift(180)
        elif g.buttons.down:
            self.move(270)
            if not g.buttons.scope:
                self.rotate(270)
                g.camera.set_shift(270)
