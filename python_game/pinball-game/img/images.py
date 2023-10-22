import pygame, constants, os

cwd = os.getcwd() + "/"

# ball = pygame.transform.scale(pygame.image.load("img/ball.png"),(40,40))
menu = pygame.transform.scale(pygame.image.load(f"{cwd}img/menu.png"),(constants.gameW,constants.gameH))
playButton = pygame.transform.scale(pygame.image.load(f"{cwd}img/playbutton.png"),(int(0.3*703),int(0.3*212)))
gameOver = pygame.transform.scale(pygame.image.load(f"{cwd}img/GAMEOVER.png"),(constants.gameW,constants.gameH))

brick = pygame.transform.scale(pygame.image.load(f"{cwd}img/redthingy.png"),(int(0.3*318),int(0.3*121)))
burst = pygame.transform.scale(pygame.image.load(f"{cwd}img/blueburst.png"),(int(0.3*338),int(0.3*338)))
bumper = pygame.transform.scale(pygame.image.load(f"{cwd}img/orangeface.png"),(int(0.3*128),int(0.3*128)))
button = pygame.transform.scale(pygame.image.load(f"{cwd}img/button.png"),(int(0.3*254),int(0.3*300)))
plunger = pygame.transform.scale(pygame.image.load(f"{cwd}img/startbouncything.png"),(20,60))
