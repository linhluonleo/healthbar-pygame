import sys
import time

import pygame

pygame.init()

screen_w, screen_h = 800, 450
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("HealthBar1")


class Healthbar:
    def __init__(self, maximum_health):
        self.maximum_health = maximum_health
        self.current_health = maximum_health
        self.healthbar_w = 400
        self.healthbar_h = 40

    def get_damage(self, amount):
        if self.current_health != 0:
            self.current_health -= amount

    def get_health(self, amount):
        if self.current_health != self.maximum_health:
            self.current_health += amount

    def healthbar(self, surface):
        self.ratio_health = self.current_health / self.maximum_health
        self.healthbar_rect_x = (screen_w / 2) - (self.healthbar_w / 2)
        self.healthbar_rect_y = (screen_h / 2) - (self.healthbar_h / 2)
        self.healthbar_rect = pygame.Rect(
            self.healthbar_rect_x,
            self.healthbar_rect_y,
            self.healthbar_w,
            self.healthbar_h,
        )
        self.current_healthbar_rect = pygame.Rect(
            self.healthbar_rect_x,
            self.healthbar_rect_y,
            self.healthbar_w * self.ratio_health,
            self.healthbar_h,
        )
        pygame.draw.rect(
            surface,
            "red",
            self.healthbar_rect,
        )
        pygame.draw.rect(
            surface,
            (0, 204, 0),
            self.current_healthbar_rect,
        )
        pygame.draw.rect(
            surface,
            (192, 192, 192),
            self.healthbar_rect,
            4,
        )


player = Healthbar(100)
health_amount = 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                player.get_damage(health_amount)
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                player.get_health(health_amount)
    screen.fill((64, 64, 64))
    player.healthbar(screen)

    font = pygame.font.Font(None, 50)
    health_text = f"{player.current_health}/{player.maximum_health}"
    health_text_render = font.render(health_text, True, "white")
    menu_render = font.render(
        f"""Press LEFT Key: +{health_amount} hp
Press RIGHT Key : +{health_amount} hp""",
        True,
        "white",
    )
    screen.blit(menu_render, (30, 70))
    screen.blit(health_text_render, (30, 30))

    clock.tick(60)
    pygame.display.update()
pygame.quit()
sys.exit()
