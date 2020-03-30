import pygame


class Wall:
    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

    def update(self, screen):
        pygame.draw.line(screen, (255, 255, 255), (self.start_x, self.start_y), (self.end_x, self.end_y))

