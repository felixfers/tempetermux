

"""
def calculadora():
   
    print("1. Suma\n2. Resta\n3. Multiplicación\n4. División")
    opcion = input("Elige: ")
   
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    
    if opcion == "1":
        print(f"Resultado: {a + b}")
    elif opcion == "2":
        print(f"Resultado: {a - b}")
    elif opcion == "3":
        print(f"Resultado: {a * b}")
    elif opcion == "4":
        if b != 0:
            print(f"Resultado: {a / b}")
        else:
            print("Error: división por cero")

"""
tareas = []

while True:
    print("\n1. Ver tareas\n2. Agregar tarea\n3. Eliminar tarea\n4. Salir")
    op = input("Opción: ")
    
    if op == "1":
        for i, t in enumerate(tareas, 1):
            print(f"{i}. {t}")
    elif op == "2":
        tareas.append(input("Nueva tarea: "))
    elif op == "3":
        if tareas:
            num = int(input("Número a eliminar: ")) - 1
            tareas.pop(num)
    elif op == "4":
        break

"""

if __name__ == "__main__":
    calculadora()
"""


