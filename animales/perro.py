class Perro:
    #Constuctor
    #Atributos
    def __init__(self, nombre:str, edad:int, raza:str, peso:float) -> None:
        self.__nombre = nombre
        self._edad = edad
        self.__raza = raza
        self.__peso = peso

    #Metodos
    @staticmethod
    def ladrar()->None:
        print("Guau guau")

    def modificar_peso(self, nuevo_peso:float) -> None:
        if isinstance(nuevo_peso, float):
            self.peso = nuevo_peso

    def traer_peso(self) -> float:
        return self.__peso
    
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre:str) -> str:
        if isinstance(nuevo_nombre, str) and nuevo_nombre != '':
            self.__nombre = nuevo_nombre

    @property
    def raza(self) -> str:
        """ Devuelve el valor del atributo privado 'raza' """
        return self.__raza
    
    @raza.setter
    def raza(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'raza'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.__raza = value
        else:
            raise ValueError('Expected str')

