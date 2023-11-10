#TPI laboratorio/Juan Baez, Agustin Colina, Francisco Piaggio, Lucas Muzzillo
def unidad(Transformador):
    partes = Transformador.split()
    if len(partes) == 2:
        valor, unidad = partes
        valor = valor.replace(',', '.')
        try:
            valor = float(valor)
        except ValueError:
            return None, None
        return valor, unidad
    else:
        return None, None
             
def a_metros(valor, unidad):
    unidades = {
        "metros": 1,
        "m": 1,
        "milimetros": 0.001,
        "mm": 0.001,
        "centimetros": 0.01,
        "cm": 0.01,
        "pies": 0.3048,
        "ft": 0.3048,
        "pulgadas": 0.0254,
        "in": 0.0254,
        "yardas": 0.9144,
        "yd": 0.9144,
        "millas": 1609.34,
        "mi": 1609.34
    }
    if unidad in unidades:
        factor = unidades[unidad]
        return valor * factor
    else:
        print(f"Unidad no válida (escriba la unidad entera y en minúsculas): {unidad}")
        return None
   
def resistencia(volumen):
    while True:
        try:
            concreto = int(input("Ingrese la dosificación del concreto que desea aplicar:\n \n1:2:2(presione 1) \n1:2:3(presione 2) \n1:2:4(presione 3)  \n1:3:4(presione 4)  \n1:3:6(presione 5) \n \nOpción: "))
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
            print(f"La cantidad de cemento es de {round(c_cemento, 6)} kg ")
            print("")
            print(f"La cantidad de arena es {round(c_arena, 6)} m³")
            print("")
            print(f"La cantidad de grava es {round(c_grava, 6)} m³")
            print("")
            print(f"La cantidad de agua es {round(c_agua, 6)} L/m³")
            print("")
            registros = [round(c_cemento, 6), round(c_arena, 6), round(c_grava, 6), round(c_agua, 6)]
            return registros   
        except ValueError:
            print(f"El valor {concreto} no está en las opciones")
            
def archivo(registros):
    Registros = "Registros.txt"
    with open(Registros, "a") as archivo:
        archivo.write(nombre + " " + "Cantidades: [Cemento, Arena, Grava, Agua]" + " = " + str(registros) + "\n")
        
def informe(nombre, longitud, ancho, alto, registros, generar_informe=True):
    nombre_archivo = f"Informe_{nombre}.txt"
    
    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"Informe de Proyecto: {nombre}\n\n")
        archivo.write(f"Dimensiones de la construccion:\n")
        archivo.write(f"Longitud: {longitud}\n")
        archivo.write(f"Ancho: {ancho}\n")
        archivo.write(f"Altura: {alto}\n\n")
        archivo.write("Calculo de materiales:\n")
        archivo.write("Cantidades: [Cemento, Arena, Grava, Agua] = " + str(registros) + "\n\n")
        if generar_informe:
            archivo.write(f"Total de metros cubicos de hormigon a entregar: {round(volumen, 6)} m³\n")
        else:
            archivo.write("Informe no generado\n")
    
    return nombre_archivo

salida = 0
while salida != 1:
    try:
        nombre = input("Nombre de su empresa/proyecto: ")
        print("")
        print("Ingrese las dimensiones de la base de la construcción. \nlos valores contemplados son:\n \nmetros = m \ncentímetros = cm \nmilímetros = mm \npies/feet = ft \npulgadas/inches = in \nyardas = yd \nmillas = mi  \n\n(ingresar el valor y separar la unidad)\n")
        longitud = input("Longitud: ")
        ancho = input("Ancho: ")
        alto = input("Altura: ")
        
        valorL, unidadL = unidad(longitud)
        valorAN, unidadAN = unidad(ancho)
        valorAL, unidadAL = unidad(alto)
        
        if None not in (valorL, valorAN, valorAL):
            metrosL = a_metros(valorL, unidadL)
            metrosAN = a_metros(valorAN, unidadAN)
            metrosAL = a_metros(valorAL, unidadAL)
            
        if None not in (metrosL, metrosAN, metrosAL):
            volumen = metrosL * metrosAN * metrosAL
        else:
            print()
            print("Ingrese los valores en el formato pedido")
            
        print("")
        print(f"La cantidad de metros cúbicos es igual a {round(volumen, 6)} m³")
        print("")
        Archivo = resistencia(volumen)
        archivo(Archivo)
        print("¿Desea un registro de la cantidad de materiales?")
        regis = int(input("Si = 1 \nNo = 0 \n: "))
        
        if regis == 1:
            nombre_archivo = informe(nombre, longitud, ancho, alto, Archivo)
            print(f"Informe guardado en el archivo: {nombre_archivo}")
        
        salida = int(input("Ingrese (1) para salir del programa:  "))
    except ValueError:
        print("Ingresa los valores en el formato pedido")
    
    

        
        