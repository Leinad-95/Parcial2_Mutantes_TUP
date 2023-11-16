# Examen Parcial 2 (GLOBAL) - Mutantes
- Nombre y Apellido: Daniel Núñez
- Legajo: 51608
- Email: danielnunezsalcedo95@gmail.com

## Sobre el Proyecto
Se necesita identificar por medio de una secuencia de ADN de 6x6 si un humano es Mutante o no. Teniendo en cuenta que:
- Cada secuencia contiene 6 Bases Nitrogenadas que pueden ser A, T, C o G.
- Los casos mutantes son aquellos que presentan **MAS DE DOS SECUNCIAS** de cuatro letras iguales, de forma oblicua, horizontal o vertical.

## Como lo resolvimos
Se propone el desarrollo de las siguientes instrucciones mediante el uso de un rústico Menu Principal

    ```
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
    ```

**1. Solicitamos el ingreso de la secuencia de ADN** y verificamos su tamaño (6 caracteres) y que los mismos correspondan a las Bases Nitrogenadas correspondientes

    ``` 
    def cargaADN()
    ```

**3. Mostramos por pantalla la matriz ingresada:**

    ```
    def MostrarADN(matriz)
    ```

**4. Luego llamamos a la funcion isMutant() para clasificar el ADN ingresado esta funcion nos retornara un boleano V o F** 
    ```
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
        if coincidencia>2:
            return True
        #Recorremos las columnas, verificamos coincidencias y tambien rompemos el bucle de la misma forma que el anterior 
        for fil in range(3):
            for col in range(6):
                if (dna[fil][col]==dna[fil+1][col]==dna[fil+2][col]==dna[fil+3][col]):
                    coincidencia = coincidencia+1
                    break
        if coincidencia>2:
            return True

        #Recorremos y veridicamos coincidencias la diagonales principal y las demas de derecha a izquierda en un rango de 0 a 2 (3 primeras filas) en las filas 
        # y de 0 a 2 tambien en las columnas (3 primeras columnas por cada fila)
        for fil in range(3):
            for col in range(3):
                if dna[fil][col]==dna[fil+1][col+1]==dna[fil+2][col+2]==dna[fil+3][col+3]:
                    coincidencia = coincidencia+1
        if coincidencia>2:
            return True

        #Recorremos y veridicamos coincidencias en las diagonales "inversa" y demas de izquierda a derecha en un rango de 0 a 2 (3 primeras filas) en las filas 
        # y de 0 a 2 tambien en las columnas (3 primeras columnas por cada fila)
        for fil in range(3):
            for col in range(5,2,-1):
                if dna[fil][col]==dna[fil+1][col-1]==dna[fil+2][col-2]==dna[fil+3][col-3]:
                    coincidencia = coincidencia+1
        if coincidencia>2:
            return True
        else:
            return False
        ```
**5. Para Finalizar de acuerdo al retorno de la funcion anterior el programa mostrara un mensaje indicando si se trata o no de un MUTANTE y tambien decidiremos si se quiere continuar con la consulta de otro ADN o no volviendo al Menu Principal** 
    ```
    esMutante=isMutant(matrizADN)
        print("\nRESULTADO: ")
        if esMutante==True:
            print(" MUTANTE")
        else:
            print(" Humano normal")
    else:
        break
    input("\nPulse cualquier tecla para continuar...")
    ```
# EJECUCION
1. Para ejecutar el código en Visual Studio Code (VS Code), primero se debe instalar tanto VS Code como Python, asegurándote de agregar Python al PATH durante la instalación.
2. Luego, abre VS Code y agrega la extensión de Python.
3. Puedes acceder al codigo desde el siguiente [enlace](https://), descargarlo y ejecutarlo.

## CASOS DE PRUEBA
### Ejemplo 1 MUTANTE
    ```
    Secuencia 1 : acgtgc
    Secuencia 2 : cagtac
    Secuencia 3 : gtacgc
    Secuencia 4 : ttgaac
    Secuencia 5 : gtcatg
    Secuencia 6 : tcgact

    ADN Ingresado:

    A   C   G   T   G   C
    C   A   G   T   A   C
    G   T   A   C   G   C
    T   T   G   A   A   C
    G   T   C   A   T   G
    T   C   G   A   C   T
    
    MUTANTE
    ```
### Ejemplo 2 HUMANO
    Secuencia 1 : atgcga
    Secuencia 2 : cagtgc
    Secuencia 3 : ttattt
    Secuencia 4 : agacgg
    Secuencia 5 : gcgtca
    Secuencia 6 : tcactg

    ADN Ingresado:
    A   T	G	C	G	A
    C	A	G	T	G	C
    T	T	A	T	T	T
    A	G	A	C	G	G
    G	C	G	T	C	A
    T	C	A	C	T	G

    HUMANO NORMAL


