#CONVERTIDOR DE NUMEROS ROMANOS A NUMERICOS
#BUZO ZAMORA ELIAN | 20760257
#DESARROLLO BACKEND I


#REGLAS PRINCIPALES A VALIDAR
#Que todo el numero romano contenga un caracter valido, sino tronar el programa
#El tope de numeros seguidos es de 3

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
    else:
            print("Buena pa")

convertir_romano("IVXLCDM")
    

            

        


