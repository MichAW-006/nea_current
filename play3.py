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
ask_to_be_friends_button = pygame.Rect(500, 400, 200, 50)
ask_to_date_button = pygame.Rect(500, 300, 200, 50)
back_button=Button(pygame.image.load('back.PNG').convert_alpha(),0,0,0.13)
npc_buttons = [pygame.Rect(20, 80 + (i * 50), 300, 40) for i in range(len(Game.npcs))]
selected_npc = None

def draw_progress_bar(x, y, value, max_value, width=200, height=20):
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)  # Border
    fill_width = (value / max_value) * (width - 4)  # Fill width based on value
    pygame.draw.rect(screen, Game.colour_2, (x + 2, y + 2, fill_width, height - 4))

def draw_relationships_screen():
    screen.fill(WHITE)

    pygame.draw.rect(screen, Game.colour_1, header_rect)
    back_button.draw(screen)

    i=0
    for npc in npc_buttons:
        pygame.draw.rect(screen, Game.colour_1, npc)
        screen.blit(Game.fonts[0].render(f"{Game.npcs[i].name} {Game.npcs[i].surname} ", True, BLACK), (npc.x + 10, npc.y + 10))
        i+=1

    # Display stats if an NPC is selected
    if selected_npc is not None:
        display_stats(selected_npc)

def display_stats(npc):
    screen.blit(Game.fonts[0].render(f"{npc.name}'s Stats", True, BLACK), (550, 20))
    screen.blit(Game.fonts[1].render(f"Age: {npc.age}", True, BLACK), (440, 120))
    draw_progress_bar(440, 150, npc.health, 100)
    screen.blit(Game.fonts[1].render("Health", True, BLACK), (655, 150))
    draw_progress_bar(440, 180, npc.relationship_level, 100)
    screen.blit(Game.fonts[1].render("Relationship", True, BLACK), (655, 180))
    screen.blit(Game.fonts[1].render("Money", True, BLACK), (655, 210))
    draw_progress_bar(440, 210, npc.money/100, 100)
    pygame.draw.rect(screen, Game.colour_1, ask_to_be_friends_button)
    screen.blit(Game.fonts[0].render("Offer to be friends", True, WHITE), (ask_to_be_friends_button.x+10, ask_to_be_friends_button.y + 15))
    if npc.age>16:
      pygame.draw.rect(screen, Game.colour_1, ask_to_date_button)
      screen.blit(Game.fonts[0].render("Ask to date", True, WHITE), (ask_to_date_button.x + 10, ask_to_date_button.y + 15))
      


running = True
while running:
    screen.fill(WHITE)  
    draw_relationships_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i,btn in enumerate(npc_buttons):
                if btn.collidepoint(mouse_pos):
                    selected_npc = Game.npcs[i]
                    break
                if selected_npc is not None:
                    if ask_to_date_button.collidepoint(mouse_pos):
                        if selected_npc.to_date() is True:
                          Game.player.relationships.append(selected_npc)
                        Game.actions+=1                   
                    if ask_to_be_friends_button.collidepoint(mouse_pos):
                        if selected_npc.be_friends() is True:
                          Game.player.relationships.append(selected_npc)
                        
                        Game.actions+=1 
                        
                                

    pygame.display.flip()

pygame.quit()
