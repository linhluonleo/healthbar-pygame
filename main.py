import sys

import pygame

pygame.init()

screen_w, screen_h = 800, 450
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("HealthBar")


class Healthbar:
    def __init__(self, x, y, max_hp):
        self.x = x
        self.y = y
        self.w = 400
        self.h = 40
        self.hp = max_hp
        self.max_hp = max_hp

    def draw_hp1(self, surface):
        font = pygame.font.Font(None, 50)
        text = f"{self.hp}/{self.max_hp}"
        text_render = font.render(text, True, "white")
        surface.blit(text_render, (self.x, self.y))

    def draw_hp2(self, surface):
        ratio_hp = self.hp / self.max_hp
        y = self.y + 70
        hp_rect = pygame.Rect(self.x, y, self.w * ratio_hp, self.h)
        max_hp_rect = pygame.Rect(self.x, y, self.w, self.h)
        pygame.draw.rect(surface, "red", max_hp_rect)
        pygame.draw.rect(surface, "green", hp_rect)

    def draw_hp3(self, surface):
        ratio_hp = self.hp / self.max_hp
        y = self.y + 120 + self.h
        hp_rect = pygame.Rect(self.x, y, self.w * ratio_hp, self.h)
        max_hp_rect = pygame.Rect(self.x, y, self.w, self.h)
        pygame.draw.rect(surface, "red", max_hp_rect)
        pygame.draw.rect(surface, "green", hp_rect)

    def draw_hp4(self, surface):
        pass


healthbar = Healthbar(50, 50, 100)

running = True
while running:
    screen.fill("black")
    healthbar.draw_hp1(screen)
    healthbar.draw_hp2(screen)
    healthbar.draw_hp3(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                if healthbar.hp == 0:
                    healthbar.hp = 0
                else:
                    healthbar.hp -= 5
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                if healthbar.hp == healthbar.max_hp:
                    healthbar.hp = healthbar.max_hp
                else:
                    healthbar.hp += 5
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                if healthbar.max_hp == 50:
                    healthbar.max_hp = 50
                else:
                    healthbar.max_hp -= 5
            if pygame.key.get_pressed()[pygame.K_UP]:
                healthbar.max_hp += 5

    clock.tick(60)
    pygame.display.update()

pygame.quit()
sys.exit()
