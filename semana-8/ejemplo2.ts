/**
 * En el taller de Santa, los elfos tienen una lista de regalos que desean fabricar
 * y un conjunto limitado de materiales.
 * Los regalos son cadenas de texto (string) y los materiales son caracteres.
 * Tu tarea es escribir una función que, dada una lista de regalos y los
 * materiales disponibles, devuelva una lista de los regalos que se pueden fabricar.
 * Un regalo se puede fabricar si contamos con todos los materiales necesarios
 * para fabricarlo.
 * Ejemplo:
 * 
 * 
  const gifts = ['tren', 'oso', 'pelota']
  const materials = 'tronesa'
 * manufacture(gifts, materials) // ["tren", "oso"]
  'tren' SÍ porque sus letras están en 'tronesa'
  'oso' SÍ porque sus letras están en 'tronesa'
  'pelota' NO porque sus letras NO están en 'tronesa'
 */

/**

function manufacture(gifts: string[], materials: string) {
  const giftsManufactured: string[] = [];

  for (let gift of gifts) {
    let isPosible: boolean = true;

    for (let character of gift) {
      if (materials.split("").includes(character)) {
        isPosible = true;
      } else {
        isPosible = false;
        break;
      }
    }

    if (isPosible) {
      giftsManufactured.push(gift);
    }
  }

  return giftsManufactured;
}

function manufacture(gifts: string[], materiales: string) {
  const giftsManufactured: string[] = [];

  for (let gift of gifts) {
    let isPosible: boolean = true;

    for (let character of gift) {
      if (!materials.split("").includes(character)) {
        isPosible = false;
        break;
      }
    }

    if (isPosible) {
      giftsManufactured.push(gift);
    }
  }

  return giftsManufactured;
}
 */

function manufacture(gifts: string[], materiales: string) {
  const materialesSet: Set<string> = new Set(materiales);
  const giftsManufactured: string[] = [];

  for (let gift of gifts) {
    if (
      gift.split("").every((character: string) => materialesSet.has(character))
    ) {
      giftsManufactured.push(gift);
    }
  }

  return giftsManufactured;
}

const gifts = ["tren", "oso", "pelota"];
const materials = "tronesa";
console.log(manufacture(gifts, materials));
