class ConvertidorTemperaturas:
    """Clase para convertir entre diferentes escalas de temperatura"""
    
    def __init__(self):
        self.escalas = {
            'C': 'Celsius',
            'F': 'Fahrenheit',
            'K': 'Kelvin',
            'R': 'Rankine'
        }
    
    def celsius_a_fahrenheit(self, celsius):
        """Convierte Celsius a Fahrenheit"""
        return (celsius * 9/5) + 32
    
    def fahrenheit_a_celsius(self, fahrenheit):
        """Convierte Fahrenheit a Celsius"""
        return (fahrenheit - 32) * 5/9
    
    def celsius_a_kelvin(self, celsius):
        """Convierte Celsius a Kelvin"""
        return celsius + 273.15
    
    def kelvin_a_celsius(self, kelvin):
        """Convierte Kelvin a Celsius"""
        return kelvin - 273.15
    
    def fahrenheit_a_kelvin(self, fahrenheit):
        """Convierte Fahrenheit a Kelvin"""
        celsius = self.fahrenheit_a_celsius(fahrenheit)
        return self.celsius_a_kelvin(celsius)
    
    def kelvin_a_fahrenheit(self, kelvin):
        """Convierte Kelvin a Fahrenheit"""
        celsius = self.kelvin_a_celsius(kelvin)
        return self.celsius_a_fahrenheit(celsius)
    
    def celsius_a_rankine(self, celsius):
        """Convierte Celsius a Rankine"""
        return (celsius + 273.15) * 9/5
    
    def rankine_a_celsius(self, rankine):
        """Convierte Rankine a Celsius"""
        return (rankine * 5/9) - 273.15
    
    def convertir(self, valor, escala_origen, escala_destino):
        """
        Convierte un valor de temperatura de una escala a otra
        
        Args:
            valor: Temperatura a convertir
            escala_origen: Escala original ('C', 'F', 'K', 'R')
            escala_destino: Escala destino ('C', 'F', 'K', 'R')
        
        Returns:
            Valor convertido en la escala destino
        """
        # Validar escalas
        escala_origen = escala_origen.upper()
        escala_destino = escala_destino.upper()
        
        if escala_origen not in self.escalas or escala_destino not in self.escalas:
            escalas_validas = ', '.join(self.escalas.keys())
            raise ValueError(f"Escala no válida. Escalas válidas: {escalas_validas}")
        
        # Si es la misma escala, devolver el mismo valor
        if escala_origen == escala_destino:
            return valor
        
        # Diccionario de funciones de conversión
        conversiones = {
            ('C', 'F'): self.celsius_a_fahrenheit,
            ('F', 'C'): self.fahrenheit_a_celsius,
            ('C', 'K'): self.celsius_a_kelvin,
            ('K', 'C'): self.kelvin_a_celsius,
            ('F', 'K'): self.fahrenheit_a_kelvin,
            ('K', 'F'): self.kelvin_a_fahrenheit,
            ('C', 'R'): self.celsius_a_rankine,
            ('R', 'C'): self.rankine_a_celsius,
            ('F', 'R'): lambda x: self.celsius_a_rankine(self.fahrenheit_a_celsius(x)),
            ('R', 'F'): lambda x: self.celsius_a_fahrenheit(self.rankine_a_celsius(x)),
            ('K', 'R'): lambda x: self.celsius_a_rankine(self.kelvin_a_celsius(x)),
            ('R', 'K'): lambda x: self.celsius_a_kelvin(self.rankine_a_celsius(x)),
        }
        
        # Obtener la función de conversión y aplicarla
        funcion = conversiones.get((escala_origen, escala_destino))
        if funcion:
            return funcion(valor)
        else:
            raise ValueError(f"Conversión no implementada de {escala_origen} a {escala_destino}")


