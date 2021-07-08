import pygame as pg
import Global as g
from Objects.Object import Object


class Player(Object):
    def __init__(self, image_url: str, center_pos: tuple, size: tuple, speed):
        super().__init__(image_url, center_pos, size, speed)
