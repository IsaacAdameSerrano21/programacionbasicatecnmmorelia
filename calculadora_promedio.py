print("=== CALCULADORA DE PROMEDIO ===")

# Solicitar datos
nombre = input("Nombre del estudiante: ")
c1 = float(input("Calificación 1: "))
c2 = float(input("Calificación 2: "))
c3 = float(input("Calificación 3: "))

# Calcular promedio
promedio = (c1 + c2 + c3) / 3

# Determinar si aprobó
if promedio >= 6.0:
    estado = "APROBADO"
else:
    estado = "NO APROBADO"

# Mostrar reporte
print("\n=== REPORTE DE CALIFICACIONES ===")
print(f"Estudiante: {nombre}")
print(f"Calificación 1: {c1}")
print(f"Calificación 2: {c2}")
print(f"Calificación 3: {c3}")
print(f"Promedio: {promedio:.2f}")
print(f"Estado: {estado}")
