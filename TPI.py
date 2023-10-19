#TPI laboratorio/Juan Baez
def numeros(Transformador):
    cad=""
    for i in Transformador:
        if i.isdigit() or i == ".":
            cad = cad + i
    return float(cad)

def resistencia(volumen):
    concreto = int(input("Ingrese que dosificación del concreto quiere aplicar:\n \n1:2:2(presione 1) \n1:2:3(presione 2) \n1:2:4(presione 3)  \n1:3:4(presione 4)  \n1:3:6(presione 5) \n \nOpción: "))
    cemento = 0
    arena = 0
    grava = 0
    agua = 0
    if concreto == 1:
        cemento += 420
        arena += 0.67
        grava += 0.67
        agua += 220
        c_cemento = volumen * cemento * 1.05
        c_arena = volumen * arena
        c_grava = volumen * grava
        c_agua = volumen * agua 
    elif concreto == 2:
        cemento += 350
        arena += 0.56
        grava += 0.84
        agua += 180
        c_cemento = volumen * cemento * 1.05
        c_arena = volumen * arena
        c_grava = volumen * grava
        c_agua = volumen * agua 
    elif concreto == 3:
        cemento += 300
        arena += 0.48
        grava += 0.96
        agua += 170
        c_cemento = volumen * cemento * 1.05
        c_arena = volumen * arena
        c_grava = volumen * grava
        c_agua = volumen * agua 
    elif concreto == 4:
        cemento += 260
        arena += 0.63
        grava += 0.84
        agua += 170
        c_cemento = volumen * cemento * 1.05
        c_arena = volumen * arena
        c_grava = volumen * grava
        c_agua = volumen * agua 
    elif concreto == 5:
        cemento += 210
        arena += 0.5
        grava += 1.0
        agua += 160
        c_cemento = volumen * cemento * 1.05
        c_arena = volumen * arena
        c_grava = volumen * grava
        c_agua = volumen * agua 
        
    print("")    
    print(f"La cantidad de cemento es de {round(c_cemento,6)} kg ")
    print("")
    print(f"La cantidad de arena es {round(c_arena,6)} m³")
    print("")
    print(f"La cantidad de grava es {round(c_grava,6)} m³")
    print("")
    print(f"La cantidad de agua es {round(c_agua,6)} L/m³")
    print("")   
        
print("Ingrese las dimensiones de la base de la construccion, los valores son tomados como metros \n")
while True:
    try:
        longitud = input("Longitud: ")
        ancho = input("Ancho: ")
        alto = input("Altura: ")
        volumen = numeros(longitud) * numeros(ancho) * numeros(alto)
        print("")
        print(f"La cantidad de metros cubicos es igual a {volumen} m³")
        print("")
        resistencia(volumen)
        break
    except ValueError:
        print("Ingresa los valores en el formato pedido")
    
    

        
        