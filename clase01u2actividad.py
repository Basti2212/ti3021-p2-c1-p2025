class Participante:
    def __init__(self, nombre: str, edad: int, numero_inscripcion: int):
        self._nombre: str = nombre 
        self._edad: int = edad 
        self._numero_inscripcion: int = numero_inscripcion 

class Entrenador:
    def __init__(self, especialidad: str,):
        self._especialidad: str = especialidad 

class Atleta:
    def __init__(self, deporte: str, registro_marcas: str, especialidad: str):
        self.__deporte: str = deporte 
        self.__registro_marcas: str = registro_marcas 
        self.__especialidad: str = especialidad

    @property
    def deporte(self):
        return self.__deporte

class Juez:
    def __init__(self, especialidad_juez: str, validar_resultado: int, registro_resultado: str):
        self.__especialidad_juez: str = especialidad_juez 
        self.__registro_resultado: int = registro_resultado 
        self.__validar_resultados: int = validar_resultado 

class Equipo:
    def __init__(self, nombre: str, edad: int, numero_inscripcion: int):
        self._nombre: str = nombre 
        self._edad: int = edad 
        self._numero_inscripcion: int = numero_inscripcion 

class Entrenamiento:
    def __init__(self, nombre: str, edad: int, numero_inscripcion: int):
        self._nombre: str = nombre 
        self._edad: int = edad 
        self._numero_inscripcion: int = numero_inscripcion 
