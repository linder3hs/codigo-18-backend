class Persona:
    def __init__(self, nombre, apellido, altura=None, peso=None, edad=None):
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def saludar(self):
        return f"Hola me llamo {self.__nombre} {self.apellido}"

    # setter
    def modificar_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # getter
    def obtener_nombre(self):
        return self.__nombre


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad_desde_persona, carrera):
        super().__init__(nombre, apellido, edad=edad_desde_persona)
        self.carrera = carrera

    def obtener_carrera(self):
        return f"Hola me llamo {self.obtener_nombre()} y estudio {self.carrera}"


estudiante1 = Estudiante("Pepe", "Perez", 29, "Ing. Software")
estudiante1.modificar_nombre("Pepe2")
print(estudiante1.saludar())
print(estudiante1.obtener_carrera())
