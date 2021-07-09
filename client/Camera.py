import Global as g
from Objects.Object import Object
import pygame as pg
import math


class Camera:
    def __init__(self, pos: tuple, size: tuple, fps: int, speed: int = 400):
        self.shift = (0, 0)
        self.place = pg.Rect(pos[0] - size[0] / 2, pos[1] - size[1] / 2, size[0], size[1])
        self.fps = fps
        self.speed = speed

    def set_shift(self, degrees: int, index: float = 0.05):
        dx = self.place.height * index * math.cos(math.radians(degrees))
        dy = -self.place.height * index * math.sin(math.radians(degrees))
        self.shift = (dx, dy)

    def get_position_over(self, object: Object, with_shift: bool = True):
        ox, oy = object.place.center
        cx, cy = self.place.size
        sx, sy = self.shift if with_shift else (0, 0)
        return ox - cx / 2 + sx, oy - cy / 2 + sy

    def set_position_over(self, object: Object, with_shift: bool = True):
        x, y = object.place.center
        csize = self.place.size
        self.place.x = x - csize[0] / 2
        self.place.y = y - csize[1] / 2
        if with_shift:
            self.place.move_ip(self.shift)

    def move_to(self, pos: tuple):
        x, y = self.place.topleft
        rx, ry = pos
        speed = int(self.speed / self.fps)
        if self.speed != 0 and abs((rx - x) / speed) >= 1:
            if rx > x:
                self.place.x += speed
            else:
                self.place.x -= speed
        else:
            self.place.x = rx
        if self.speed != 0 and abs((ry - y) / speed) >= 1:
            if ry > y:
                self.place.y += speed
            else:
                self.place.y -= speed
        else:
            self.place.y = ry

    def move_to_object(self, map, player):
        mpos = self.place.topleft
        rmpos = self.get_position_over(player)
        if mpos != rmpos:
            self.move_to(rmpos)

    def get_map_place(self):
        x, y = self.place.topleft
        return -x, -y

    def get_object_place(self, object: Object):
        x, y = object.place.topleft
        cx, cy = self.place.topleft
        cw, ch = self.place.size
        if cx < x < cx + cw and cy < y < cy + ch:
            return x - cx, y - cy
        else:
            return False
