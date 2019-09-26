print "hola"

rectSizeX = 200
rectSizeY = 100
curve = 7
rect1vs1X = 20
rect1vs1Y = 80
rectCPUvsCPUX = 140
rectCPUvsCPUY = 200
rect1vsCPUX = 260
rect1vsCPUY = 80

ovso = False
ovscpu = False
cpuvscpu = False

def setup():
    size(60*8, 60*8)
    textSize(32);
    background(255,204,0)
    fill(0, 255, 0)
    rect(rect1vs1X, rect1vs1Y, rectSizeX, rectSizeY, curve)
    rect(rect1vsCPUX, rect1vsCPUY, rectSizeX, rectSizeY, curve)
    rect(rectCPUvsCPUX, rectCPUvsCPUY, rectSizeX, rectSizeY, curve)
    fill(0, 0, 255)
    text("JUGADORES...", 120, 45)
    text("1 VS 1", 75, 140)
    text("1 VS CPU", 290, 140)
    text("CPU VS CPU", 148, 260)

def draw():
    print "adios"
    if ovso:
        background(0, 46, 255)

def update():
    if over1vs1(rect1vs1X, rect1vs1Y, rectSizeX, rextSizeY):
        print "over 1vs1"
        ovso = True
    else:
        print "other"
        ovso = False

def mousePressed():
    if (ovso):
        print "pressssss"
    print "notpreeeessss"
    
def over1vs1():
    if (mouseX >= x and mouseX <= x+width and mouseY >= y and mouseY <= y+height):
        return True;
    else:
        return False;
