class Cliente:
    def __init__(self, nombre, rut, edad):
        self.__nombre: str = nombre
        self.__rut: str = rut
        self.__edad: int = edad

Cliente1: Cliente = Cliente(
    nombre: "Felipe Villarroel",
    rut: "21789567-K",
    edad: "21"
)

print(Cliente1)