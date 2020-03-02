def setup():
    rectMode(CORNERS)
    size(700, 600)
    
def draw():
    #rect(mouseX, height/3, width/3*2, height/3*2)
    #clear()
    if mousePressed:
        circle(300, 300, 300)    
    else:
        triangle(230, 230, 590, 390, 450, 500)
     
def mouseClicked():
    clear()
    triangle(230, 230, 590, 390, 450, 500)
