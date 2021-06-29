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
player=pygame.Rect(200,200,20,20)
#create variable "playery" to increase position of player in y direction by 1
playery=1

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project C2")
carryOn = True
while carryOn:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      carryOn = False             
  screen.fill(YELLOW)
  
  #Increment player y coordinate here by "playery" variable
  player.y=player.y+playery
  #Check if y coordinate is outside lower boundary of screen, negate "playery" if it is
  if player.y>=390:
    playery=-playery
   #Check if y coordinate is outside upper boundary of screen, negate "playery" if it is
  if player.y<=0:
    playery=-playery
    
  pygame.draw.rect(screen,LIGHTBLUE,player)
  pygame.display.flip()
pygame.quit()
