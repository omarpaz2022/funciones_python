# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

def imprimir_mayor(numero_1, numero_2):
    print("Funcion imprimir mayor")
    # En esta función debe determinar cual de los dos
    # números ingresados por parámetro es mayor
    # y luego imprimir dicho valor
    
    
    if numero_2 > numero_1:
        numero_mayor = numero_2 
    else:
        numero_mayor = numero_1
    return numero_mayor          


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Complete la función "imprimir_mayor" 
    
    retorno = imprimir_mayor(10, 2)
    print(retorno) 
    print("terminamos")