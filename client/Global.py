import pygame as pg


class buttons:
    up = False
    left = False
    down = False
    right = False

    fire = False
    scope = False


class size:
    screen = (1200, 800)
    map = (5000, 5000)
    camera = (1200, 800)


class types:
    class level:
        ground = 1
        area = 1
        air = 3
        sky = 4

    class image:
        sprite = 1
        drawable = 2


class state:
    default = 1
    moving = 2


engine = None
screen = None
camera = None
map = None


class dir:
    images = 'images\\'
