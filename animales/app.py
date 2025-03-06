from boaconstrictor import BoaConstrictor
from huron import Huron

# Crear instancias de los animales
boa = BoaConstrictor("Serpiente", 12.5, 5, "Brasil", 1.2)
huron = Huron("Rocky", 2.3, 3, "Canadá", 0.8)

# Lista de animales
animales = [boa, huron]

# Función para mostrar información de los animales
def mostrar_informacion(animales):
    for animal in animales:
        print(f"\nNombre: {animal._nombre}")
        print(f"Peso: {animal.obtener_peso()} kg")
        print(f"Edad: {animal.obtener_edad()} años")
        print(f"País de Origen: {animal.obtener_pais_origen()}")
        print(f"Sonido: {animal.hacer_sonido()}")
        
        # Si es una BoaConstrictor, mostrar cuántos ratones ha comido
        if isinstance(animal, BoaConstrictor):
            print(f"Ratones Comidos: {animal.obtener_ratones_comidos()}")
        
        # Mostrar el costo de flete
        print(f"Costo de Flete: {animal.calcular_flete()}")

# Mostrar la información de todos los animales
mostrar_informacion(animales)

# Simular que la boa ha comido algunos ratones
boa.comer_ratón()
boa.comer_ratón()

# Volver a mostrar la información después de que la boa coma ratones
print("\nDespués de que la boa haya comido algunos ratones:")
mostrar_informacion(animales)
