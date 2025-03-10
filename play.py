import pygame
import random
from c_s import *
from variables import *
pygame.init()
Game=game()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Life Simulator")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
header_rect = pygame.Rect(0, 0, 800, 50)
stats_rect = pygame.Rect(0, 0, 400, 50)
choice_rect = pygame.Rect(400, 250, 420, 230)
history_rect = pygame.Rect(0, 50, 400, 350)
options_rect = pygame.Rect(0, 400, 400, 200)
settings_rect = pygame.Rect(400, 500, 400, 100)
choice_buttons = [
pygame.Rect(420, 310, 360, 40),
pygame.Rect(420, 360, 360, 40),
pygame.Rect(420, 410, 360, 40),]
npc_buttons = [
pygame.Rect(420, 310, 360, 40),
pygame.Rect(420, 360, 360, 40),
pygame.Rect(420, 410, 360, 40),
pygame.Rect(420, 360, 360, 40),
pygame.Rect(420, 410, 360, 40)]
conversate_button = pygame.Rect(500, 400, 200, 50)
ask_for_money_button = pygame.Rect(500, 300, 200, 50)
buy_button = pygame.Rect(500, 400, 200, 50)
sell_button = pygame.Rect(500, 400, 200, 50)
age_up_button = Button(pygame.image.load('age_up.png').convert_alpha(),140,395,0.27)
school_button = Button(pygame.image.load('school.png').convert_alpha(),10,450,0.3)
property_button = Button(pygame.image.load('property.png').convert_alpha(),140,495,0.27)
relationships_button = Button(pygame.image.load('relationships.png').convert_alpha(),250,450,0.3)
choices =show_choices_and_option(baby_choices)
def draw_progress_bar(x, y, value, max_value, width=200, height=20):
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)  # Border
    fill_width = (value / max_value) * (width - 4)  # Fill width based on value
    pygame.draw.rect(screen, Game.colour_2, (x + 2, y + 2, fill_width, height - 4))
def draw_main_screen():
    screen.fill(WHITE)

    pygame.draw.rect(screen, Game.colour_1, header_rect)
    pygame.draw.rect(screen, Game.colour_1, stats_rect)
    pygame.draw.rect(screen, Game.colour_2, choice_rect)
    pygame.draw.rect(screen, Game.colour_3, options_rect)
    pygame.draw.rect(screen,Game.colour_1, settings_rect)

    for btn in choice_buttons:
        pygame.draw.rect(screen, Game.colour_3, btn, border_radius=8)


    age_up_button.draw(screen)
    school_button.draw(screen) 
    relationships_button.draw(screen)
    property_button.draw(screen)
    screen.blit(Game.fonts[0].render(f"{Game.player.name} {Game.player.surname}", True, WHITE), (20, 15))
    screen.blit(Game.fonts[0].render("Stats", True, WHITE), (600, 15))
    screen.blit(Game.fonts[0].render("Settings", True, BLACK), (560, 550))
    screen.blit(render_text_list(wrap_text(choices[0],Game.fonts[1],400),Game.fonts[1],BLACK), (420, 260))
    screen.blit(Game.fonts[1].render(f"{choices[1]}", True, BLACK), (450, 320))
    screen.blit(Game.fonts[1].render(f"{choices[2]}", True, BLACK), (450, 370))
    screen.blit(Game.fonts[1].render(f"{choices[3]}", True, BLACK), (450, 420))
    # Stats text
    screen.blit(Game.fonts[1].render(f"Age: {Game.player.age}", True, BLACK), (420, 80))
    screen.blit(Game.fonts[1].render(f"Money: {Game.player.money}", True, BLACK), (420, 100))

    # Progress Bars
    draw_progress_bar(420, 120, Game.player.health, 100)
    screen.blit(Game.fonts[1].render(f"Health: {Game.player.health}%", True, BLACK), (630, 120))

    draw_progress_bar(420, 145, Game.player.mood, 100)
    screen.blit(Game.fonts[1].render(f"Mood: {Game.player.mood}%", True, BLACK), (630, 145))

    draw_progress_bar(420, 170, Game.player.intelligence, 100)
    screen.blit(Game.fonts[1].render(f"Smarts: {Game.player.intelligence}%", True, BLACK), (630, 170))

    y_offset = 80
    for event_text in Game.history[-5:]:
        screen.blit(render_text_list(wrap_text(event_text,Game.fonts[1],400),Game.fonts[1],BLACK), (10, y_offset))
        y_offset += 20


running = True
while running:
    screen.fill(WHITE)  # Clear the screen
    draw_main_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if age_up_button.rect.collidepoint(mouse_pos):
                        Game.player.age += 1
                        Game.history.append(f"Age {Game.player.age}: {choices[0]}")
                        Game.history.append('')
                        choices =show_choices_and_option(check_available_choices(Game.player))


    pygame.display.flip()

pygame.quit()
