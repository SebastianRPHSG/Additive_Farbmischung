# Funktion: Schieberegler generieren
# objX:      X-Position des Reglers
# objY:      Y-Position des Reglers
# objLength: Laenge des Reglers
def draw_ruler1(objX, objY, objLength):
    global movingMode1
    global pointerPos1
    global pointerVal1
    
    # Schieber einstellen
    pointerRadius = 24
    if pointerPos1 == 0:
        pointerPos1 = objY
    
    # Linie zeichnen
    fill(85)
    strokeWeight(6)
    line(objX, objY, objX , objY- objLength)
    fill(185)
    strokeWeight(2)
    
    # ueberpruefen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseY > pointerPos1 - pointerRadius and mouseY < pointerPos1 + pointerRadius and mouseX > objX - pointerRadius and mouseX < objX + pointerRadius and mousePressed == True:
        movingMode1 = True
    
    # Wenn keine Maustaste gedrueckt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode1 = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode1 == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseY < objY and mouseY > objY - objLength:
            pointerPos1 = mouseY
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseY < objY:
                pointerPos1 = objY - objLength
            if mouseY > objY:
                pointerPos1 = objY

    # Schieber zeichnen  und rot faerben        
    fill(255,0,0)  
    circle(objX, pointerPos1, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal1 = int(100 / float(objLength) * (objY - pointerPos1))
