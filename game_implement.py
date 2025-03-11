import pygame
import random
from c_s import *
from variables import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tiny Choices")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
header_rect = pygame.Rect(0, 0, 800, 50)
stats_rect = pygame.Rect(0, 0, 400, 50)
choice_rect = pygame.Rect(400, 250, 420, 230)
history_rect = pygame.Rect(0, 50, 400, 350)
options_rect = pygame.Rect(0, 400, 400, 200)
settings_rect = pygame.Rect(400, 500, 400, 100)
blank_rect = pygame.Rect(400, 50, 400, 550)

#start up buttons 
new_game_button=Button(pygame.image.load('new_game.PNG').convert_alpha(),400,305,1)
resume_button=Button(pygame.image.load('resume.PNG').convert_alpha(),400,380,1)
options_button=Button(pygame.image.load('settings.PNG').convert_alpha(),405,450,1)
quit_button=Button(pygame.image.load('quit.PNG').convert_alpha(),400,530,1)

#Game property buttons
buy_button = pygame.Rect(400, 400, 300, 50)
mortgage_button = pygame.Rect(400, 500, 300, 50)
property_buttons = [pygame.Rect(20, 80 + (i * 50), 300, 40) for i in range(len(Game.properties))]

#player property buttons
player_property_buttons = [pygame.Rect(20, 80 + (i * 50), 300, 40) for i in range(len(Game.player.properties))]
sell_button = pygame.Rect(400, 300, 300, 50)

#game npc buttons
ask_to_be_friends_button = pygame.Rect(500, 400, 200, 50)
ask_to_date_button = pygame.Rect(500, 300, 200, 50)
npc_buttons = [pygame.Rect(20, 80 + (i * 50), 300, 40) for i in range(len(Game.npcs))]


#player relationship buttons
conversate_button = pygame.Rect(500, 400, 200, 50)
make_new_relationships_button = pygame.Rect(500, 200, 200, 50)
start_fight_button = pygame.Rect(500, 500, 200, 50)
ask_for_money_button = pygame.Rect(500, 300, 200, 50)
relationship_buttons = [pygame.Rect(20, 80 + (i * 50), 300, 40) for i in range(len(Game.player.relationships))]

back_button=Button(pygame.image.load('back.PNG').convert_alpha(),0,0,0.13)

#main screen buttons
choice_buttons = [
pygame.Rect(420, 310, 360, 40),
pygame.Rect(420, 360, 360, 40),
pygame.Rect(420, 410, 360, 40)]
age_up_button = Button(pygame.image.load('age_up.png').convert_alpha(),140,395,0.27)
school_button = Button(pygame.image.load('school.png').convert_alpha(),10,450,0.3)
property_button = Button(pygame.image.load('property.png').convert_alpha(),140,495,0.27)
relationships_button = Button(pygame.image.load('relationships.png').convert_alpha(),250,450,0.3)

choices =show_choices_and_option(check_available_choices(player))

selected_job = None
selected_player_property= None
selected_relationship = None
selected_npc = None
selected_property = None

def draw_progress_bar(x, y, value, max_value, width=200, height=20):
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)  # Border
    fill_width = (value / max_value) * (width - 4)  # Fill width based on value
    pygame.draw.rect(screen, Game.colour_2, (x + 2, y + 2, fill_width, height - 4))

def draw_start_up_screen():
  screen.blit(pygame.image.load('start_up.JPG'), (0, 0))
  new_game_button.draw(screen)
  resume_button.draw(screen)
  options_button.draw(screen)
  quit_button.draw(screen)
    
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
        
def draw_potential_relationships_screen():
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
        display_potential_relationships(selected_npc)
def draw_relationships_screen():
    screen.fill(WHITE)

    pygame.draw.rect(screen, Game.colour_1, header_rect)
    back_button.draw(screen)

    i=0
    for npc in npc_buttons:
        pygame.draw.rect(screen, Game.colour_1, npc)
        screen.blit(Game.fonts[0].render(f"{Game.player.relationships[i].name} {Game.player.relationships[i].surname} ", True, BLACK), (npc.x + 10, npc.y + 10))
        i+=1
    pygame.draw.rect(screen, Game.colour_1, make_new_relationships_button)
    screen.blit(Game.fonts[0].render("Make New Friends", True, WHITE), (make_new_relationships_button.x+10, make_new_relationships_button.y + 15))
    # Display stats if an NPC is selected
    if selected_npc is not None:
        display_relationships(selected_npc)

def draw_potential_properties_screen():
    screen.fill(WHITE)

    pygame.draw.rect(screen, Game.colour_1, header_rect)
    back_button.draw(screen)

    i=0
    for property in property_buttons:
        pygame.draw.rect(screen, Game.colour_1, property)
        screen.blit(Game.fonts[0].render(f"{Game.properties[i].type}  ", True, BLACK), (property.x + 10, property.y + 10))
        i+=1

    
    if selected_property is not None:
        display_potential_properties(selected_property)

