#String[] dna = {"ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"};
dna = [["ATGCGA"],
    ["CAGTGC"],
    ["TTATGT"],
    ["TGAAGG"],
    ["TCCCCA"],
    ["TCACTG"]
    ]

def isMutant(dna):
    pass

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

#print(verificarFila(dna))

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
print(verificarColumna(dna))


def verificarDiagonal(dna):
    mutantes = 0
    
    

    return mutantes