from pygame.math import Vector2
import math
import pygame


class Ray:
    def __init__(self, degree):
        self._degree = degree
        self._length = 1000

    def update(self, screen, mouse_x, mouse_y, walls):
        center = Vector2((mouse_x, mouse_y))
        vector = Vector2()
        vector.from_polar((self._length, self._degree))
        point = self.cast(center,center+vector,walls)

        if point is not None:
            pygame.draw.line(screen, (255, 255, 255), center, point)

    def cast(self, mouse_center, mouse_vector, walls):
        nearest = None
        distance = None
        for wall in walls:
            x1, y1 = wall.start_x, wall.start_y
            x2, y2 = wall.end_x, wall.end_y

            x3, y3 =  int(mouse_center[0]), int(mouse_center[1])
            x4, y4 = int(mouse_vector[0]), int(mouse_vector[1])

            denominator = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
            if denominator == 0:
                break

            t = (((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/denominator)
            u = -(((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3))/denominator)

            if t > 0 and t < 1 and u > 0:
                if nearest is None:
                    nearest = (x1+t*(x2-x1),y1+t*(y2-y1))
                    distance = self.get_distance(x3,y3,x1+t*(x2-x1),y1+t*(y2-y1))
                elif self.get_distance(x3,y3,x1+t*(x2-x1),y1+t*(y2-y1)) < distance:
                    nearest = (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
                    distance = self.get_distance(x3, y3, x1 + t * (x2 - x1), y1 + t * (y2 - y1))
            else:
                pass
        return nearest
    def get_distance(self,x1,y1,x2,y2):
        return math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))