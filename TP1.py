def generarMatriz(n,m):
    matriz = []
    for i in range(n):
        a = [0]*m
        matriz.append(a)
    return matriz

def Mostrar(n, M):
    print("La matriz es la siguiente:")
    for n in M:
        for valor in n:
            print("\t", valor, end=" ")
        print()

def validarFinal(e,x):
    if x==1:
        if e==0:
            return True
        else:
            return False
    elif x==2:
        if e==6 or e==9 or e==12:
            return True
        else:
            return False
    elif x==3:
        if e==1 or e==2:
            return True
        else:
            return False

def cambiarCadena(cadena):
    cadenaaux = cadena
    cadenaaux = cadenaaux.replace("a", "0")
    cadenaaux = cadenaaux.replace("b", "1")
    return cadenaaux

def recorrerMatriz(cadena,M):
    e = 0
    e = int(e)
    for i in range(len(cadena)):
        cadenita = cadena[i]
        cadenita = int(cadenita)

        e = M[e][cadenita]
    return e

def traerMenu():
    print("-----Trabajo Practico N° 1-----")
    print(
        "1.Conjunto de cadenas sobre {a,b}, donde la paridad de la cantidad de b sea la misma que la paridad de la longitud de la cadena.")
    print(
        "2.Conjunto de cadenas sobre {a,b} de longitud 4 que contengan menor cantidad de a que de b, o que comiencen con b.")
    print("3.Dada la expresion regular, llevar a automata deterministico: ((a*|b*)*)*")
    print("4.Salir")
    respuesta = input("Realizar ejercicio: ")
    respuesta = int(respuesta)
    return respuesta

def traerCondicionales():
    respuesta = traerMenu()
    if respuesta == 1:
        matriz2 = generarMatriz(4, 2)
        matriz2[0][0] = 1
        matriz2[0][1] = 2
        matriz2[1][0] = 0
        matriz2[1][1] = 3
        matriz2[2][0] = 3
        matriz2[2][1] = 0
        matriz2[3][0] = 2
        matriz2[3][1] = 1
        cadena = input("Ingrese la cadena con a o b: ")
        cadena = cambiarCadena(cadena)
        e = recorrerMatriz(cadena, matriz2)
        if validarFinal(e, 1):
            print("ACEPTA LA CADENA")
        else:
            print("NO ACEPTA LA CADENA")

    elif respuesta == 2:
        matriz2 = generarMatriz(13, 2)
        matriz2[0][0] = 1
        matriz2[0][1] = 2
        matriz2[1][0] = 10
        matriz2[1][1] = 4
        matriz2[2][0] = 7
        matriz2[2][1] = 7
        matriz2[3][0] = 3
        matriz2[3][1] = 3
        matriz2[4][0] = 3
        matriz2[4][1] = 5
        matriz2[5][0] = 3
        matriz2[5][1] = 6
        matriz2[6][0] = 3
        matriz2[6][1] = 3
        matriz2[7][0] = 8
        matriz2[7][1] = 8
        matriz2[8][0] = 9
        matriz2[8][1] = 9
        matriz2[9][0] = 3
        matriz2[9][1] = 3
        matriz2[10][0] = 11
        matriz2[10][1] = 3
        matriz2[11][0] = 12
        matriz2[11][1] = 3
        matriz2[12][0] = 3
        matriz2[12][1] = 3
        cadena = input("Ingrese la cadena con a o b: ")
        cadena = cambiarCadena(cadena)
        e = recorrerMatriz(cadena, matriz2)
        if validarFinal(e, 2):
            print("ACEPTA LA CADENA")
        else:
            print("NO ACEPTA LA CADENA")
    elif respuesta == 3:
        matriz2 = generarMatriz(3, 2)
        matriz2[0][0] = 1
        matriz2[0][1] = 2
        matriz2[1][0] = 1
        matriz2[1][1] = 2
        matriz2[2][0] = 1
        matriz2[2][1] = 2
        cadena = input("Ingrese la cadena con a o b: ")
        cadena = cambiarCadena(cadena)
        e = recorrerMatriz(cadena, matriz2)
        if validarFinal(e, 3):
            print("ACEPTA LA CADENA")
        else:
            print("NO ACEPTA LA CADENA")
    elif respuesta == 4:
        exit(print("HA FINALIZADO CON EXITO, GRACIAS VUELVAS PRONTOS"))
    traerCondicionales()

traerCondicionales()
