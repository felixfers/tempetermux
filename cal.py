print("q temperatura tienes ?")
print("1. celsius\n2. fahrenheit\n3. kelvin\n4. salir")

def convertir():
    temperatura = float(input("temperatura: "))



def cf():
    (temperatura * 9/5) + 32

def ck():
    (temperatura + 273.15)

def fc():
    ((temperatura - 32) * 5/9)

def fk():
    ((temperatura - 32) * 5/9 + 273.15)

def kc():
    (temperatura - 273.15)

def kf():
    (temperatura - 273.15) * 9/5 + 32


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
