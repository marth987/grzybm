def setup():
    size(500, 500)
    textSize(80)
    frameRate(5)
    global slownik_kolorow
    slownik_kolorow = {"LightSeaGreen":(32, 178, 170), "BlueViolet":(138, 43, 226), "LightCoral":(240, 128, 128)}
    global lista_kolorow
    lista_kolorow = []
    
    for klucz, wartosc in slownik_kolorow.items():
        lista_kolorow.append(wartosc)
    global iteracja_programu
    iteracja_programu = 0
    
def draw():
    clear()
    global iteracja_programu
    iteracja_programu +=1
    
    if mouseX==150:
        fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)])
    elif mouseX==65:
        fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)])
    elif 65<mouseX<150:
        fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)])
    elif mouseY==190:
        fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)])
    elif mouseY==65:
        fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)])
    elif 65<mouseY<190:
        fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)])
    text("M", width/2-100, height/2)
    
    if key == "g":
        text("G", width/2+10, height/2)
        if keyPressed:
            fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)])
            text("G", width/2+10, height/2)
            
# 1pkt
# brakuje obsługi strzałek, myszka działa 'dziwnie', brakuje kształtu niestandardowego
# plus do aktywności za zmianę kolorów
