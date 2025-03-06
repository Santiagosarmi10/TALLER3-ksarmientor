from animal import Animal

class AnimalExotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad)  # Llamamos al constructor de Animal
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    def calcular_flete(self) -> float:
        """Calcula el costo de importar el animal basado en su peso e impuestos."""
        return self._impuestos * self._peso

    def hacer_sonido(self):
        """Método que será sobrescrito por las clases hijas."""
        return "Sonido de animal exótico"
    
    def obtener_pais_origen(self) -> str:
        """Devuelve el país de origen del animal exótico."""
        return self._pais_origen
