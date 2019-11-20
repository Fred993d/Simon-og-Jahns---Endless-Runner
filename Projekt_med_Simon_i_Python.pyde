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
    global img
    global player
    global enemy
    size(backgroundx,backgroundy)
    img = loadImage("Warsong gullach.png")
    player = loadImage("Rogueo logo.png")
    enemy = loadImage("Paladino logo.png")

def draw():
    global point
    
    background(156, 22, 26)
    imageMode(CORNER)
    image(img, 0,0, backgroundx, backgroundy)
    stroke(0,0,255)
    # line(backgroundx, 100, 0, 100)
    # line(backgroundx, 200, 0, 200)
    
    stroke(0,255,0)
    fill(0,255,0)
    imageMode(CENTER)
    image(player,playerx,playery,playerR * 2,playerR * 2)
    
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
