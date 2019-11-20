playerx = 100
playery = 150
playerR = 25

backgroundx = 1200
backgroundy = 300

enemyx = backgroundx
enemyy = 0
enemyside = 50
lane = 0

point = 0

speed = 25

baseEnemyTimer = 50
enemyTimer = 50
enemies = []

class enemy():
    def __init__(self, enemyy):
        self.enemyx = backgroundx + enemyside/2
        self.enemyy = enemyy
    def new_location(self):
        self.enemyx = self.enemyx - 25
        
def setup():
    global enemyTimer
    size(backgroundx, backgroundy)
    enemyTimer = baseEnemyTimer
    
def draw():
    global enemyy
    global enemyTimer
    global point
    background(156, 22, 26)
    stroke(0,0,255)
    line(backgroundx, 100, 0, 100)
    line(backgroundx, 200, 0, 200)
    stroke(0)
    fill(255)
    if enemyTimer == 0:
        lane = int(random(1,4))
        if lane == 1:
            enemyy = 50
        elif lane == 2:
            enemyy = 150
        elif lane == 3:
            enemyy = 250
        newenemy = enemy(enemyy)
        enemies.append(newenemy)
        enemyTimer = baseEnemyTimer
        
    else:
        enemyTimer = enemyTimer - 1
    rectMode(CENTER)
    for newenemy in enemies:
        rect(newenemy.enemyx,newenemy.enemyy,enemyside,enemyside)
        newenemy.new_location()
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
