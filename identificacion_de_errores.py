"""
PROGRAMA A
nombre = input("Tu nombre: ")
edad = input("Tu edad: ")  <--- AQUI ESTA EL ERROR(error de ejecucion o TypeError)
años_futuros = edad + 10  
print(f"En 10 años tendrás {años_futuros} años")
"""
#EL ERROR OCURRE YA QUE NO ESTAMOS 
#DECLARANDO EL TIPO DE VARIABLE(tipo de dato) PARA EDAD 
#SOLUCION
nombre = input("Tu nombre: ")
edad = int(input("Tu edad: "))
años_futuros = edad + 10
print(f"En 10 años tendrás {años_futuros} años")





"""
PROGRAMA B
base = 5
altura = 10
area = (base * altura) / 2
print(f"El área del triángulo es: {área}") <-----AQUI ESTA EL ERROR(Error Sintactico)

"""
#EL ERROR OCURRE YA QUE ESTAMOS USANDO UN LETRA ACENTUADA 
#LO QUE ES DIFERENTE ALA VARIABLE QUE DECLARAMOS ANTES
#SOLUCION
base = 5
altura = 10
area = (base * altura) / 2
print(f"El área del triángulo es: {area}") 




"""
PROGRAMA C
numero = int(input("Ingresa un número: "))
resultado = numero / 0  <-----AQUI ESTA EL ERROR(Error Division Cero)
print(resultado)
"""
#EL ERROR OCURRE YA QUE ESTAMOS DIVIENDO CON CERO
#LO CUAL MATEMATICAMENTE NO ESTA DEFINIDO
#SOLUCION
numero = int(input("Ingresa un número: "))
resultado = numero / 2
print(resultado)
