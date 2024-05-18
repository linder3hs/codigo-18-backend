# El nombre de la clase siempre debe empezar con mayuscula
class Persona:
    """
    Existe una funcion que se ejecuta cuando instanciamos a nuestra clase,
    a esa funcion se le dice constructor, podemos tener mas de 1 y la forma en
    la que se utiliza en python es con el nombre __init__

    Cuando estamos dentro de una clase el primer parametro de TODAS las funciones
    sera self, luego de self podemos colocar los parametros que queramos
    """

    def __init__(self, nombre, apellido, edad, altura, direccion, peso):
        """
        Vamos a agregar propiedades a self y para hacer estos es de la siguiente
        manera

        self.nombre_de_la_propiedad = valor
        """
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.apltura = altura
        self.direccion = direccion
        self.peso = peso

    def saludar(self):
        return f"Hola me llamo {self.nombre} {self.apellido}, tengo {self.edad} años de edad."

    # reto: crear la funcion que retorn la direccion de la persona

    def obtener_direccion(self):
        return f"Mi direccion es: {self.direccion}"


"""
Para poder instanciar una clase, debemos simplemente llamarla por su nombre y
guardarlar en una variable
"""
persona1 = Persona("Pepe", "Perez", 29, 1.94, "av mi casa 123", 85.4)
print(persona1.saludar())
print(persona1.obtener_direccion())
