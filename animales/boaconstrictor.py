from animalexotico import AnimalExotico

class BoaConstrictor(AnimalExotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = 0  # Atributo adicional para contar ratones comidos

    def hacer_sonido(self):
        return "¡Tsss!"  # El sonido característico de la boa

    def comer_ratón(self):
        """Aumenta el contador de ratones que la boa ha comido."""
        self._ratones_comidos += 1

    def obtener_ratones_comidos(self):
        """Devuelve el número total de ratones comidos por la boa."""
        return self._ratones_comidos
