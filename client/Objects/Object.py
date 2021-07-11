import Global as g
import pygame as pg
import math


class Object:
    def __init__(self, center_pos: tuple, hitbox_size: tuple, speed: int = 0, angle_speed: int = 0, image: tuple = None,
                 state: int = g.state.default):
        if image is not None:
            self.image_type = g.types.image.sprite
            self.animations = {}
            for anim in image:
                state, animation = anim
                self.animations[state] = animation
        else:
            self.image_type = g.types.image.drawable
            self.repaint()
        self.__state__ = None
        self.animation = None
        self.__dx__ = 0
        self.__dy__ = 0
        self.__dr__ = 0
        self.rotation = 0
        self.rotation_angle = 0
        self.speed = speed
        self.angle_speed = angle_speed
        self.set_state(state)
        self.__orig_image__ = self.animation.frame()
        self.image = self.__orig_image__
        self.place = self.image.get_rect(center=center_pos)
        self.hitbox = pg.Rect(center_pos[0] - hitbox_size[0] / 2, center_pos[1] - hitbox_size[1] / 2, hitbox_size[0], hitbox_size[1])
        self.level = None

    def set_position(self, center_pos):
        cx, cy = center_pos
        self.place = self.image.get_rect(center=center_pos)
        w, h = self.hitbox.size
        self.hitbox = pg.Rect(cx - w / 2, cy - h / 2)

    def set_state(self, state):
        self.__state__ = state
        if (animation := self.animations.get(state)) is not None:
            self.animation = animation

    def get_state(self):
        return self.__state__

    def rotate(self, degrees):
        if self.rotation + self.rotation_angle != degrees:
            if (a1 := degrees - self.rotation) < (a2 := self.rotation + 360 - degrees):
                self.rotation_angle = a1
            else:
                self.rotation_angle = -a2

    def move(self, degrees):
        speed = self.speed / g.camera.fps
        self.__dx__ += speed * math.cos(math.radians(degrees))
        self.__dy__ += -speed * math.sin(math.radians(degrees))

    def update(self):
        self.check_events()
        self.check_image()

    def check_image(self):
        if self.animation.update():
            self.__orig_image__ = self.animation.frame()

        aspeed = self.angle_speed / g.camera.fps
        if self.rotation_angle != 0:
            if abs(self.rotation_angle) > aspeed:
                self.__dr__ += aspeed if self.rotation_angle > 0 else -aspeed
            else:
                self.__dr__ += self.rotation_angle
            self.rotation_angle -= self.__dr__
            dr = round(self.__dr__)
            self.__dr__ -= dr
            self.rotation += dr
            self.image = pg.transform.rotate(self.__orig_image__, self.rotation)
            self.place = self.image.get_rect(center=self.place.center)

        dx = round(self.__dx__)
        dy = round(self.__dy__)
        self.__dx__ -= dx
        self.__dy__ -= dy
        self.place.move_ip(dx, dy)

    def check_events(self):
        pass

    def repaint(self):
        pass
