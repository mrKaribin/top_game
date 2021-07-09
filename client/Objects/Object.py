import Global as g
import pygame as pg
import math


class Object:
    def __init__(self, center_pos: tuple, size: tuple, speed: int = 0, image_url: str = None):
        if image_url is not None:
            self.org_image = pg.transform.scale(pg.image.load(image_url).convert_alpha(), size)
            self.image = self.org_image
        else:
            self.org_image = None
            self.image = None
        self.place = self.image.get_rect(center=center_pos)
        self.real_x = float(self.place.center[0])
        self.real_y = float(self.place.center[1])
        self.speed = speed

    def set_position(self, center_pos):
        cx, cy = center_pos
        w, h = self.place.size
        self.place = pg.Rect(cx - w / 2, cy - h / 2, w, h)
        self.real_x = float(self.place.center[0])
        self.real_y = float(self.place.center[1])

    def rotate(self, degrees):
        self.image = pg.transform.rotate(self.org_image, degrees)

    def move(self, degrees):
        speed = self.speed / g.camera.fps
        dx = speed * math.cos(math.radians(degrees))
        dy = -speed * math.sin(math.radians(degrees))

        self.real_x += dx
        self.real_y += dy
        self.place = self.image.get_rect(center=(self.real_x, self.real_y))

    def update(self):
        self.check_events()

    def check_events(self):
        pass
