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
    cargaADN()
    ```

**3. Mostramos por pantalla la matriz ingresada:**

    ```
    MostrarADN(matriz)
    ```

**4. Luego llamamos a la funcion isMutant() para clasificar el ADN ingresado esta funcion nos retornara un boleano V o F** 

    ```
    #Metodo para comprobar si la secuencia de ADN ingresada pertenece o no a un mutante retorna T o F segun corresponda
    isMutant(dna)
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
1. Puedes ejecutar el código en Visual Studio Code (VS Code), consola o cualquier IDE de tu preferencia.
2. Si utilizas VS Code agrega la extensión de Python para poder continuar.
3. Puedes acceder al codigo desde el siguiente [enlace](https://github.com/Leinad-95/Parcial2_Mutantes_TUP/blob/main/Mutantes.py), descargarlo y ejecutarlo.

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
    A   T   G   C   G   A
    C   A   G   T   G   C
    T   T   A   T   T   T
    A   G   A   C   G   G
    G   C   G   T   C   A
    T   C   A   C   T   G

    HUMANO NORMAL


