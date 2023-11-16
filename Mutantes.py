#Metodos o Funciones
#Metodo para el Llenado de la matriz de ADN y comprobacion
def cargaADN():
    dna = []
    for i in range(6):
        continuar=True
        while (continuar==True):
            continuar=False
            listaSec=list((input("Ingrese la secuencia/fila nº "+ str(i+1) + " del ADN ")).upper())
            for letra in listaSec:
                if((letra !='A' and letra!='T' and letra!='C' and letra!='G') or len(listaSec)!=6):
                    print("Secuencia no valida, debe ingresar una secuencia de 6 bases nitrogenadas (A,T,G o C)")
                    continuar=True
                    break
        dna.append(listaSec)
    return dna

#Metodo para Mostrar matriz
def mostrarMatriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print("")

#Metodo para comprobar si la secuencia de ADN ingresada pertenece o no a un mutante retorna T o F segun corresponda
def isMutant(dna):
    coincidencia=0
    #Recorremos las filas y verificamos coincidencias, al encontraar la primera coincidencia se rompe el bucle para no sumar 3 coincidencias por ejemplo
    #si una de las filas fuera de un mismo tipo (base nitrogenada) Ej: A A A A A A  Posicion (0 a 3), (1 a 4) y (2 a 5) encontraria 3 coincidencias
    #siendo que solo seria un conjunto de seis A donde se tendria en cuenta solo 4 A realmente (No estoy seguro si este seria o no el razonamiento correcto)
    for fil in range(6):
        for col in range(3):
            if (dna[fil][col]==dna[fil][col+1]==dna[fil][col+2]==dna[fil][col+3]):
                coincidencia = coincidencia+1
                break
    if coincidencia>1:
        return True
    #Recorremos las columnas, verificamos coincidencias y tambien rompemos el bucle de la misma forma que el anterior 
    for fil in range(3):
        for col in range(6):
            if (dna[fil][col]==dna[fil+1][col]==dna[fil+2][col]==dna[fil+3][col]):
                coincidencia = coincidencia+1
                break
    if coincidencia>1:
        return True

    #Recorremos y verificamos coincidencias la diagonales principal y las demas de derecha a izquierda en un rango de 0 a 2 (3 primeras filas) en las filas 
    # y de 0 a 2 tambien en las columnas (3 primeras columnas por cada fila)
    for fil in range(3):
        for col in range(3):
            if dna[fil][col]==dna[fil+1][col+1]==dna[fil+2][col+2]==dna[fil+3][col+3]:
                coincidencia = coincidencia+1
    if coincidencia>1:
        return True

    #Recorremos y verificamos coincidencias en las diagonales "inversa" y demas de izquierda a derecha en un rango de 0 a 2 (3 primeras filas) en las filas 
    # y de 0 a 2 tambien en las columnas (3 primeras columnas por cada fila)
    for fil in range(3):
        for col in range(5,2,-1):
            if dna[fil][col]==dna[fil+1][col-1]==dna[fil+2][col-2]==dna[fil+3][col-3]:
                coincidencia = coincidencia+1
    if coincidencia>1:
        return True
    else:
        return False
    
#Programa Principal
while True:
    print("--------VERIFICACION DE HUMANOS-------")
    op=input(" - Pulse 1 para iniciar la prueba\n - Cualquier tecla para salir\n")
    if op=='1':
        matrizADN=cargaADN()
        print("\nLa secuencia ingresada es:\n")
        mostrarMatriz(matrizADN)
        esMutante=isMutant(matrizADN)
        print("\nRESULTADO: ")
        if esMutante==True:
            print(" MUTANTE")
        else:
            print(" Humano normal")
    else:
        break
    input("\nPulse cualquier tecla para continuar...")




    
















