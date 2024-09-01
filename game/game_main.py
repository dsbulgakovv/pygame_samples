import pygame
import hydra

from source_snake import Snake
from source_food import Food
from source_dashboard import Dashboard


def game_loop(
        cfg, display, clock,
        x1_change, y1_change,
        game_over, game_close,
        snake_obj, food_obj, dashboard_obj
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

    if (
        snake_obj.cur_x >= cfg.display.dis_width
            or snake_obj.cur_x < 0
            or snake_obj.cur_y >= cfg.display.dis_height
            or snake_obj.cur_y < 0
    ):
        game_close = True

    snake_obj.cur_x += x1_change
    snake_obj.cur_y += y1_change

    # 1 - background
    display.fill(
        tuple(map(lambda y: int(y.strip()), cfg.colors.background_color.split(',')))
    )

    # 2 - Food
    food_obj.draw_food(display)

    # 3 - Snake
    game_close = snake_obj.check_snake(game_close)
    snake_obj.draw_snake(display)

    # 4 - Score
    dashboard_obj.cur_score = snake_obj.length_of_snake - 1
    dashboard_obj.draw_score(display)

    pygame.display.update()

    # relocate food if it is eaten
    if snake_obj.cur_x == food_obj.x and snake_obj.cur_y == food_obj.y:
        food_obj.relocate_food()
        snake_obj.length_of_snake += 1

    clock.tick(cfg.snake.snake_speed)

    return game_over, game_close, x1_change, y1_change


@hydra.main(config_path="configs", config_name="cfg", version_base=None)
def main(cfg):
    pygame.init()
    display = pygame.display.set_mode((cfg.display.dis_width, cfg.display.dis_height))
    pygame.display.set_caption(cfg.main.game_title)
    clock = pygame.time.Clock()

    game_over = False
    game_close = False

    init_x = cfg.display.dis_width / 2
    init_y = cfg.display.dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_obj = Snake(
        init_x, init_y,
        tuple(map(lambda y: int(y.strip()), cfg.colors.snake_color.split(','))),
        cfg.snake.snake_block
    )

    food_obj = Food(
        tuple(map(lambda y: int(y.strip()), cfg.colors.food_color.split(','))),
        cfg.food.block, cfg.display.dis_width, cfg.display.dis_height
    )

    dashboard_obj = Dashboard(
        tuple(map(lambda y: int(y.strip()), cfg.colors.score_color.split(','))),
        cfg.fonts.score_font, cfg.fonts.score_font_size,
        cfg.display.dis_width, cfg.display.dis_height,
        cfg.texts.quit_txt
    )

    while not game_over:
        while game_close:
            display.fill(
                tuple(map(lambda x: int(x.strip()), cfg.colors.background_color.split(',')))
            )

            dashboard_obj.draw_end_dashboard(display)
            dashboard_obj.draw_score(display)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        hydra.core.global_hydra.GlobalHydra.instance().clear()
                        main()

        game_over, game_close, x1_change, y1_change = game_loop(
            cfg, display, clock,
            x1_change, y1_change,
            game_over, game_close,
            snake_obj, food_obj, dashboard_obj
        )

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
