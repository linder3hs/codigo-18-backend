/**
 * Como tipamos un objeto en TS
 * para ellos tenemos 2 soluciones:
 * 1. Interface: La cual me permite poder definir los atributos del objeto y el tipo de dato
 * de cada atributo
 * 2. Type: Lo mismo que interface
 */

interface Persona {
  nombre: string;
  apellido: string;
  dni: number;
  edad: number;
  direccion?: string;
}

type Persona2 = {
  nombre: string;
  apellido: string;
  dni: number;
  edad: number;
  direccion?: string;
};

const persona: Persona = {
  nombre: "Pepe",
  apellido: "Perez",
  dni: 7273737,
  edad: 86,
  direccion: "av mi casa 123",
};

const persona2: Persona2 = {
  nombre: "Juan",
  apellido: "Perez",
  dni: 88888,
  edad: 29,
};

const listaDePersonas: Persona[] = [
  {
    nombre: "Persona1",
    apellido: "Apellido1",
    dni: 888,
    edad: 19,
  },
  {
    nombre: "Persona2",
    apellido: "Apellido2",
    dni: 9999,
    edad: 101,
  },
];

function saludar(persona: Persona) {
  console.log(
    `Hola me llamo ${persona.nombre} ${persona.apellido} y tengo ${persona.edad} años de edad`
  );
}

saludar(persona);
