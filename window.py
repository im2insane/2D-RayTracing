import pygame as pygame
import random
from pygame.math import Vector2
from Wall import Wall
from Ray import Ray


class RayWindow:
    def __init__(self, width, height):
        self._height = height
        self._width = width
        self._backgroundColor = (0, 0, 0)
        self._origin_x = width // 2
        self._origin_y = height // 2
        self._color = (255, 255, 255)

        self._walls = [
            Wall(random.randint(0, self._height), random.randint(0, self._width), random.randint(0, self._height),
                 random.randint(0, self._width)) for i in range(5)]
        self._rays = [Ray(i) for i in range(0, 360,1)]

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((self._height, self._width))
        screen_rect = screen.get_rect()
        pygame.display.set_caption("Ray Tracing Example")
        screen.fill(self._backgroundColor)
        print("screen_rect", screen.get_rect())
        print("screen_rect.center", screen_rect.center)



        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill(self._backgroundColor)
            self.updateMousePosition()

            for wall in self._walls:
                wall.update(screen)

            for ray in self._rays:
                ray.update(screen, self._origin_x, self._origin_y, self._walls)

            pygame.display.flip()

    def updateMousePosition(self):
        mouse_positon = pygame.mouse.get_pos()
        self._origin_x = mouse_positon[0]
        self._origin_y = mouse_positon[1]
