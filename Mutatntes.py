#String[] dna = {"ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"};
dna = [

    ]

def isMutant(dna):
    if (verificarColumna(dna) + verificarFila(dna) + verificarDiagonalPrincipal(dna) + verificarDiagonalInversa (dna))> 2:
        return True
    else:
        return False

def verificarFila(dna):
    mutante=0
    for i in range(0,len(dna)):
        cont = 1
        for j in range(0,len(dna[i][0])-1):
            if dna[i][0][j] == dna [i][0][j+1]:
                cont+=1
            else:
                cont=1
            if cont>3:
                mutante+=1
                break
    return mutante

def verificarColumna(dna):
    mutante=0
    cont=1
    for j in range(0,len(dna[0][0])):
        cont = 1
        for i in range(0,len(dna)-1):
                print(dna[i][0][j])
                print("-------------")
                print(dna[i+1][0][j])
                print("   ")
                if dna[i][0][j] == dna[i+1][0][j]:
                        cont+=1
                else:
                    cont=1
                if cont>3:
                    mutante+=1
                    break
    return mutante


def verificarDiagonalPrincipal(dna):
    mutantes = 0
    cont = 1
    #verifico la diagonal principal
    for i in range(len(dna)-1):
        if dna[i][0][i] == dna[i+1][0][i+1]:
            cont+=1
        else:
            cont=1
        if cont>3:
            mutantes+=1
            break
    return mutantes


def verificarDiagonalInversa(dna):
    mutantes = 0
    cont = 1
    n = len(dna)  

    # Verifico la diagonal inversa
    for i in range(n - 1):
        if dna[i][0][n - 1 - i] == dna[i + 1][0][n - 2 - i]:
            cont += 1
            if cont >= 4:
                mutantes += 1
                break
        else:
            cont = 1

    return mutantes

def verificarDiagonales(dna):
    n = len(dna)
    mutantes = 0

    # Diagonales de izquierda a derecha
    for fila in range(0,5):
        for columna in range(1 - fila, 3):
            cont = 1
            for i in range(n - max(fila, columna) - 1):
                if dna[fila + i][0][columna + i] == dna[fila + i + 1][0][columna + i + 1]:
                    cont += 1
                    if cont >= 4:
                        mutantes += 1
                        break
                else:
                    cont = 1

    # Diagonales de derecha a izquierda
    # Comienzan en (0,3), (0,4), (1,5), y (2,5)
    for fila in range(2):
        for columna in range(3 + fila, 6):
            cont = 1
            for i in range(min(columna, n - 1 - fila)):
                if dna[fila + i][0][columna - i] == dna[fila + i + 1][0][columna - i - 1]:
                    cont += 1
                    if cont >= 4:
                        mutantes += 1
                        break
                else:
                    cont = 1

    return mutantes

def mostrarArray(dna):
    for i in range(0,len(dna)):
        print (dna[i][0])

def validarLetras(secuenciaADN):
    if len(secuenciaADN) != 6:
        print("La cantidad de valores no coincide, deben ser 6")
        return False
    for letra in secuenciaADN.upper():
        if letra not in ['A', 'C', 'G', 'T']:
            print("Letras no correspondientes a un ADN, recuerde tambien sin espacios")
            return False

    return True


while True:
    print()
    print("---------------MUTANTES---------------")
    for i in range(0,6):
        secuenciaADN =[]
        secuencia= input(f"Ingresar la secuencia de ADN 6 valores A T C G (sin espacios) N° {i+1} ")
        while(not validarLetras(secuencia)):
            secuencia = input("Ingrese nuevamente la secuencia de ADN  ")
        secuenciaADN.append(secuencia.upper)
        dna.append(secuenciaADN)
        secuenciaADN=[]

    print("Vamos a analizar su secuencia de ADN")
    mostrarArray(dna)
    print("---------------LA PERSONA ES--------------")
    print("La persona es Mutante" if isMutant else "La persona no es Mutante")
    otra_entrada = input("\n¿Desea ingresar otra cadena de ADN? (s/n): ")
    if otra_entrada.lower() != 's':
        print()
        print("--------------Muchas gracias por usar nuestros servicios--------------")
        break

