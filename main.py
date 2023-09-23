'''
Programmer: Shreyas Rao
April 20, 2021
Description: Using pygame to draw shapes and integrate graphics
'''

import pygame, helper, time

# Initializes pygame
pygame.init()

clock = pygame.time.Clock()

# Colour codes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Screen dimension
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

# Sets the display screen
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen = pygame.display.get_surface()

# Sets the title of the display screen
pygame.display.set_caption("Game Window")

# Welcome text
font1 = pygame.font.SysFont("Times New Roman", 28)
welcomeText = font1.render("Winter Season", True, (139, 28, 199))
welcomeText_width = welcomeText.get_width()
welcomeText_height = welcomeText.get_height()
welcomeText_x = (SCREEN_WIDTH-welcomeText_width)//2
welcomeText_y = 0

# Time in seconds
timer = 50
# Jump count and text display on screen
jumpCount = 0
font2 = pygame.font.SysFont("Times New Roman", 18)

# Game complete text
font3 = pygame.font.SysFont("Comic Sans", 30)
font4 = pygame.font.SysFont("Times New Roman", 16)
# Font for home screen
font5 = pygame.font.SysFont("Comic Sans", 15)

# Sets the location of rectangle and circle
rect_x = 220 # x value of starting position of (rectangle) character
rect_y = 300 # y value of starting position of (rectangle) character

center_x = 70   # x value of center of circle (sun)
center_y = 350  # y value of center of circle (sun)

# Speed and movement of rectangle
rect_change_x = 0
rect_jump = 8

# Sets the game loop
running = True
jump = False # movement control loop
intro = False # loop for text animation in game loop

background = (3, 232, 252) # light blue colour
CURRENT_SCREEN = "homepage" # Sets the variable to homepage to have separate functioning pages in the navigation menu 


# MAIN PROGRAM ########################################
while running:

  # variable for key pressed by user and mouse input
  keys = pygame.key.get_pressed()
  mousePosition = pygame.mouse.get_pos()
  mouseButton = pygame.mouse.get_pressed()
  mouseX = mousePosition[0]
  mouseY = mousePosition[1]
  
  # Condition if statements to control navigation in game program
  if CURRENT_SCREEN == "homepage":
    helper.homepage(screen, font5)
  elif CURRENT_SCREEN == "about":
    helper.aboutPage(screen, font5)
  elif CURRENT_SCREEN == "game end":
    helper.gameEnd(screen, font3, font4, font5)
  elif CURRENT_SCREEN == "start":
      # Counts the number of jumps
      if jumpCount == 10:
        CURRENT_SCREEN = "game end"
      
      timer -= 0.5
      #Sets the background colour of the display screen
      screen.fill(background) # light blue colour
      
      # Displays the jump count of the character on screen
      if jumpCount > 4:
        if background == (19, 2, 46): # night sky
          jumpCount_text = font2.render("Total jumps: ??", True, WHITE)
          screen.blit(jumpCount_text, (380, 4))
        else:
          jumpCount_text = font2.render("Total jumps: ??", True, BLACK)
          screen.blit(jumpCount_text, (380, 4))
      else:
        if background == (19, 2, 46): # night sky
          jumpCount_text = font2.render("Total jumps: "+str(jumpCount), True, WHITE)
          screen.blit(jumpCount_text, (380, 4))
        else:
          jumpCount_text = font2.render("Total jumps: "+str(jumpCount), True, BLACK)
          screen.blit(jumpCount_text, (380, 4))


      # Welcome display
      if intro == False:
        screen.blit(welcomeText, (welcomeText_x, welcomeText_y))
        if welcomeText_y < 50:
          welcomeText_y += 2
        else:
          screen.blit(welcomeText, (welcomeText_x, welcomeText_y))       
          # gets the time in milliseconds
          if timer <= 0:
            intro = True

      # Movement control
      rect_x += rect_change_x
      if jump == False:
        if keys[pygame.K_LEFT] and rect_x >= 0 and CURRENT_SCREEN == "start":
          rect_change_x = -6
        elif keys[pygame.K_RIGHT] and rect_x <= 500 and CURRENT_SCREEN == "start":
          rect_change_x = 6
        else:
          rect_change_x = 0
        if keys[pygame.K_UP] == True and CURRENT_SCREEN == "start":
          jump = True
      else:
        # Reference for making an object jump:  https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping/
          if rect_jump >= -8:
            rect_y -= (rect_jump * abs(rect_jump)) * 0.3
            rect_jump -= 1
          else:
            rect_jump = 8
            jumpCount += 1
            jump = False

      # House
      helper.drawHouse(screen)

      # Sun and Moon
      if background == (19, 2, 46): # night sky
        pygame.draw.circle(screen, (255, 241, 173), (center_x, center_y), 50)
        pygame.draw.circle(screen, (19, 2, 46), (center_x+40, center_y), 50)
        if center_y != 65:
          center_y -= 3
      else:
        pygame.draw.circle(screen, (247, 180, 22), (center_x, center_y), 50)
        if center_y != 65:
          center_y -= 3
      
      # Movable object and if statement for setting boundary for screen size
      if rect_x<0 or rect_x+30 > 500:
        rect_x = 220
        rect_y = 300
        rect_jump = 8
        jump = False
      else:
        pygame.draw.rect(screen, (255, 238, 0), (rect_x, rect_y, 30, 30))
        #pygame.draw.rect(screen, RED, (rect_x+4, rect_y+5, 21, 21))
    
      # Snow fall
      helper.snowfall(screen)
      
      # Grass
      pygame.draw.rect(screen, (80, 153, 60), (0, 330, SCREEN_WIDTH, SCREEN_HEIGHT-330))

      # Car
      helper.drawCar(screen)

  #####

  # Event handler, takes user input and resets variable when program exits 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      print("Program exited.")
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        CURRENT_SCREEN = "homepage"
        helper.homepage(screen, font5)
        intro = False
        center_x = 70
        center_y = 350
        rect_x = 220
        rect_y = 300
        welcomeText_y = 0
        timer = 50
        jumpCount = 0
        time.sleep(0.05)
      if event.key == pygame.K_z:
        background = (19, 2, 46) # night sky colour
      if event.key == pygame.K_x:
        background = (3, 232, 252) # light blue sky colour
    # checks if mouse pointer is in play textbox in home screen and if user has clicked on start button 
    elif mouseX >= 213 and mouseX <= 213+100 and mouseY >= 150 and mouseY <= 150+20 and mouseButton[0] == 1 and CURRENT_SCREEN == "homepage":
      CURRENT_SCREEN = "start"
    # checks if mouse pointer is in about textbox in home screen and if user has clicked on about button 
    elif mouseX >= 201 and  mouseX <= 201+100 and mouseY >= 198 and mouseY <= 198+18 and mouseButton[0] == 1 and CURRENT_SCREEN == "homepage":
      CURRENT_SCREEN = "about"
  
  #####

  clock.tick(60)
  pygame.display.update()

pygame.quit()


