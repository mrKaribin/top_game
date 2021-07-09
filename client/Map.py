from PIL import Image
import os.path as path
import pygame as pg
import Global as g


class Map:
    def __init__(self, size):
        self.size = size
        filename = g.dir.images + 'map.png'
        if path.exists(filename):
            self.image = pg.transform.scale(pg.image.load(filename).convert(), size)
        else:
            self.generate(size)
        self.place = self.image.get_rect(topleft=(0, 0))

    def generate(self, size):
        img = Image.new('RGB', self.size)
        ground = Image.open(g.dir.images + 'ground.png')
        ground_size = 60
        ground.thumbnail((ground_size, ground_size))
        width, height = size
        for i in range(int(width / ground_size) + 1):
            for j in range(int(height / ground_size) + 1):
                img.paste(ground, (i * ground_size, j * ground_size))
        filename = g.dir.images + 'map.png'
        img.save(filename)
        self.image = pg.image.load(filename).convert()
