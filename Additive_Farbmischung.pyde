from ruler1 import *
# Globale Variablen:
# movingMode (Boolean): True, wenn der Schieber (Kreis) in Bewegung ist, False wenn nicht
# pointerPos (Integer): Position des Pointers in Pixeln
# pointerVal (Float):   Eingestellter Wert (0 - 100)
# Definiert drei Mal fuer jeden einzelnen Schieberegler
movingMode1 = False
pointerPos1 = 0
pointerVal1 = 1.0

movingMode2 = False
pointerPos2 = 0
pointerVal2 = 1.0

movingMode3 = False
pointerPos3 = 0
pointerVal3 = 1.0

def setup():
    frameRate(15)
    size(900, 600)
    background(255, 255, 255)
  
           
def draw():
    
    #RGB Werte in Abhaengigkeit der PointerValues definiert
    
    r = 255 * pointerVal1 / 100
    g = 255 * pointerVal2 / 100
    b = 255 * pointerVal3 / 100
    
    #Bei jedem Durchgang wird alles mit dem Hintergrund ueberschrieben und neu gemacht
    background(255, 255, 255)

    
    #Textueberschrift mit den RGB-Werten entsprechender Faerbung
    textSize(42)
    fill(r, g, b)
    #Textanweisung fuer Benutzung der App
    text("Additive Farbmischung", 250, 50)
    textSize(24)
    text("Verschiebe den Regler und schau, was passiert!", 400, 570)

    
    #Ausgabe der Prozentzahl des RGB Anteils unter den Reglern
    #"%" zu ergaenzen hinter Prozentzahl
    textSize(24)
    fill(0)
    text(str(r*100/255)+("%"), 600, 500)
    text(str(g*100/255)+("%"), 700, 500)
    text(str(b*100/255)+("%"), 800, 500)
    


    #Rotes Quadrat  
    fill(r, 0, 0)
    square(75, 75, 250)
    
    #Gruenes Quadrat  
    fill(0, g, 0)
    square(275, 75, 250)
    
    #Blaues Quadrat  
    fill(0, 0, b)
    square(175, 275, 250)  
    
    #Mittleres Quadrat  
    fill(r, g, b)
    square(275, 275, 50)
    
    #Schnittstelle Rot-Gruen
    fill(r, g, 0)
    rect(275, 75, 50, 200)
    
    #Schnittstelle Rot-Blau
    fill(r, 0, b)
    rect(175, 275, 100, 50)
    
    #Schnittstelle Gruen-Blau
    fill(0, g, b)
    rect(325, 275, 100, 50)
    
# '''
# ' Schieberegler
# ' Simon Hefti, Okt. 2020 veraendert von Maria Mannai November 2022
# '''


#aufrufen der Schieberegler Funktionen 

    ruler1 = draw_ruler1(620, 450, 200)
    ruler2 = draw_ruler2(720, 450, 200)
    ruler3 = draw_ruler3(820, 450, 200)

            
# Zweite Definition fuer zweiten Schieberegler

def draw_ruler2(objX, objY, objLength):
    global movingMode2
    global pointerPos2
    global pointerVal2
    
    # Schieber einstellen
    pointerRadius = 24
    if pointerPos2 == 0:
        pointerPos2 = objY
    
    # Linie zeichnen
    fill(85)
    strokeWeight(6)
    line(objX, objY, objX , objY- objLength)
    fill(185)
    strokeWeight(2)
    
    # ueberpruefen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseY > pointerPos2 - pointerRadius and mouseY < pointerPos2 + pointerRadius and mouseX > objX - pointerRadius and mouseX < objX + pointerRadius and mousePressed == True:
        movingMode2 = True
    
    # Wenn keine Maustaste gedrueckt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode2 = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode2 == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseY < objY and mouseY > objY - objLength:
            pointerPos2 = mouseY
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseY < objY:
                pointerPos2 = objY - objLength
            if mouseY > objY:
                pointerPos2 = objY

    # Schieber zeichnen  und gruen faerben       
    fill(0,255,0)          
    circle(objX, pointerPos2, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal2 = int(100 / float(objLength) * (objY - pointerPos2))
            
# Zweite Definition fuer dritten Schieberegler

def draw_ruler3(objX, objY, objLength):
    global movingMode3
    global pointerPos3
    global pointerVal3
    
    # Schieber einstellen
    pointerRadius = 24
    if pointerPos3 == 0:
        pointerPos3 = objY
    
    # Linie zeichnen
    fill(85)
    strokeWeight(6)
    line(objX, objY, objX , objY- objLength)
    fill(185)
    strokeWeight(2)
    
    # ueberpruefen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseY > pointerPos3 - pointerRadius and mouseY < pointerPos3 + pointerRadius and mouseX > objX - pointerRadius and mouseX < objX + pointerRadius and mousePressed == True:
        movingMode3 = True
    
    # Wenn keine Maustaste gedrueckt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode3 = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode3 == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseY < objY and mouseY > objY - objLength:
            pointerPos3 = mouseY
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseY < objY:
                pointerPos3 = objY - objLength
            if mouseY > objY:
                pointerPos3 = objY

    # Schieber zeichnen und blau faerben   
    fill(0,0,255)          
    circle(objX, pointerPos3, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal3 = int(100 / float(objLength) * (objY - pointerPos3))
            
    
