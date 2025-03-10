import pygame
import random
import math
from variables import *

class Main_Character():
  
  def __init__(self):
    set_values(self)
    country_city = random_choice(Countries)
    self.country = country_city[0]
    self.city = country_city[1]
    self.age = 0                #age is automatically set to 0
    self.health = random.randint(40,100) # attributes are set randomly
    self.mood = 100
    self.money = 0
    self.intelligence=random.randint(0,100)
    self.life = True
    self.school_behaviour = 100
    self.grades = round(self.intelligence/0.85)
    self.attendance = 100
    self.experience=0
    self.properties =[]
    
class Npc():
  
  def __init__(self,player):
    set_values(self)
    self.country = player.country
    self.city = player.city
    self.age = random.randint(5,75)
    self.health = random.randint(0,100)
    self.relationship_level = random.randint(0,100)
    self.life = True
    self.relationship_level = 10
    self.money = random.randint(100,10000)
    
  def have_conversation(self):
    conversation= random_choice(conversation_topics)
    self.relationship_level += random.randint(-10,10)
    self.change_relationship()
    return f'You and {self.name} had a conversation about {conversation[0]}'
  
  def check_health(self):
    health_check(self)
 
  def age_up(self):
    self.age+=1
    self.health = round(self.health*(random.uniform(0.6,1.4))) 
    money += random.randint(100,10000)
    self.check_health()
  
  def ask_for_money(self):
    if self.relationship_level >60:
      money = random.randint(1,1000)
      self.money -= money
      self.relationship_level += random.randint(-10,1)
      random_comment = 'insert comment here'
      self.change_relationship()
      return money,random_comment
    else:
      self.relationship_level += random.randint(-30,1)
      self.change_relationship()
      return 0, 'stop asking'
      
  def change_relationship(self):
    self.relationship_level=check_values (self.relationship_level,100,0)
    
  

class Parent(Npc):
  def __init__(self,player):
    super().__init__(player)
    self.surname = player.surname
    self.age = random.randint(17,75)
    self.health = random.randint(0,100)
    self.relationship_level = random.randint(0,100)
    if self.gender == 'male':
      self.realtionship_type_main = 'Father'
    else:
      self.realtionship_type_main = 'Mother'
      
class Sibling(Npc):
  def __init__(self,player,max_age):
    super().__init__(player)
    self.surname = player.surname
    self.age = random.randint(0,max_age)
    self.relationship_level = random.randint(0,100)
    self.realtionship_type_main = 'Sibling'



class Job():
  
  def __init__(self):
    self.salary = 26000 #default salary for someone starting level in a job without a degree
    self.skill_required = 0
    self.experience_required = 20
    create_job(self,'')
    if self.education[0] != 'None':
      self.salary = random.randint(35000,40000)# sets random salary of the job
      self.skill_required = random.randint(20,60)
        
  def promote(self,player):
    
    if self.work_ethic>60:
      if 'Junior' or 'Apprentice' in self.title:
        self.salary += random.randint(1000,9000)
        player.experience+=20
        self.work_life_balance = random.randint(1,10)
        self.title=self.title.replace('Junior ','')
        self.title=self.title.replace('Apprentice ','')
      elif 'Senior' or 'Expert' in self.title:
        self.salary += random.randint(5000,13000)
      else :
        self.salary += random.randint(1000,20000)
        self.work_life_balance = random.randint(1,10)
        player.experience+=40
        self.title='Senior ' + self.title
        if self.education[0]=='None':
          self.title='Expert ' + self.title

  def work(self,player):
    self.work_ethic+=random.randint(1,7)
    player.mood += random.randint(-10,5)
    player.intelligence += random.randint(-5,5)
    player.health+= self.work_life_balance*random.randint(-5,0)
  
  def check_maxxed(self):
    if self.work_ethic>100:
      self.work_ethic = 100

class Junior_Job(Job):
  def __init__(self):
    super().__init__()
    self.salary = 13000 #default salary for someone starting level in a job without a degree
    self.skill_required = 0
    self.experience_required = 0
    create_job(self,'Junior')
    if self.education[0] != 'None':
      self.salary = random.randint(24000,29000)# sets random salary of the job
      self.skill_required = random.randint(0,40)
      
      
