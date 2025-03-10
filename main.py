import pygame
import random
from c_s import *
from variables import *
player = Main_Character()
# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Life Simulator")

# Colors
PURPLE = (150, 80, 255)
WHITE = (255, 255, 255)
PINK = (255, 105, 180)
BLACK = (0, 0, 0)
LIGHT_PINK = (255, 182, 193)
DARK_PURPLE = (100, 50, 200)
GRAY = (200, 200, 200)
# Fonts
font = pygame.font.Font(None, 30)
small_font = pygame.font.Font(None, 24)
smallest_font = pygame.font.Font(None, 18)
# Game Variables
choices =show_choices_and_option(check_available_choices(player))
money = player.money
health = player.health
relationship = 35
attendance = 95
grades = 35
behavior = 75
work_ethic = 95
skill = 35
experience = 75
mood = player.mood
smarts = player.intelligence
relationship_level = 35
property_condition = 35
history = []

# UI Elements
header_rect = pygame.Rect(0, 0, WIDTH, 50)
stats_rect = pygame.Rect(0, 0, 400, 50)
choice_rect = pygame.Rect(400, 250, 420, 230)
history_rect = pygame.Rect(0, 50, 400, 350)
options_rect = pygame.Rect(0, 400, 400, 200)
settings_rect = pygame.Rect(400, 500, 400, 100)

# Buttons
choice_buttons = [
    pygame.Rect(420, 310, 360, 40),
    pygame.Rect(420, 360, 360, 40),
    pygame.Rect(420, 410, 360, 40),
]
# Relationships Page
npc_list = [pygame.Rect(50, 80 + (i * 50), 300, 40) for i in range(6)]
npc_selected = None
interact_button = pygame.Rect(500, 300, 200, 50)

# Properties Page
property_list = [pygame.Rect(50, 80 + (i * 50), 300, 40) for i in range(6)]
property_selected = None
buy_button = pygame.Rect(500, 400, 200, 50)

age_up_button = pygame.Rect(150, 450, 100, 80)
school_button = pygame.Rect(20, 450, 80, 80)
property_button = pygame.Rect(160, 520, 80, 80)
relationships_button = pygame.Rect(300, 450, 80, 80)
back_button = pygame.Rect(10,10,50,80)

# Draw Progress Bar
def draw_progress_bar(x, y, value, max_value, width=200, height=20):
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)  # Border
    fill_width = (value / max_value) * (width - 4)  # Fill width based on value
    pygame.draw.rect(screen, PINK, (x + 2, y + 2, fill_width, height - 4))
def draw_main_screen():
    screen.fill(WHITE)
    
    # Draw UI sections
    pygame.draw.rect(screen, DARK_PURPLE, header_rect)
    pygame.draw.rect(screen, PURPLE, stats_rect)
    pygame.draw.rect(screen, PURPLE, choice_rect)
    pygame.draw.rect(screen, PURPLE, options_rect)
    pygame.draw.rect(screen, PINK, settings_rect)
    # Draw buttons
    for btn in choice_buttons:
        pygame.draw.rect(screen, LIGHT_PINK, btn, border_radius=8)


    pygame.draw.circle(screen, WHITE, age_up_button.center, 40)
    pygame.draw.circle(screen, WHITE, school_button.center, 40)
    pygame.draw.circle(screen, WHITE, relationships_button.center, 40)



    # Draw text
    screen.blit(font.render(f"{player.name} {player.surname} ", True, WHITE), (20, 15))
    screen.blit(font.render("Stats", True, WHITE), (600, 15))
    screen.blit(render_text_list(wrap_text(choices[0],small_font,400),small_font,BLACK), (420, 260))
    screen.blit(font.render("Settings", True, BLACK), (560, 550))

    # Stats text
    screen.blit(small_font.render(f"Age: {player.age}", True, BLACK), (420, 80))
    screen.blit(small_font.render(f"Money: {money}", True, BLACK), (420, 100))

    # Progress Bars
    draw_progress_bar(420, 120, player.health, 100)
    screen.blit(small_font.render(f"Health: {player.health}%", True, BLACK), (630, 120))

    draw_progress_bar(420, 145, player.mood, 100)
    screen.blit(small_font.render(f"Mood: {player.mood}%", True, BLACK), (630, 145))

    draw_progress_bar(420, 170, player.intelligence, 100)
    screen.blit(small_font.render(f"Smarts: {player.intelligence}%", True, BLACK), (630, 170))

    # Choice buttons text
    screen.blit(small_font.render(f"{choices[1]}", True, BLACK), (450, 320))
    screen.blit(small_font.render(f"{choices[2]}", True, BLACK), (450, 370))
    screen.blit(small_font.render(f"{choices[3]}", True, BLACK), (450, 420))

    # Bottom buttons text
    screen.blit(smallest_font.render("Age Up", True, BLACK), (age_up_button.x+ 25, age_up_button.y+30))
    screen.blit(smallest_font.render("School / Career", True, BLACK), (school_button.x + 5, school_button.y + 30))
    screen.blit(smallest_font.render("Relationships", True, BLACK), (relationships_button.x - 5, relationships_button.y + 30))
     
   # Display history log (only last 5 events)
    y_offset = 80
    for event_text in history[-5:]:
        screen.blit(small_font.render(event_text, True, BLACK), (10, y_offset))
        y_offset += 20
    if player.age>13:
        pygame.draw.circle(screen, WHITE, property_button.center, 40)
        screen.blit(smallest_font.render("Property", True, BLACK), (property_button.x + 10, property_button.y + 30))

