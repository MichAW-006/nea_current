import pygame
import random
from c_s import *
from variables import *
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tiny Choices")
Game = game()
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
age_up_button = Button(pygame.image.load('age_up.PNG').convert_alpha(),140,395,0.27)
school_button = Button(pygame.image.load('school.PNG').convert_alpha(),10,450,0.3)
property_button = Button(pygame.image.load('property.PNG').convert_alpha(),140,495,0.27)
relationships_button = Button(pygame.image.load('relationships.PNG').convert_alpha(),250,450,0.3)

selected_job = None
selected_player_property= None
selected_relationship = None
selected_npc = None
selected_property = None

choices =show_choices_and_option(check_available_choices(Game.player))
make_choice = True
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
    global selected_job
    global selected_player_property
    global selected_relationship
    global selected_npc
    global selected_property
    selected_job = None
    selected_player_property= None
    selected_relationship = None
    selected_npc = None
    selected_property = None

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
    for event_text in Game.history[-10:]:
        screen.blit(render_text_list(wrap_text(event_text,Game.fonts[1],400),Game.fonts[1],BLACK), (10, y_offset))
        y_offset += 20
        
def draw_relationships_screen():
    screen.fill(WHITE)

    pygame.draw.rect(screen, Game.colour_1, header_rect)
    back_button.draw(screen)

    i=0
    for npc in relationship_buttons:
        pygame.draw.rect(screen, Game.colour_1, npc)
        screen.blit(Game.fonts[0].render(f"{Game.player.relationships[i].name} {Game.player.relationships[i].surname} ", True, BLACK), (npc.x + 10, npc.y + 10))
        i+=1
    pygame.draw.rect(screen, Game.colour_1, make_new_relationships_button)
    screen.blit(Game.fonts[0].render("Make New Friends", True, WHITE), (make_new_relationships_button.x+10, make_new_relationships_button.y + 15))
    # Display stats if an NPC is selected
    if selected_relationship is not None:
        display_relationships(selected_relationship)

def display_relationships(npc):
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
        
def display_potential_relationships(npc):
    screen.blit(Game.fonts[0].render(f"{npc.name}'s Stats", True, BLACK), (550, 20))
    screen.blit(Game.fonts[1].render(f"Age: {npc.age}", True, BLACK), (440, 120))
    draw_progress_bar(440, 150, npc.health, 100)
    screen.blit(Game.fonts[1].render("Health", True, BLACK), (655, 150))
    screen.blit(Game.fonts[1].render("Money", True, BLACK), (655, 180))
    draw_progress_bar(440, 180, npc.money/100, 100)
    pygame.draw.rect(screen, Game.colour_1, ask_to_be_friends_button)
    screen.blit(Game.fonts[0].render("Offer to be friends", True, WHITE), (ask_to_be_friends_button.x+10, ask_to_be_friends_button.y + 15))
    pygame.draw.rect(screen, Game.colour_1, ask_to_date_button)
    screen.blit(Game.fonts[0].render("Ask to date", True, WHITE), (ask_to_date_button.x + 10, ask_to_date_button.y + 15))


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
    # Buy button
    buy_button = pygame.Rect(x + 10, y + height - 40, width - 20, 25)
    mortgage_button = pygame.Rect(x + 10, y + height - 70, width - 20, 25)
    pygame.draw.rect(screen, Game.colour_1, buy_button, border_radius=5)
    pygame.draw.rect(screen, Game.colour_1, mortgage_button, border_radius=5)
    buy_text = Game.fonts[2].render("Buy with cash", True, WHITE)
    mort_text = Game.fonts[2].render("Apply for mortgage", True, WHITE)
    screen.blit(buy_text, (x + 20, y + height - 35))
    screen.blit(mort_text, (x + 20, y + height - 65))


    return card_rect,buy_button,mortgage_button

def draw_potential_properties_screen():
    
    screen.fill(WHITE)
    
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

    for i, property in enumerate(Game.properties):
        row = i // properties_per_row
        col = i % properties_per_row
        x = 50 + col * (card_width + margin)
        y = 100 + row * (card_height + margin)
        card_rect,buy_button,mortgage_button = draw_property_card(x, y, card_width, card_height, property)

        # Handle buy button clicks
        mouse_pos = pygame.mouse.get_pos()
        if buy_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]: # Left mouse button
                property.buy(Game.player,False)
                return True
                
        elif mortgage_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                property.buy(Game.player,True)
                return True
        
                
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
        

  
current_screen = "start up" 
# Game loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen

    # Draw the appropriate screen based on game state
    if current_screen == "main":
        Game.history=check_history(Game.history)
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
                    Game.history.append(f"Age {Game.player.age-1}: {choices[0]}")
                    Game.history.append('')
                    aging_cycle(Game.player)
                    make_choice = True
                    choices =show_choices_and_option(check_available_choices(Game.player))
                elif choice_buttons[0].collidepoint(mouse_pos) and make_choice == True:
                    Game.player.choice_results('a',choices) 
                    make_choice = False
                elif choice_buttons[1].collidepoint(mouse_pos) and make_choice == True:
                    Game.player.choice_results('b',choices)
                    make_choice = False
                elif choice_buttons[2].collidepoint(mouse_pos)and make_choice == True:
                    Game.player.choice_results('c',choices)
                    make_choice = False
                elif property_button.rect.collidepoint(mouse_pos):
                    current_screen = "potential properties"  # Switch to properties screen
                elif relationships_button.rect.collidepoint(mouse_pos):
                    current_screen = "relationships"  # Switch to relationships screen
                elif school_button.rect.collidepoint(mouse_pos):
                    current_screen = "school"  # Switch to relationships screen
                elif settings_rect.collidepoint(mouse_pos):
                    current_screen = "settings"
                    
            
            
            elif current_screen == 'start up':
                if new_game_button.rect.collidepoint(mouse_pos):
                    current_screen = "main"  # Switch to properties screen
            
            elif current_screen == 'potential properties':
                if draw_potential_properties_screen() is True:
                   current_screen = "main"
            elif current_screen == "relationships":
              
              if back_button.rect.collidepoint(mouse_pos):
                current_screen = "main"
              for i,btn in enumerate(relationship_buttons):
                if btn.collidepoint(mouse_pos):
                  selected_relationship = Game.player.relationships[i]
                  break
                if selected_relationship is not None:
                  if ask_for_money_button.collidepoint(mouse_pos):
                    response = selected_relationship.ask_for_money(Game.player)
                    Game.history.append(response)
                    current_screen = "main"
                  if conversate_button.collidepoint(mouse_pos):
                    response = selected_relationship.have_conversation(Game.player)
                    Game.history.append(response)
                    current_screen = "main"
                  if start_fight_button.collidepoint(mouse_pos):
                    Game.history.append(selected_relationship.start_fight(Game.player) )  
                    Game.history.append('')
                    current_screen = "main"
              if make_new_relationships_button.collidepoint(mouse_pos):
                current_screen = "potential relationships"
        
            elif current_screen == "potential relationships":
              if back_button.rect.collidepoint(mouse_pos):
                current_screen = "relationships"
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


            elif current_screen in ["relationships","properties",'school','work','job']:
                if back_button.rect.collidepoint(mouse_pos):
                    current_screen = "main"  # Go back to the main screen



    pygame.display.flip()


pygame.quit()
