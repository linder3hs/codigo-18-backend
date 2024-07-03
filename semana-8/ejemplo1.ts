// como tipado implicito
// que TS interpreta el tipo de dato basado en valor
let nombre = "Linder"; // string

// tipado explicito
let direccion: string = "av mi casa 123";

/**
 * Tipos de dato
 * string
 * number
 * boolean
 * object | null
 * undefined
 */

const numero1: number = 100;
const esMayor: boolean = true;
const alumenos: object = [];

function sumar(n1: number, n2: number) {
  return n1 + n2;
}

console.log("Sumando numeros");
console.log(sumar(10, 20));

const sumaDeLosProductosDeHoy: number = 100;
