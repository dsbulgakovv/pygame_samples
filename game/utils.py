import pygame


def start_display(dis_width, dis_height):
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game')
    return dis


def your_score(display, score, score_font, score_color):
    value = score_font.render("Your Score: " + str(score), True, score_color)
    display.blit(value, [0, 0])


def our_snake(display, snake_color, snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, snake_color, [x[0], x[1], snake_block, snake_block])


def message(display, font_obj, msg_text, msg_color, dis_width, dis_height):
    msg = font_obj.render(msg_text, True, msg_color)
    display.blit(msg, [dis_width / 6, dis_height / 3])