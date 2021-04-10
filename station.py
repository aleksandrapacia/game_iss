import pygame


class Station:
    def __init__(self, pos_x: int, pos_y: int, texture: pygame.Surface):
        self.pos_x = pos_x
        self.pox_y = pos_y
        self.texture = texture
