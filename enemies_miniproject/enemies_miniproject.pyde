playerx = 100
playery = 150
playerR = 25
playerLane = 2

backgroundx = 1200
backgroundy = 300

enemyx = backgroundx
enemyy = 0
enemyside = 50
lane = 0

point = 0
hiddenPoint = 0

baseSpeed = 25
speed = baseSpeed

baseEnemyTimer = 50
enemyTimer = 50
enemies = []

class enemy():
    def __init__(self, enemyy, lane):
        self.enemyx = backgroundx + enemyside/2
        self.enemyy = enemyy
        self.lane = lane
    def new_location(self):
        self.enemyx = self.enemyx - speed
        
def setup():
    global enemyTimer
    global point
    global speed
    size(backgroundx, backgroundy)
    enemyTimer = baseEnemyTimer
    point = 0
    speed = baseSpeed
    
def draw():
    global enemyy
    global enemyTimer
    global point
    global speed
    global hiddenPoint
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
        newenemy = enemy(enemyy, lane)
        enemies.append(newenemy)
        enemyTimer = baseEnemyTimer
        
    else:
        enemyTimer = enemyTimer - 1
    rectMode(CENTER)
    for newenemy in enemies:
        rect(newenemy.enemyx,newenemy.enemyy,enemyside,enemyside)
        newenemy.new_location()
        if playerx < newenemy.enemyx + 15 and playerx > newenemy.enemyx - 15 and playerLane == newenemy.lane:
            setup()
            
    stroke(0,255,0)
    fill(0,255,0)
    ellipseMode(CENTER)
    ellipse(playerx, playery, playerR, playerR)
    
    point = point + 1
    hiddenPoint = hiddenPoint + 1
    if hiddenPoint == 100:
        hiddenPoint = 0
        speed = speed + 1
    fill(255)
    textSize(30)
    text(point,25,25)
    
    
def keyPressed():
    global playery
    global playerLane
    if key == "1":
        playery = 50
        playerLane = 1
    elif key == "2":
        playery = 150
        playerLane = 2
    elif key == "3":
        playery = 250
        playerLane = 3
def reset():
    global enemyTimer
    size(backgroundx, backgroundy)
    enemyTimer = baseEnemyTimer
