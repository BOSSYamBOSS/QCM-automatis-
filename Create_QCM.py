### IMPORTS ###
from pygame import *





### SETTING ###
init()
WIDTH = 600
HEIGHT = 300
screen = dispaly.set_mode((WIDTH, HEIGHT))
display.set_caption("Faire son QCM facilement")

state = "Name"




### DISPLAY ###
running = True
while running:
  for event in event.get():
    if event.type == QUIT:
      running = False
    
