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
buy_button = pygame.Rect(400, 400, 300, 50)
mortgage_button = pygame.Rect(400, 500, 300, 50)
sell_button = pygame.Rect(400, 300, 300, 50)
back_button=Button(pygame.image.load('back.png').convert_alpha(),0,0,0.13)
property_buttons = [pygame.Rect(20, 80 + (i * 50), 300, 40) for i in range(len(Game.properties))]
selected_property = None

def draw_progress_bar(x, y, value, max_value, width=200, height=20):
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)  # Border
    fill_width = (value / max_value) * (width - 4)  # Fill width based on value
    pygame.draw.rect(screen, Game.colour_2, (x + 2, y + 2, fill_width, height - 4))

def draw_properties_screen():
    screen.fill(WHITE)

    pygame.draw.rect(screen, Game.colour_1, header_rect)
    back_button.draw(screen)

    i=0
    for npc in property_buttons:
        pygame.draw.rect(screen, Game.colour_1, npc)
        screen.blit(Game.fonts[0].render(f"{Game.properties[i].type}  ", True, BLACK), (npc.x + 10, npc.y + 10))
        i+=1

    
    
    # Display stats if an NPC is selected
    if selected_property is not None:
        display_stats(selected_property)

def display_stats(property):
    screen.blit(Game.fonts[0].render("Property Stats", True, BLACK), (400, 80))
    screen.blit(Game.fonts[1].render(f"Price: {property.price}", True, BLACK), (400, 120))
    screen.blit(render_text_list(wrap_text(property.location,Game.fonts[1],400),Game.fonts[1],BLACK), (400, 220))
    pygame.draw.rect(screen, Game.colour_1, buy_button)
    draw_progress_bar(400, 150, property.condition, 100)
    screen.blit(Game.fonts[1].render(f"Condition: {property.condition}%", True, BLACK), (610, 150))
    screen.blit(Game.fonts[0].render("Buy With Cash", True, BLACK), (buy_button.x + 50, buy_button.y + 15))
    pygame.draw.rect(screen, Game.colour_1, mortgage_button)
    screen.blit(Game.fonts[0].render("Apply For Mortgage", True, BLACK), (mortgage_button.x + 50, mortgage_button.y + 15))
    pygame.draw.rect(screen, Game.colour_1, sell_button)
    screen.blit(Game.fonts[0].render("sell This Property", True, BLACK), (sell_button.x + 50, sell_button.y + 15))


running = True
while running:
    screen.fill(WHITE)  
    draw_properties_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i,btn in enumerate(property_buttons):
                if btn.collidepoint(mouse_pos):
                    selected_property = Game.properties[i]
                    break
                if selected_property is not None:
                    if buy_button.collidepoint(mouse_pos):
                        selected_property.buy(Game.player,True)    
                        Game.actions+=1                   
                    if sell_button.collidepoint(mouse_pos):
                        selected_property.sell(Game.player)
                        Game.actions+=1 
                        
                                

    pygame.display.flip()

pygame.quit()

