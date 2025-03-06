from iAnimal import iAnimal

class Animal(iAnimal):
    def __init__(self, nombre: str, peso: float, edad: int):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos = 0  # Se cambia el nombre para evitar conflictos
    
    def comer(self, kilos: float):
        """Aumenta la cantidad de kilos de comida consumidos por el animal."""
        self._kilos_comidos += kilos
        
    def obtener_kilos_comidos(self) -> float:
        """Devuelve la cantidad total de kilos de comida consumidos."""
        return self._kilos_comidos  # Ahora accede a la variable correcta
    
    def hacer_sonido(self):
        """Método que será sobrescrito por las clases hijas."""
        pass
    
    def obtener_peso(self) -> float:
        """Devuelve el peso del animal."""
        return self._peso
    
    def obtener_edad(self) -> int:
        """Devuelve la edad del animal."""
        return self._edad
