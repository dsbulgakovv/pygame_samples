import pygame
import random


class Food:
    def __init__(self, color, food_block, dis_width, dis_height):
        self.food_color = color
        self.food_block = food_block
        self.dis_width = dis_width
        self.dis_height = dis_height
        self.x = round(random.randrange(0, self.dis_width - self.food_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, self.dis_height - self.food_block) / 10.0) * 10.0

    def relocate_food(self):
        self.x = round(random.randrange(0, self.dis_width - self.food_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, self.dis_height - self.food_block) / 10.0) * 10.0

    def draw_food(self, display):
        pygame.draw.rect(
            display,
            self.food_color,
            [self.x, self.y, self.food_block, self.food_block]
        )
