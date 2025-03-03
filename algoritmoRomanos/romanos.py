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
        print("Número inválido. Reformula el número romano");
        return
    #el flujo ya no llega aqui si los caracteres no pasan el filtro
    print("Aqui llega si es un numero valido")

convertir_romano("IVXLCDMeeee")
    

            

        


