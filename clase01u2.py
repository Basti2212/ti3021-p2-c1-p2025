class Cliente:
    def __init__(self, nombre, rut, edad):
        self.__nombre: str = nombre
        self.__rut: str = rut
        self.__edad: int = edad
    def __str__(self):
        return f"{self.__nombre} {self.__rut} {self.__edad}"

cliente1: Cliente = Cliente(nombre = "Felipe Villarroel", rut = "21789567-K", edad = 21)

print(cliente1)