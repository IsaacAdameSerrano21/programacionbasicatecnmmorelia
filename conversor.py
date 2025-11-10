#  Constantes de conversión
#  En python tal cual no existe una tipo de dato CONSTANTE 
#  por convencion se utiliza nombres en mayuscula para indicar
#  que esa variable debe utilizarse como CONSTANTE
FACTOR_F = 9 / 5
SUMA_F = 32
SUMA_K = 273.15

# Solicitar temperatura en Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Conversión a Fahrenheit y Kelvin
fahrenheit = (celsius * FACTOR_F) + SUMA_F
kelvin = celsius + SUMA_K

# Mostrar resultados con formato
print(f"\nTemperatura en Celsius: {celsius:.2f} °C")
print(f"Temperatura en Fahrenheit: {fahrenheit:.2f} °F")
print(f"Temperatura en Kelvin: {kelvin:.2f} K")
