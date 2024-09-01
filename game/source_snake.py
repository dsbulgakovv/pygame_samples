import pygame


class Snake:
    def __init__(self, init_x, init_y, color, snake_block):
        self.snake_list = list()
        self.snake_color = color
        self.cur_x = init_x
        self.cur_y = init_y
        self.snake_block = snake_block
        self.length_of_snake = 1

    def check_snake(self, game_close_flg):
        snake_head = list()
        snake_head.append(self.cur_x)
        snake_head.append(self.cur_y)
        self.snake_list.append(snake_head)
        if len(self.snake_list) > self.length_of_snake:
            del self.snake_list[0]

        for x in self.snake_list[:-1]:
            if x == snake_head:
                game_close_flg = True

        return game_close_flg

    def draw_snake(self, display):
        for x in self.snake_list:
            pygame.draw.rect(
                display,
                self.snake_color,
                [x[0], x[1], self.snake_block, self.snake_block]
            )

