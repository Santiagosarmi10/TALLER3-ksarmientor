# Punto 1: Construcción de pruebas para las clases de Hurón y Boa Constrictor

import unittest
from huron import Huron
from boaconstrictor import BoaConstrictor

class TestHuron(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Rocky", 2.3, 3, "Canadá", 0.8)
    
    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")
    
    def test_calcular_flete(self):
        self.assertGreater(self.huron.calcular_flete(), 0)

class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        self.boa = BoaConstrictor("Serpiente", 12.5, 5, "Brasil", 1.2)
    
    def test_hacer_sonido(self):
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")
    
    def test_calcular_flete(self):
        self.assertGreater(self.boa.calcular_flete(), 0)
    
    def test_alimentar(self):
        ratones_iniciales = self.boa._ratones_comidos
        self.boa.comer_ratón()
        self.assertEqual(self.boa._ratones_comidos, ratones_iniciales + 1)

    def test_alimentar_limite(self):
        self.boa._ratones_comidos = 20
        with self.assertRaises(ValueError) as context:
            self.boa.comer_ratón()
        self.assertEqual(str(context.exception), "Demasiados Ratones!")

# Punto 3: Clase Guardería con manejo de errores

class Guarderia:
    def __init__(self):
        self.boas = [BoaConstrictor("Boa1", 10, 4, "Amazonas", 1.0), 
                     BoaConstrictor("Boa2", 12, 5, "Brasil", 1.2)]
        self.hurones = [Huron("Huron1", 2, 3, "Canadá", 0.8), 
                        Huron("Huron2", 2.5, 4, "USA", 0.9)]

    def alimentar_boa(self, boa):
        if boa is None:
            return "Esta Boa no existe!"
        try:
            boa.comer_ratón()
            return "Éxito"
        except ValueError:
            return "La boa está llena"

if __name__ == "__main__":
    unittest.main()
