// importar express
const express = require("express");

// instanciar express en una variable
const app = express();

// vamos a indicar que nuestro proyecto puede recibir json desde el cliente
app.use(express.json());

// request: donde esta la info que envia el cliente
// response: es lo que usamos para poder responderle al cliente

app.get("/", function (request, response) {
  return response.json({ message: "Hola mundo!" });
});

app.post("/", function (request, response) {
  // si queremos acceder a la info que el cliente esta enviando entonces usamos lo siguiente:
  console.log(request.body);

  return response.json({ message: "observando la info" });
});

app.get("/products", function (request, response) {
  return response.json([
    {
      id: 1,
      title: "Tv 65'",
    },
    {
      id: 2,
      title: "iPhone 14",
    },
  ]);
});

app.listen(9000, function () {
  console.log("El servidor inicio en http://localhost:9000");
});
