import pygame
import random
from c_s import *
from variables import *
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tiny Choices")
Game = game()
f=0
club_buttons = [pygame.Rect(50, 300 + (i * 50), 300, 40) for i in range(len(Game.schools[f].clubs))]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
header_rect = pygame.Rect(0, 0, 800, 50)
join_club_button = pygame.Rect(500, 200, 200, 50)
study_harder_button = pygame.Rect(500, 300, 200, 50)
bunk_class_button = pygame.Rect(500, 400, 200, 50)
show_clubs= None
selected_club = None
def draw_progress_bar(x, y, value, max_value, width=200, height=20):
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)  # Border
    fill_width = (value / max_value) * (width - 4)  # Fill width based on value
    pygame.draw.rect(screen, Game.colour_2, (x + 2, y + 2, fill_width, height - 4))
def draw_school_screen():
    
    screen.fill(WHITE)
    pygame.draw.rect(screen, Game.colour_1, header_rect)
    global club_buttons
    global f
    if Game.player.age >=18:
        f = 2
    if Game.player.age >=11:
        f = 1

    

    screen.blit(Game.fonts[0].render(f"{Game.schools[f].name}", True, WHITE), (20, 15))
    draw_progress_bar(50, 70, Game.schools[f].attendance, 100)
    screen.blit(Game.fonts[1].render("Attendance", True, BLACK), (270, 70))
    draw_progress_bar(50, 120, Game.schools[f].behaviour, 100)
    screen.blit(Game.fonts[1].render("Behaviour", True, BLACK), (270, 120))
    draw_progress_bar(50, 170, Game.schools[f].grades, 100)
    screen.blit(Game.fonts[1].render("Grade", True, BLACK), (270, 170))
    pygame.draw.rect(screen,Game.colour_1, join_club_button)
    screen.blit(Game.fonts[1].render("Join a Club", True, BLACK), (550, 215))
    pygame.draw.rect(screen,Game.colour_1, study_harder_button)
    screen.blit(Game.fonts[1].render("Study Harder", True, BLACK), (550, 315))
    pygame.draw.rect(screen,Game.colour_1, bunk_class_button)
    screen.blit(Game.fonts[1].render("Bunk Class", True, BLACK), (550, 415))
    if show_clubs is not None:
        display_clubs()

def display_clubs(): 
    i=0
    for club in club_buttons:
        pygame.draw.rect(screen, Game.colour_1, club)
        screen.blit(Game.fonts[0].render(f"{Game.schools[f].clubs[i]}", True, BLACK), (club.x + 10, club.y + 10))
        i+=1




running = True
while running:
    screen.fill(WHITE)  # Clear the screen

    draw_school_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if join_club_button.collidepoint(mouse_pos):
                show_clubs = True
            for i,btn in enumerate(club_buttons):
                if btn.collidepoint(mouse_pos):
                    selected_club = Game.schools[f].clubs[i]
                    break
                if selected_club is not None:
                    print(f'joined {selected_club}') 

    pygame.display.flip()

pygame.quit()
