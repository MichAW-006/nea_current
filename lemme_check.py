import pygame
import sys
from c_s import *
from variables import *
pygame.init()
Game=game()
pygame.display.set_caption("Life Simulator")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
selected_property = None
# Player info

find_property_button = pygame.Rect(600, 60, 150, 50)
header_rect = pygame.Rect(0, 0, 800, 50)

screen = pygame.display.set_mode((800, 600))
back_button=Button(pygame.image.load('back.png').convert_alpha(),0,0,0.13)

# Function to draw a property card
def draw_property_card(x, y, width, height, property):
    card_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, Game.colour_3, card_rect, border_radius=10)

    # Property name
    name_surface = Game.fonts[0].render(property.type, True, BLACK)
    screen.blit(name_surface, (x + 10, y + 10))

    # Property price

    price_surface = Game.fonts[2].render(f"Price: ${property.price:,}", True, BLACK)
    screen.blit(price_surface, (x + 10, y + 50))

    # Property condition
    draw_progress_bar(x + 80, y + 80, property.condition, 100,100,10)
    condition_text = Game.fonts[2].render("Condition:", True, BLACK)
    condition_number =Game.fonts[2].render(f"{property.condition}%", True, BLACK)
    screen.blit(condition_text, (x + 10, y + 80))
    screen.blit(condition_number, (x + 183, y + 80))


    # Property location
    location_surface = Game.fonts[2].render(f"Location: {property.location}", True, BLACK)
    screen.blit(location_surface, (x + 10, y + 110))
    # sell button
    sell_button = pygame.Rect(x + 10, y + height - 40, width - 20, 25)
    pygame.draw.rect(screen, Game.colour_1, sell_button, border_radius=5)
    sell_text = Game.fonts[2].render("Sell this property", True, WHITE)
    screen.blit(sell_text, (x + 20, y + height - 35))



    return card_rect,sell_button

def draw_progress_bar(x, y, value, max_value, width=200, height=20):
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)  # Border
    fill_width = (value / max_value) * (width - 4)  # Fill width based on value
    pygame.draw.rect(screen, Game.colour_2, (x + 2, y + 2, fill_width, height - 4))

def draw_potential_property_screen():
    
    screen.fill(WHITE)
    pygame.draw.rect(screen, Game.colour_2, find_property_button)
    screen.blit(Game.fonts[1].render('Find Properties',True,BLACK),(618,80))
    pygame.draw.rect(screen, Game.colour_1, header_rect)
    back_button.draw(screen)
    # Draw title
    title_surface = Game.fonts[0].render("Available Properties", True, BLACK)
    screen.blit(title_surface, (50, 20))

    # Draw player money
    money_surface = Game.fonts[2].render(f"Money: ${Game.player.money}", True, BLACK)
    screen.blit(money_surface, (800 - 200, 20))

    # Draw property cards
    card_width = 210
    card_height = 220
    margin = 20
    properties_per_row = 3

    for i, property in enumerate(Game.player.properties):
        row = i // properties_per_row
        col = i % properties_per_row
        x = 50 + col * (card_width + margin)
        y = 100 + row * (card_height + margin)
        card_rect,sell_button = draw_property_card(x, y, card_width, card_height, property)

        # Handle buy button clicks
        mouse_pos = pygame.mouse.get_pos()
        if sell_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]: # Left mouse button
                property.buy(Game.player,False)
                

        
running = True
while running:
    screen.fill(WHITE)  
    draw_potential_property_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                        
                                

    pygame.display.flip()

pygame.quit()