def menu_interactivo():
    """Menú interactivo para el usuario"""
    convertidor = ConvertidorTemperaturas()
    
    print("=" * 50)
    print("     CONVERTIDOR DE TEMPERATURAS")
    print("=" * 50)
    
    while True:
        print("\nEscalas disponibles:")
        print("  C - Celsius")
        print("  F - Fahrenheit")
        print("  K - Kelvin")
        print("  R - Rankine")
        print("  S - Salir")
        print("-" * 30)
        
        # Obtener escala de origen
        while True:
            origen = input("Escala de origen (C/F/K/R): ").upper()
            if origen == 'S':
                print("¡Hasta luego!")
                return
            if origen in convertidor.escalas:
                break
            print(f"Escala no válida. Escalas válidas: C, F, K, R")
        
        # Obtener escala destino
        while True:
            destino = input("Escala destino (C/F/K/R): ").upper()
            if destino == 'S':
                print("¡Hasta luego!")
                return
            if destino in convertidor.escalas:
                break
            print(f"Escala no válida. Escalas válidas: C, F, K, R")
        
        # Obtener valor a convertir
        while True:
            try:
                valor_str = input(f"Valor en {convertidor.escalas[origen]}: ")
                valor = float(valor_str)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        # Realizar conversión
        try:
            resultado = convertidor.convertir(valor, origen, destino)
            print(f"\n{valor:.2f}° {convertidor.escalas[origen]} = {resultado:.2f}° {convertidor.escalas[destino]}")
        except Exception as e:
            print(f"Error: {e}")


def ejemplos_de_uso():
    """Muestra ejemplos de uso del convertidor"""
    convertidor = ConvertidorTemperaturas()
    
    print("=== Ejemplos de Conversión ===")
    
    # Ejemplo 1: Celsius a Fahrenheit
    celsius = 25
    fahrenheit = convertidor.celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit:.2f}°F")
    
    # Ejemplo 2: Fahrenheit a Celsius
    fahrenheit = 77
    celsius = convertidor.fahrenheit_a_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius:.2f}°C")
    
    # Ejemplo 3: Celsius a Kelvin
    celsius = 0
    kelvin = convertidor.celsius_a_kelvin(celsius)
    print(f"{celsius}°C = {kelvin:.2f}K")
    
    # Ejemplo 4: Usando el método convertir
    valor = 100
    resultado = convertidor.convertir(valor, 'C', 'F')
    print(f"{valor}°C = {resultado:.2f}°F (usando método convertir)")
    
    valor = 212
    resultado = convertidor.convertir(valor, 'F', 'K')
    print(f"{valor}°F = {resultado:.2f}K (usando método convertir)")


def tabla_de_conversion():
    """Muestra una tabla de conversión de temperaturas"""
    convertidor = ConvertidorTemperaturas()
    
    print("\n=== Tabla de Conversión Celsius ↔ Fahrenheit ===")
    print("Celsius    Fahrenheit")
    print("-" * 25)
    
    for celsius in range(-10, 41, 10):
        fahrenheit = convertidor.celsius_a_fahrenheit(celsius)
        print(f"{celsius:7}°C    {fahrenheit:10.2f}°F")
    
    print("\nPuntos de referencia importantes:")
    puntos = [
        ("Punto de congelación del agua", 0, 'C'),
        ("Punto de ebullición del agua", 100, 'C'),
        ("Temperatura corporal humana", 37, 'C'),
        ("Cero absoluto", 0, 'K')
    ]
    
    for nombre, valor, escala in puntos:
        if escala == 'C':
            f = convertidor.convertir(valor, 'C', 'F')
            k = convertidor.convertir(valor, 'C', 'K')
            print(f"\n{nombre}:")
            print(f"  {valor}°C = {f:.2f}°F = {k:.2f}K")
        elif escala == 'K':
            c = convertidor.convertir(valor, 'K', 'C')
            f = convertidor.convertir(valor, 'K', 'F')
            print(f"\n{nombre}:")
            print(f"  {valor}K = {c:.2f}°C = {f:.2f}°F")


if __name__ == "__main__":
    # Mostrar ejemplos
    ejemplos_de_uso()
    
    # Mostrar tabla de conversión
    tabla_de_conversion()
    
    # Ejecutar menú interactivo
    print("\n" + "=" * 50)
    print("Ahora puedes usar el convertidor interactivo")
    print("=" * 50)
    
    menu_interactivo()
