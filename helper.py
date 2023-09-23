'''
Objects on screen
'''

import pygame, random, time

# Colour codes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
houseColour = (225, 206, 96)
roofColour = (171, 2, 227)
doorColour = (166, 165, 162)
windowColour = (242, 235, 149)

# Welcome Screen
background = pygame.image.load("Data/Game background.png")
# Reference for similar background image: https://www.wallpapertip.com/wpic/hwwxoo_blue-illustrated-landscape-mountains-wallpaper-mural-mountain/
backgroundText = pygame.image.load("Data/Welcome page text.png")
start = pygame.image.load("Data/Game play button.png")
about = pygame.image.load("Data/Game play button 2.png")
gameAbout = pygame.image.load("Data/Game about text.png")
gameComplete = pygame.image.load("Data/Game complete text.png")
gameControls = pygame.image.load("Data/Game controls text.PNG")

def homepage(screen, font5):
  gameVersion = font5.render("Demo game assignment v1.0", True, WHITE)
  screen.blit(background, (0, 0))
  screen.blit(backgroundText, (78, 30))
  screen.blit(start, (213, 150))
  screen.blit(about, (201, 198))
  screen.blit(gameVersion, (353, 387))

# About page
def aboutPage(screen, font5):
  gameVersion = font5.render("Demo game assignment v1.0", True, WHITE)
  screen.blit(background, (0, 0))
  screen.blit(gameAbout, (102, 15))
  screen.blit(gameControls, (25, 70))
  screen.blit(gameVersion, (353, 387))

# Game end page
def gameEnd(screen, font3, font4, font5):
  gameText = font3.render("Thank you for playing the demo game!", True, (139, 28, 199))
  gameText2 = font4.render("Secret Achievement Accquired: Total jumps should equal to 10", True, (139, 28, 199))
  gameText3 = font4.render("Press ESC key to go back to main screen", True, (139, 28, 199))
  gameVersion = font5.render("Demo game assignment v1.0", True, WHITE)
  screen.blit(background, (0, 0))
  screen.blit(gameComplete, (28, 45))
  screen.blit(gameText, (66, 130))
  screen.blit(gameText2, (46, 163))
  screen.blit(gameText3, (120, 190))
  screen.blit(gameVersion, (353, 387))

# Car
def drawCar(screen):
  pygame.draw.rect(screen, RED, (70, 296, 130, 60))
  pygame.draw.rect(screen, BLACK, (71, 296, 130, 60), 1)
  pygame.draw.rect(screen, WHITE, (70, 296, 10, 8))
  pygame.draw.rect(screen, (237, 208, 19), (135, 256, 60, 50))
  pygame.draw.rect(screen, BLACK, (135, 255, 61, 51), 1)
  pygame.draw.circle(screen, BLACK, (95, 356), 15)
  pygame.draw.circle(screen, BLACK, (177, 356), 15)

# Snow fall
def snowfall(screen):
  for i in range(50):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    snow = random.randint(1, 5)
    pygame.time.delay(1)
    pygame.draw.circle(screen, WHITE, [x, y], snow)

# House
def drawHouse(screen):
  pygame.draw.rect(screen, houseColour, (310, 200, 190, 140))
  pygame.draw.rect(screen, BLACK, (310, 200, 191, 141), 1)
  
  # Roof 
  pygame.draw.polygon(screen, roofColour, [(290, 220), (360, 142), (500, 142), (500, 220)]) 
  pygame.draw.polygon(screen, BLACK, [(290, 220), (360, 142), (500, 142), (500, 220)], 1)
  
  # Door
  pygame.draw.rect(screen, doorColour, (330, 250, 48, 80))
  pygame.draw.rect(screen, BLACK, (329, 249, 48, 82), 1)
  pygame.draw.circle(screen, BLACK, (367, 295), 4)
  
  # Window
  pygame.draw.rect(screen, windowColour, (416, 251, 40, 40)) 
  pygame.draw.polygon(screen, BLACK, [(415, 250), (455, 250), (455, 290), (415, 290)], 1)
  pygame.draw.line(screen, BLACK, (435, 250), (435, 290), 1)
  pygame.draw.line(screen, BLACK, (415, 270), (455, 270), 1)


