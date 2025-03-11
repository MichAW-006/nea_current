# Import necessary libraries
import pygame
import sys
from pygame.locals import *
from c_s import *
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Life Simulator")
new_game_button=Button(pygame.image.load('new_game.PNG').convert_alpha(),400,305,1)
resume_button=Button(pygame.image.load('resume.PNG').convert_alpha(),400,380,1)
options_button=Button(pygame.image.load('settings.PNG').convert_alpha(),405,450,1)
quit_button=Button(pygame.image.load('quit.PNG').convert_alpha(),400,530,1)
# Flag to control the game loop
running = True

def draw_start_up_screen():
  screen.blit(pygame.image.load('start_up.JPG'), (0, 0))
  new_game_button.draw(screen)
  resume_button.draw(screen)
  options_button.draw(screen)
  quit_button.draw(screen)
# Main game loop
running = True
while running:
    draw_start_up_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if new_game_button.rect.collidepoint(mouse_pos):
                       pass
            elif resume_button.rect.collidepoint(mouse_pos):
                     pass
            elif options_button.rect.collidepoint(mouse_pos):
              quit_button
            elif resume_button.rect.collidepoint(mouse_pos):
              pass
                     
                     
    pygame.display.flip()

pygame.quit()