def draw_relationships_screen():
    pygame.draw.rect(screen, PURPLE, (0, 0, WIDTH, 50))
    screen.blit(font.render("Relationships", True, WHITE), (100, 15))
    pygame.draw.rect(screen, WHITE, back_button, border_radius=15)
    screen.blit(small_font.render("Back", True, BLACK), (30, 20))

    for npc in npc_list:
        pygame.draw.rect(screen, GRAY if npc == npc_selected else WHITE, npc)
        screen.blit(small_font.render("NPC Name - Connection", True, BLACK), (npc.x + 10, npc.y + 10))

    screen.blit(font.render("NPC Stats", True, BLACK), (550, 80))
    screen.blit(small_font.render(f"Age: {player.age}", True, BLACK), (440, 120))
    draw_progress_bar(440, 150, health, 100)
    screen.blit(small_font.render(f"Health: {health}%", True, BLACK), (655, 150))
    draw_progress_bar(440, 180, relationship_level, 100)
    screen.blit(small_font.render(f"Relationship: {relationship_level}%", True, BLACK), (655, 180))

    pygame.draw.rect(screen, PURPLE, interact_button)
    screen.blit(small_font.render("Interact with NPC", True, WHITE), (interact_button.x + 50, interact_button.y + 15))

# School/Job Screen
def draw_school_screen():
    screen.fill(WHITE)
    pygame.draw.rect(screen, PURPLE, (0, 0, WIDTH, 50))
    pygame.draw.rect(screen, GRAY, back_button, border_radius=8)

    screen.blit(font.render("School & Job", True, WHITE), (50, 10))
    screen.blit(small_font.render("Back", True, BLACK), (back_button.x + 15, back_button.y + 5))

    # School Stats
    screen.blit(font.render("Player's Last School", True, BLACK), (50, 80))
    
    screen.blit(small_font.render("Attendance:", True, BLACK), (50, 120))
    draw_progress_bar(200, 120, attendance, 100)

    screen.blit(small_font.render("Grades:", True, BLACK), (50, 160))
    draw_progress_bar(200, 160, grades, 100)

    screen.blit(small_font.render("Behavior:", True, BLACK), (50, 200))
    draw_progress_bar(200, 200, behavior, 100)

    # Job Stats
    screen.blit(font.render("Player's Last Job", True, BLACK), (50, 280))

    screen.blit(small_font.render("Work Ethic:", True, BLACK), (50, 320))
    draw_progress_bar(200, 320, work_ethic, 100)

    screen.blit(small_font.render("Skill:", True, BLACK), (50, 360))
    draw_progress_bar(200, 360, skill, 100)

    screen.blit(small_font.render("Experience:", True, BLACK), (50, 400))
    draw_progress_bar(200, 400, experience, 100)

def draw_properties_screen():
    pygame.draw.rect(screen, PURPLE, (0, 0, WIDTH, 50))
    screen.blit(font.render("Properties", True, WHITE), (100, 15))
    pygame.draw.rect(screen, WHITE, back_button, border_radius=15)
    screen.blit(small_font.render("Back", True, BLACK), (30, 20))

    for prop in property_list:
        pygame.draw.rect(screen, GRAY if prop == property_selected else WHITE, prop)
        screen.blit(small_font.render("Property Address - Price", True, BLACK), (prop.x + 10, prop.y + 10))

    screen.blit(font.render("Property Stats", True, BLACK), (500, 80))
    screen.blit(small_font.render(f"Price: {money}", True, BLACK), (500, 120))
    draw_progress_bar(500, 150, property_condition, 100)
    screen.blit(small_font.render(f"Condition: {property_condition}%", True, BLACK), (710, 150))

    pygame.draw.rect(screen, PURPLE, buy_button)
    screen.blit(small_font.render("Buy This Property", True, WHITE), (buy_button.x + 50, buy_button.y + 15))
current_screen = "main" 
# Game loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen

    # Draw the appropriate screen based on game state
    if current_screen == "main":
        draw_main_screen()
        
    elif current_screen == "relationships":
        draw_relationships_screen()
    elif current_screen == "properties":
        draw_properties_screen()
    elif current_screen == "school":
        draw_school_screen()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if current_screen == "main":
                if age_up_button.collidepoint(mouse_pos):
                    player.age += 1
                    history.append(f"Age {player.age}: {choices[0]}")
                    choices =show_choices_and_option(check_available_choices(player))
                elif choice_buttons[0].collidepoint(mouse_pos):
                    player.choice_results('a',choices)    
                elif choice_buttons[1].collidepoint(mouse_pos):
                    player.choice_results('b',choices)
                elif choice_buttons[2].collidepoint(mouse_pos):
                    player.choice_results('c',choices)
                elif property_button.collidepoint(mouse_pos):
                    current_screen = "properties"  # Switch to properties screen
                elif relationships_button.collidepoint(mouse_pos):
                    current_screen = "relationships"  # Switch to relationships screen

                elif school_button.collidepoint(mouse_pos):
                    current_screen = "school"  # Switch to relationships screen
            elif current_screen in ["relationships", "properties",'school']:
                if back_button.collidepoint(mouse_pos):
                    current_screen = "main"  # Go back to the main screen

    pygame.display.flip()


pygame.quit()
