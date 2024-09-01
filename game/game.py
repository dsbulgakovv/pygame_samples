import pygame
import random
import hydra

from utils import start_display, your_score, our_snake, message


def game_loop(
        cfg, display, score_font_obj, clock,
        x1, y1, x1_change, y1_change, food_x, food_y, snake_list,
        length_of_snake,
        game_over, game_close
):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -cfg.snake.snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = cfg.snake.snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -cfg.snake.snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = cfg.snake.snake_block
                x1_change = 0

    if x1 >= cfg.display.dis_width or x1 < 0 or y1 >= cfg.display.dis_height or y1 < 0:
        game_close = True
    x1 += x1_change
    y1 += y1_change
    display.fill(
        tuple(map(lambda y: int(y.strip()), cfg.colors.background_color.split(',')))
    )
    pygame.draw.rect(
        display,
        tuple(map(lambda y: int(y.strip()), cfg.colors.food_color.split(','))),
        [food_x, food_y, cfg.snake.snake_block, cfg.snake.snake_block]
    )
    snake_head = list()
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > length_of_snake:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_close = True

    our_snake(
        display,
        tuple(map(lambda y: int(y.strip()), cfg.colors.snake_color.split(','))),
        cfg.snake.snake_block, snake_list
    )
    your_score(
        display, length_of_snake-1, score_font_obj,
        tuple(map(lambda y: int(y.strip()), cfg.colors.score_color.split(',')))
    )

    pygame.display.update()

    if x1 == food_x and y1 == food_y:
        food_x = round(random.randrange(0, cfg.display.dis_width - cfg.snake.snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, cfg.display.dis_height - cfg.snake.snake_block) / 10.0) * 10.0
        length_of_snake += 1

    clock.tick(cfg.snake.snake_speed)

    return game_over, game_close, food_x, food_y, x1, y1, x1_change, y1_change, snake_list, length_of_snake


@hydra.main(config_path="configs", config_name="cfg", version_base=None)
def main(cfg):
    pygame.init()
    display = start_display(cfg.display.dis_width, cfg.display.dis_height)
    clock = pygame.time.Clock()
    font_style_obj = pygame.font.SysFont(cfg.fonts.font_style, cfg.fonts.font_style_size)
    score_font_obj = pygame.font.SysFont(cfg.fonts.score_font, cfg.fonts.score_font_size)

    game_over = False
    game_close = False

    x1 = cfg.display.dis_width / 2
    y1 = cfg.display.dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = list()
    length_of_snake = 1

    food_x = round(random.randrange(0, cfg.display.dis_width - cfg.snake.snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, cfg.display.dis_height - cfg.snake.snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close is True:
            display.fill(
                tuple(map(lambda x: int(x.strip()), cfg.colors.background_color.split(',')))
            )
            message(
                display, font_style_obj, cfg.texts.quit_txt,
                tuple(map(lambda x: int(x.strip()), cfg.colors.red.split(','))),
                cfg.display.dis_width, cfg.display.dis_height
            )
            your_score(
                display, length_of_snake-1, score_font_obj,
                tuple(map(lambda x: int(x.strip()), cfg.colors.score_color.split(',')))
            )
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        main()

        game_over, game_close, food_x, food_y, x1, y1, x1_change, y1_change, snake_list, length_of_snake = game_loop(
            cfg, display, score_font_obj, clock,
            x1, y1, x1_change, y1_change, food_x, food_y, snake_list,
            length_of_snake,
            game_over, game_close
        )

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
