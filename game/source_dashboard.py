import pygame


def message(display, font_obj, msg_text, msg_color, dis_width, dis_height):
    msg = font_obj.render(msg_text, True, msg_color)
    display.blit(msg, [dis_width / 6, dis_height / 3])


class Dashboard:
    def __init__(self, color, score_font_name, score_font_size, dis_width, dis_height, quit_txt):
        self.dis_width = dis_width
        self.dis_height = dis_height
        self.cur_score = 0
        self.color = color
        self.score_font_obj = pygame.font.SysFont(score_font_name, score_font_size)
        self.quit_txt = quit_txt

    def draw_score(self, display):
        value = self.score_font_obj.render("Your Score: " + str(self.cur_score), True, self.color)
        display.blit(value, [0, 0])

    def draw_end_dashboard(self, display):
        msg = self.score_font_obj.render(self.quit_txt, True, self.color)
        display.blit(msg, [self.dis_width / 6, self.dis_height / 3])
