a = 10

def setup():
    size(800, 800)
    background(255, 255, 255)
    
def draw():
    colorMode(RGB,100)

 #Roter Kreis  
    fill(100, 0, 0, a)
    circle(300, 400, 200)
    
  #Grüner Kreis  
    fill(0, 100, 0, a)
    circle(400, 400, 200)
    
   #Blauer Kreis  
    fill(0, 0, 100, a)
    circle(350, 500, 200)  
