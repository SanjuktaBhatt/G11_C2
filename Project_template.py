import pygame
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
size = (400, 400)

#Create player rectangle object here

#create variable "playery" to increase position of player in y direction by 1


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project C2")
carryOn = True
while carryOn:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      carryOn = False             
  screen.fill(YELLOW)
  
  #Increment player y coordinate here by "playery" variable
  
  #Check if y coordinate is outside lower boundary of screen, negate "playery" if it is
  
  
   #Check if y coordinate is outside upper boundary of screen, negate "playery" if it is
 


  pygame.draw.rect(screen,LIGHTBLUE,player)
  pygame.display.flip()
pygame.quit()
