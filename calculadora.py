
# Constantes para mensajes repetitivos
MSG_INGRESA = "Ingresa un número: "
MSG_RES = "Resultado: {}"

# Solicitar dos números
num1 = float(input(MSG_INGRESA))
num2 = float(input(MSG_INGRESA))

# Operaciones
print("\n--- RESULTADOS ---")
#el metodo .format() se utiliza para añadir un valor u otra cadena dentro de una
#ya existente
print(f"{num1} + {num2} = {MSG_RES.format(num1 + num2)}")
print(f"{num1} - {num2} = {MSG_RES.format(num1 - num2)}")
print(f"{num1} * {num2} = {MSG_RES.format(num1 * num2)}")

if num2 != 0:
    #el metodo .round() se utiliza para redondear un numero cierto numero
    #de decimales
    print(f"{num1} / {num2} = {MSG_RES.format(round(num1 / num2, 4))}")
    print(f"{num1} // {num2} = {MSG_RES.format(num1 // num2)}")
    print(f"{num1} % {num2} = {MSG_RES.format(round(num1 % num2, 4))}")
else:
    print("Error: No se puede dividir entre cero.")