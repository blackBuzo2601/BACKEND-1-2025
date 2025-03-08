#CONVERTIDOR DE NUMEROS ROMANOS A NUMERICOS
#BUZO ZAMORA ELIAN | 20760257
#DESARROLLO BACKEND I


#REGLAS PRINCIPALES A VALIDAR
#Que todo el numero romano contenga un caracter valido, sino tronar el programa
#El tope de numeros seguidos es de 3
#NO SE PUEDEN REPETIR (V,L,D) (5,50,500)
#SOLO PUEDEN RESTAR: (I,X,C) y UNICAMENTE a los DOS simbolos inmediatamente superiores, por lo
#que estas son las combinaciones de restas posibles permitidas:
#IV
#IX
#XL
#XC
#CD
#CM


#los diccionarios son equivalentes a un objeto de js
def convertir_romano(romano):
    valores_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
#verificamos que el numero introducido tenga caracteres romanos VALIDOS
#por cada caracter de romano, verificamos si ese caracter está presente en el diccionario
    es_valido = all(caracter in valores_romanos for caracter in romano)
    if not es_valido:
        print("Número inválido. Reformula el número romano")
        return
    #el flujo ya no llega aqui si los caracteres no pasan el filtro
    contador=0 #para contar la cantidad de veces que está repitiendose una misma letra
    letra_actual=""
    for i in range(len(romano)): #iterar por cada letra de romano
        letra_actual=romano[i]
        if i<1:
            print("PRIMERA LETRA") 
            contador=contador+1
        else: #a partir de la segunda letra empiezan las evaluaciones aqui
            if contador<3:
                if letra_actual==romano[i-1]: #comprobar si actual es lo mismo que el anteriorj
                    print("REPETIDO DETECTADO"+ romano[i])
                    contador=contador+1
                else:
                    print("No es una letra repetida a la anterior"+romano[i])
                    contador=0
            else:
            #EL FLUJO AVANZA AQUI CUANDO YA HUBO 3 REPETICIONES
                if letra_actual==romano[i-1]:
                    print("ERROR, se ha detectado una cuarta letra repetida")
                    return
                else:
                    print("No es letra repetida, puedes continuar")
                    contador=0

#hay que continuar




        
            
#XXXXMXX   
convertir_romano("IIIXIXIXIXIIII")
    

            

        