def draw_potential_jobs_screen():
    screen.fill(WHITE)

    pygame.draw.rect(screen, Game.colour_1, header_rect)
    back_button.draw(screen)

    i=0
    for job in job_buttons:
        pygame.draw.rect(screen, Game.colour_1, job)
        screen.blit(Game.fonts[0].render(f"{Game.jobs[i].title}  ", True, BLACK), (job.x + 10, job.y + 10))
        i+=1

    
    
    # Display stats if an NPC is selected
    if selected_property is not None:
        display_potential_jobs(selected_property)
        
def display_relationships(npc)
    pygame.draw.rect(screen, WHITE, blank_rect)
    screen.blit(Game.fonts[0].render(f"{npc.name}'s Stats", True, BLACK), (550, 20))
    screen.blit(Game.fonts[1].render(f"Age: {npc.age}", True, BLACK), (440, 120))
    draw_progress_bar(440, 150, npc.health, 100)
    screen.blit(Game.fonts[1].render("Health", True, BLACK), (655, 150))
    draw_progress_bar(440, 180, npc.relationship_level, 100)
    screen.blit(Game.fonts[1].render("Relationship", True, BLACK), (655, 180))
    screen.blit(Game.fonts[1].render("Money", True, BLACK), (655, 210))
    draw_progress_bar(440, 210, npc.money/100, 100)
    pygame.draw.rect(screen, Game.colour_1, conversate_button)
    screen.blit(Game.fonts[0].render("Have a chat", True, WHITE), (conversate_button.x+10, conversate_button.y + 15))
    pygame.draw.rect(screen, Game.colour_1, ask_for_money_button)
    screen.blit(Game.fonts[0].render("Ask for money", True, WHITE), (ask_for_money_button.x + 10, ask_for_money_button.y + 15))
    if npc.relationship_type == 'Sibling':
      pygame.draw.rect(screen, Game.colour_1, start_fight_button)
      screen.blit(Game.fonts[0].render("Start a fight", True, WHITE), (start_fight_button.x + 10, start_fight_button.y + 15))
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
    elif current_screen == 'job':
        draw_job_screen()
    elif current_screen == "potential relationships":
        draw_potential_relationships_screen()
    elif current_screen == "potential properties":
        draw_potential_properties_screen()
    elif current_screen == 'potential jobs':
        draw_potential_job_screen()
    elif current_screen == "school":
        draw_school_screen()
    elif current_screen == "start up":
        draw_start_up_screen()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if current_screen == "main":
                draw_main_screen()
                if age_up_button.rect.collidepoint(mouse_pos):
                    Game.player.age += 1
                    Game.history.append(f"Age {Game.player.age}: {choices[0]}")
                    Game.history.append('')
                    choices =show_choices_and_option(check_available_choices(Game.player))
                elif choice_buttons[0].collidepoint(mouse_pos):
                    player.choice_results('a',choices)    
                elif choice_buttons[1].collidepoint(mouse_pos):
                    player.choice_results('b',choices)
                elif choice_buttons[2].collidepoint(mouse_pos):
                    player.choice_results('c',choices)
                elif property_button.rect.collidepoint(mouse_pos):
                    current_screen = "properties"  # Switch to properties screen
                elif relationships_button.rect.collidepoint(mouse_pos):
                    current_screen = "relationships"  # Switch to relationships screen
                elif school_button.rect.collidepoint(mouse_pos):
                    current_screen = "school"  # Switch to relationships screen
                elif settings_rect.collidepoint(mouse_pos):
                    current_screen = "settings"
                    
            elif current_screen in ["relationships",'potential properties' ,"properties",'school',"potential relationships",'settings','work','job', "potential jobs"]:
                if back_button.rect.collidepoint(mouse_pos):
                    current_screen = "main"  # Go back to the main screen

            
            elif current_screen == 'start up':
                if new_game.rect.collidepoint(mouse_pos):
                    current_screen = "main"  # Switch to properties screen
            

            
            elif  current_screen == "relationships":
                for i,btn in enumerate(relationship_buttons):
                    if btn.collidepoint(mouse_pos):
                        selected_relationship = Game.player.relationships[i]
                        break
                    if selected_relationship is not None:
                        if ask_for_money_button.collidepoint(mouse_pos):
                            selected_relationship.ask_for_money()    
                            Game.actions+=1                   
                        if conversate_button.collidepoint(mouse_pos):
                            selected_relationship.have_conversation()
                            Game.actions+=1 
                        if start_fight_button.collidepoint(mouse_pos):
                            selected_relationship.start_fight()    
                            Game.actions+=1 
                   elif make_new_relationships_button.collidepoint(mouse_pos):
                       current_screen = "potential relationships"
                       
            elif current_screen == 'potential relationships':
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

            elif current_screen == 'potential jobs':
                 for i,btn in enumerate(job_buttons):
                    if btn.collidepoint(mouse_pos):
                        selected_job = Game.jobs[i]
                        break
                    if selected_job is not None:
                        if button.collidepoint(mouse_pos):
                            selected_job.apply(Game.player) 


    pygame.display.flip()


pygame.quit()


