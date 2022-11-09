r = 255
g = 255
b = 255

def setup():
    frameRate(5)
    size(900, 600)
    background(255, 255, 255)
  
    #Textanweisung für Benutzung der App
    textSize(24)
    fill(0)
    text("Verschiebe den Regler und schau, was passiert!", 400, 570)
           
def draw():
    colorMode(RGB,255)
    
    #Textüberschrift mit Random flimmernder Farbe
    textSize(42)
    rn1 = random(0,255)
    rn2 = random(0,255)
    rn3 = random(0,255)
    fill(rn1, rn2, rn3)
    text("Additive Farbmischung", 250, 50)


    
    #Ausgabe der Prozentzahl des RGB Anteils unter den Reglern
    #"%" zu ergänzen hinter Prozentzahl
    textSize(24)
    fill(0)
    text(str(r*100/255)+("%"), 600, 500)
    text(str(g*100/255)+("%"), 700, 500)
    text(str(b*100/255)+("%"), 800, 500)
    
    #interaktive Regler für den RGB Anteil
    #zu ergänzen über den Prozentzahlen


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
    
