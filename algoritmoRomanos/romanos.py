#CONVERTIDOR DE NUMEROS ROMANOS A NUMERICOS
#BUZO ZAMORA ELIAN | 20760257
#DESARROLLO BACKEND I


def convertir_romano(romano):
    
#los diccionarios son equivalentes a un objeto de js
    valores_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    resultado = 0

    
    for i in range(len(romano)):
      
        if i + 1 < len(romano) and valores_romanos[romano[i]] < valores_romanos[romano[i + 1]]:
            resultado -= valores_romanos[romano[i]]
        else:
         
            resultado += valores_romanos[romano[i]]

    return resultado


print(convertir_romano("XIV"))  
print(convertir_romano("IX"))   
print(convertir_romano("MMXXI")) 

            

        


