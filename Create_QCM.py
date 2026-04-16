### IMPORTS ###
from pygame import *
from math  import *





### SETTING ###
init()
WIDTH = 900
HEIGHT = 500
screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Faire son QCM facilement")

state = "Name"
clock = time.Clock().tick





### CONSTANTS ###
color_back = (75, 75, 200)
color_fore = (20, 20, 100)
a = gcd(WIDTH, HEIGHT)
w = WIDTH   // a
liste = [x for x in range(1, w) if w % x == 0 and 40 <= w // x <= 60]
a *= liste[0] if liste else 1

w = WIDTH  //a
h = HEIGHT// a





### CLASSES ###
class Button:
    def __init__(self, x, y, w, h):
        self.color = (30, 30, 30)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        pass

    def draw(self, text, police=font.SysFont("Arial", 36), color=(255, 255, 255)):
        texte = police.render(text, True, color)
        screen.blit(texte, (self.x, self.y))
        pass

    def is_clicked(self, event):
        pass

class TextArea:
    def __init__(self, x, y, w, h, filler):
        self.active = False
        self.button = Button(x+50, y+50, w, h)
        self.placeholder = filler
        self.text = ""
        self.rect = (x, y, w, h)

    def show(self):
        draw.rect(screen, (0, 0, 0), self.rect)
        if self.text:
            text = self.text
            police = font.SysFont("Times New Roman", 20)
            self.button.draw(text, police)
        else:
            text = self.placeholder
            police = font.SysFont("Comic Sans MS", 15)
            self.button.draw(text, police, (100, 100, 100))
Titre = Button(300, 25, 300, 50)
Ask_Titre = TextArea(150, 100, 600, 300, "Nom de l'évaluation")





### FUNCTIONS ###
def fond():
    screen.fill(color_back)
    for i in range(w):
        for j in range(h):
            draw.rect(screen, color_fore, (i*a+1, j*a+1, a-2, a-2))

def ask_name():
    Titre.draw("Nom de l'évaluation")
    Ask_Titre.show()
    pass

def ask_points():
    pass

def make_questions():
    pass

def make_folder():
    pass

def make_exam():
    pass

def make_correction():
    pass

def validating():
    pass





### DISPLAY ###
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    fond()
    if state == "Name":
        ask_name()
    elif state == "Points":
        ask_points()
    elif state == "QCM":
        make_questions()
    elif state == "Verification":
        validating()

    display.flip()
    clock(60)

make_folder()
make_exam()
make_correction()