class Senior_Job(Job):
  def __init__(self):
    super().__init__()
    starting_salary = 35000 #default salary for someone starting level in a job without a degree
    self.skill_required = 0
    self.experience_required = 40
    create_job(self,'')
    if self.education[0] != 'None':
      self.salary = random.randint(55000,80000)# sets random salary of the job
      self.skill_required = random.randint(60,80)


class Property():
  def __init__(self):
    random_value= random.choice(list(property_names.items()))
    x= random_value[0]
    self.condition = random.randint(0,100)
    self.price =round(15850000 * (0.6309 ** x) + self.condition, 2 - len(str(int(15850000 * (0.6309 ** x)))))
    self.type = random_value[1]
    self.location = str(random.randint(1,270))+' '+random_choice(street_names)+' '+random_choice(location_names)
    self.price_paid = 0
    self.years_left =25
    self.strikes = 3

  def buy(self,mortgage,player):
    if mortgage is True: 
      if player.money >= (self.price/10):
        self.price_paid=player.money-(self.price/10)
        return True
      else:
        return False
    elif mortgage is False :
      if player.money >= self.price:
        self.price_paid = self.price
        return True 
      else:
        return False
        
  def sell(self,player):
    player.money += self.price_paid
    
  def pay_mortagage(self,player):
    self.years_left += -1
    left_to_pay =self.price-self.price_paid
    if player.money >= (left_to_pay)/25:
      self.price_paid +=(left_to_pay)/25
      return left_to_pay/25
    else:
      self.strikes+=-1
  def check_if_defaulted(self):
    if self.strikes == 0:
      pass
      

class School:
  def __init__(self,dict):
    self.attendance = 100
    self.behaviour = 100
    self.grades = 100
    self.name = random_choice(school_prefixes)+' '+random_choice(dict)
      
  def change_attendance(self,player):
    if player.health < 70:
      self.attendance += -random.randint(0,5)*(70/player.health)
      player.mood += random.randint(-20,0)
      
  def change_behaviour(self, player):
    self.behaviour +=random.randint(-20,0)
    self.grades += random.randint(-20,0)
    player.mood += random.randint(-20,0)
    
  def study(self,player):
    self.grades += random.randint(0,8)
    player.intelligence += random.randint(1,7)


class game():
  def __init__(self):
    self.player= Main_Character()
    self.running = True
    self.colour_1 = (105,146,248) 
    self.colour_2 = (77,238,125) 
    self.colour_3 = (245,179,234)
    self.fonts= [pygame.font.Font(None, 30), pygame.font.Font(None, 24),pygame.font.Font(None, 18)]
    self.jobs = generate_jobList()
    self.properties = generate_propertiesList()
    self.npcs=generate_starting_npcs(self.player)
    self.actions = 0
    self.history = []
  
  def Change_Colour_Style_1(self,new_colour):
    self.colour_1=sort_and_change(new_colour)
    
  def Change_Colour_Style_2(self,new_colour):
    self.colour_2=sort_and_change(new_colour)
    
  def Change_Colour_Style_3(self,new_colour):
    self.colour_3=sort_and_change(new_colour)
  def new_objects(self):
    self.jobs = generate_jobList()
    self.properties = generate_propertiesList()
    self.npcs=remove_dead_npc(self.npcs)

