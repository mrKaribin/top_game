import pygame as pg
import Global as g
from Objects.Object import Object


class Engine:
    def __init__(self):
        self._ground_ = []
        self._area_ = []
        self._air_ = []
        self._sky_ = []

    def add_object(self, object: Object, type: int):
        if type == g.types.level.ground:
            self._ground_.append(object)
        elif type == g.types.level.area:
            self._area_.append(object)
        elif type == g.types.level.air:
            self._air_.append(object)
        elif type == g.types.level.sky:
            self._sky_.append(object)
        else:
            return
        object.level = type

    def update(self):
        for level in [self._ground_, self._area_, self._air_, self._sky_]:
            for object in level:
                if object is not None:
                    if (place := g.camera.get_object_place(object)) is not False:
                        object.update()
                        g.screen.blit(object.image, place)
