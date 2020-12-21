width=800
height=600
speedx=3
speedy=3
radiushero=30
counter=0
speedypl = 10
platformsizey=150
platformsizex=10

xpositionhero=width//2
ypositionhero=height//2
ypositionplatform=height//2

def setup():
    size(width, height)
    frameRate(120)

def draw():
    global xpositionhero, radiushero, counter, speedx, speedy, ypositionhero, ypositionplatform, platformsizex, platformsizey
    background(255, 255, 255)
    fill(0)
    textSize(20)
    text(counter, width//2, height//2)
    fill(255, 0, 0)
    ellipse(xpositionhero, ypositionhero, radiushero, radiushero)
    fill(255, 255, 255)
    ellipse(xpositionhero, ypositionhero, radiushero-6, radiushero-6)
    fill(0)
    rect(0, ypositionplatform, platformsizex, platformsizey)
    
    xpositionhero+=speedx
    ypositionhero+=speedy
    if (xpositionhero > (width-radiushero//2)):
        speedx *= -1
    if (xpositionhero < 0):
        background(0,0,0)
        fill(255,0,0)
        textSize(70)
        text("You Lost!", width/4, height/2)
        textSize(20)
        text("Press space to start new game", width/4 + 12, height/2 + 25)
        counter=0
        speedx=0
        speedy=0
    if (ypositionhero > (height-radiushero//2)):
        speedy *= -1
    if (ypositionhero < radiushero//2):
        speedy *= -1
    if (ypositionplatform > height):
        ypositionplatform=-platformsizey
    if (ypositionplatform < -platformsizey):
        ypositionplatform=height
    
    if (xpositionhero <= platformsizex and 0 <= (ypositionhero - ypositionplatform) <= platformsizey):
            speedx = abs(speedx)
            counter += 1

def keyPressed():
    global ypositionplatform, speedypl, speedx, speedy, xpositionhero, ypositionhero
    if (keyCode==40):
        ypositionplatform+=speedypl
    if (keyCode==38):
        ypositionplatform-=speedypl
    if (keyCode==32) and speedx==0 and speedy==0:
        xpositionhero=width//2
        ypositionhero=height//2
        speedx=3
        speedy=3
