# Pasos para iniciar un proyecto con Node y Experss

## Paso 1

Primero debemos crear nuestro archivo `package.json` y para ellos usamos el siguiente comando:

```bash
npm init

# preguntas que nos hacen para crear el proyecto
package name: (api) node-api
version: (1.0.0)
description: Mi primera API con NodeJS
entry point: (index.js) app.js
test command:
git repository:
keywords: API, Node
author: Linder Hassinger
license: (ISC) MIT
```

## Paso 2

Ahora vamos a instalar `express` con el siguiente comando:

```bash
npm install express
```

## Paso 3

Abrimos `vscode` y verificamos que la carpeta `node_modules` se haya creado y que el archivo `package.json` este completo.

## Paso 4

Creamos el archivo `.gitignore` y agregamos la carpeta `node_module`, esto sirve para evitar que dicha carpeta se suba a `github`, debido a que esta carpeta es muy pesada.

## Paso 5

Creamos el archivo `app.js` y empezamos a codear!!!
