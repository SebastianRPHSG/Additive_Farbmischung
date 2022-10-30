r = 255
g = 255
b = 255

def setup():
    size(600, 600)
    background(255, 255, 255)
    
def draw():
    colorMode(RGB,100)

    #Rotes Quadrat  
    fill(r, 0, 0)
    square(75, 75, 250)
    
    #Grünes Quadrat  
    fill(0, g, 0)
    square(275, 75, 250)
    
    #Blaues Quadrat  
    fill(0, 0, b)
    square(175, 275, 250)  
    
    #Mittleres Quadrat  
    fill(r, g, b)
    square(275, 275, 50)
    
    #Schnittstelle Rot-Grün
    fill(r, g, 0)
    rect(275, 75, 50, 200)
    
    #Schnittstelle Rot-Blau
    fill(r, 0, b)
    rect(175, 275, 100, 50)
    
    #Schnittstelle Grün-Blau
    fill(0, g, b)
    rect(325, 275, 100, 50)
