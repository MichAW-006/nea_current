import pygame
new_game_button=Button(pygame.image.load('new_game.PNG').convert_alpha(),50,50,1)
resume_button=Button(pygame.image.load('resume.PNG').convert_alpha(),80,80,1)
options_button=Button(pygame.image.load('settings.PNG').convert_alpha(),200,200,1)
quit_button=Button(pygame.image.load('quit.PNG').convert_alpha(),300,300,1)
start_up_button=Button(pygame.image.load('start_up.JPG').convert_alpha(),0,0,1)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Life Simulator")
def draw_start_up_screen():
  start_up_button.draw(screen)
  new_game_button.draw(screen)
  resume_button.draw(screen)
  options_button.draw(screen)
  quit_button.draw(screen)
  
  
running = True
while running:
    screen.fill(WHITE)  
    draw_start_up_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
  

    pygame.display.flip()

pygame.quit()
    