class Button():
    def __init__(self,image,x,y,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

#---------------------------------------





def create_job(self,Type):
  random_job = random_choice(Jobs_Dict)
  self.title=Type + ' ' + random_job[0]
  self.education = random_job[1:len(random_job)]# sets the education required for the job
  self.work_ethic = 100
  self.work_life_balance = random.randint(1,10)
  if self.education[0] == 'None' and Type == 'Junior':
    self.title='Apprentice' + ' ' + random_job[0]
  elif self.education[0] == 'None' and Type == 'Senior':
    self.title='Expert' + ' ' + random_job[0]
def generate_propertiesList():
  list = []
  for i in range(0,9):
    list.append(Property())
  return(list)
def generate_jobList():
  list = []
  for i in range(0,2):
    list.append(Job())
    list.append(Junior_Job())
    list.append(Senior_Job())
  return(list)

def generate_schools():
  return [School(primary_school_names),School(secondary_school_names),School(univeristy_names)]

#game subprograms
def sort_and_change(colour):
    for x,y in colours:
        if colour == x:
          return y
        
#choice subprograms
def check_available_choices(P):
  if P.age >=55:
    return elder_choices
  elif P.age >=30:
    return adult_choices
  elif P.age >=19:
    return young_adult_choices
  elif P.age >=12:
      return teen_choices
  elif P.age >=4:
    return child_choices
  else:
    return baby_choices



def random_choice(d):
    random_value= random.choice(list(d.items()))
    return random_value[1]
def random_choices_for_game(d):
    random_value= random.choice(list(d.items()))
    return random_value[1]
def show_choices_and_option(choice_dict):
  choice = random_choices_for_game(choice_dict)
  return([choice[0],choice[1],choice[2],choice[3],choice[4][0][0],choice[4][1][0],choice[4][2][0],choice[4][0][1],choice[4][1][1],choice[4][2][1],choice[4][0][2],choice[4][1][2],choice[4][2][2]])
  
  
#character subprograms
def set_values(self):
  isFemale = bool(random.getrandbits(1)) # randomly generates the gender of the character
  
  if isFemale is True:
    self.name = random_choice(female_names)
  
  elif not isFemale :
    self.name = random_choice(male_names)
          
  self.surname =  random_choice(last_names)
def check_values(value,maxival,minival):
  if value > maxival:
    return maxival
  elif value < minival:
    return minival
  else:
    return value
def remove_dead_npc(npc_list,player):
  for npc in npc_list:
    if npc.check_health() is False:
      npc_list.remove(npc)
      generate_new_npc(player,npc_list)
            
def increment_npcs(npc_list,player):
  for npc in npc_list:
    npc.age+=1
    npc.health=round(npc.health*(random.uniform(0.6,1.4)))
    remove_dead_npc(npc_list,player)
    
def aging_cycle(player):
   if player.age>38:
      player.health=round(player.health*(random.uniform(0.73,1)))
     
#game implementation subprograms

def generate_starting_npcs(player):
    npc_list=[Npc(player),Npc(player),Npc(player),Npc(player),Npc(player),Npc(player),Npc(player),Npc(player),Npc(player)]
      
    return npc_list
    
      
def generate_new_npc(player,npc_list):
  return(npc_list.append(Npc(player)))

def generate_sibling(player,parent1,parent2,npc_list):
    if parent1.age+parent2.age<75 and random.randint(1,9)==3:
        npc_list.append(Sibling(player,0))


def health_check(self):
  if self.health< 5:
    self.life = False






#found on github
def wrap_text(text, font, width):
    text_lines = text.replace('\t', '    ').split('\n')
    if width is None or width == 0:
        return text_lines

    wrapped_lines = []
    for line in text_lines:
        line = line.rstrip() + ' '
        if line == ' ':
            wrapped_lines.append(line)
            continue

        # Get the leftmost space ignoring leading whitespace
        start = len(line) - len(line.lstrip())
        start = line.index(' ', start)
        while start + 1 < len(line):
            # Get the next potential splitting point
            next = line.index(' ', start + 1)
            if font.size(line[:next])[0] <= width:
                start = next
            else:
                wrapped_lines.append(line[:start])
                line = line[start+1:]
                start = line.index(' ')
        line = line[:-1]
        if line:
            wrapped_lines.append(line)
    return wrapped_lines


def render_text_list(lines, font, colour=(255, 255, 255)):
    rendered = [font.render(line, True, colour).convert_alpha()
                for line in lines]

    line_height = font.get_linesize()
    width = max(line.get_width() for line in rendered)
    tops = [int(round(i * line_height)) for i in range(len(rendered))]
    height = tops[-1] + font.get_height()

    surface = pygame.Surface((width, height)).convert_alpha()
    surface.fill((0, 0, 0, 0))
    for y, line in zip(tops, rendered):
        surface.blit(line, (0, y))

    return surface
#..........................................
