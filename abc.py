from sys import exit

import pygame
from enum import Enum, auto

Vector2 = pygame.Vector2


class EntityType(Enum):
    PLAYER = 0


class Entity:
    def __init__(self, _type, name):
        self.pos = Vector2()
        self.type = _type
        self.name = name


class Entities(list):
    def append(self, __object) -> None:
        if isinstance(__object, Entity):
            super(Entities, self).append(__object)

    def update(self):
        pass


class Background(pygame.Surface):
    def __init__(self, size, imgs):
        super().__init__(size)
        self.imgs = imgs

    def __unpack_imgs(self):
        pass

    def move(self):
        pass

    def update(self):
        pass


class Camera:
    def __init__(self, _bg, player):
        self.bg = _bg
        self.player = player

    def update(self):
        pass


class Player(Entity):
    def __init__(self, cam, img):
        super().__init__(EntityType.PLAYER, "")
        self.cam = cam
        self.img = img

    def update(self):
        pass


if __name__ == '__main__':
    screen = pygame.display.set_mode((500, 500))
    bg = Background(screen.get_size())

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                exit()

        screen.blit(bg, (0, 0))
