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

#main screen buttons
choice_buttons = [
pygame.Rect(420, 310, 360, 40),
pygame.Rect(420, 360, 360, 40),
pygame.Rect(420, 410, 360, 40)]
age_up_button = Button(pygame.image.load('age_up.PNG').convert_alpha(),140,395,0.27)
school_button = Button(pygame.image.load('school.PNG').convert_alpha(),10,450,0.3)
property_button = Button(pygame.image.load('property.PNG').convert_alpha(),140,495,0.27)
relationships_button = Button(pygame.image.load('relationships.PNG').convert_alpha(),250,450,0.3)

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

#player relationship with npcs buttons
conversate_button = pygame.Rect(500, 400, 200, 50)
make_new_relationships_button = pygame.Rect(500, 200, 200, 50)
start_fight_button = pygame.Rect(500, 500, 200, 50)
ask_for_money_button = pygame.Rect(500, 300, 200, 50)
relationship_buttons = [pygame.Rect(20, 80 + (i * 50), 300, 40) for i in range(len(Game.player.relationships))]

#school buttons 
join_club_button = pygame.Rect(500, 200, 200, 50)
study_harder_button = pygame.Rect(500, 300, 200, 50)
bunk_class_button = pygame.Rect(500, 400, 200, 50)




back_button=Button(pygame.image.load('back.PNG').convert_alpha(),0,0,0.13)

selected_job = None
selected_player_property= None
selected_property = None
selected_relationship = None
selected_npc = None
show_clubs= None
selected_club = None

make_choice = True

