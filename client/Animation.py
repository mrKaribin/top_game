import pygame as pg
import Global as g
import os.path as path


class Animation:
    def __init__(self, dir: str, size: tuple, fps: int, angle: int = None):
        self.frames = []
        i = 1
        while path.exists(f'{dir}{i}.png'):
            image = pg.transform.scale(pg.image.load(f'{dir}{i}.png').convert_alpha(), size)
            if angle is not None:
                image = pg.transform.rotate(image, angle)
            self.frames.append(image)
            i += 1
        self.current = -1
        self.fps = fps
        self.count = 0

    def start(self):
        self.current = -1
        self.count = 0

    def increase(self):
        self.current += 1
        if self.current >= len(self.frames):
            self.current = 0

    def update(self):
        if self.fps != 0:
            if g.camera.fps / self.fps < self.count:
                self.count = 0
                self.increase()
                return True
        return False

    def frame(self):
        return self.frames[self.current]
