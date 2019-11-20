playerx = 100
playery = 150
playerR = 25

backgroundx = 1200
backgroundy = 300

enemyx = backgroundx
enemyy = 0
enemyside = 50

point = 0

speed = 25

enemytimer = 100

enemies = []

def setup():
    size(backgroundx,backgroundy)


def draw():
    global point
    background(156, 22, 26)
    stroke(0,0,255)
    line(backgroundx, 100, 0, 100)
    line(backgroundx, 200, 0, 200)
    
    stroke(0,255,0)
    fill(0,255,0)
    ellipseMode(CENTER)
    ellipse(playerx, playery, playerR, playerR)
    
    point = point + 1
    fill(255)
    textSize(30)
    text(point,25,25)
    
    
def keyPressed():
    global playery
    if key == "1":
        playery = 50
    elif key == "2":
        playery = 150
    elif key == "3":
        playery = 250
