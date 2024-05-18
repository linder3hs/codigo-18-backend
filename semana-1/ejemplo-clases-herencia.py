class Persona:
    def __init__(self, nombre, apellido, altura=None, peso=None, edad=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def saludar(self):
        return f"Hola me llamo {self.nombre} {self.apellido}"


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad_desde_persona, carrera):
        super().__init__(nombre, apellido, edad=edad_desde_persona)
        self.carrera = carrera

    def obtener_carrera(self):
        return f"Hola me llamo {self.nombre} y estudio {self.carrera}"


estudiante1 = Estudiante("Pepe", "Perez", 29, "Ing. Software")
print(estudiante1.saludar())
print(estudiante1.obtener_carrera())
