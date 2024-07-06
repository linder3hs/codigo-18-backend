// importar express
const express = require("express");
const { PrismaClient } = require("@prisma/client");

// instanciar express en una variable
const app = express();
const prisma = new PrismaClient();
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

app.get("/books", async function (req, res) {
  const books = await prisma.book.findMany();

  return res.json({
    books,
  });
});

app.get("/books/:id", async function (req, res) {
  const bookId = Number(req.params.id);
  const book = await prisma.book.findUnique({
    where: {
      id: bookId,
    },
  });

  return res.json({ book });
});

app.post("/books", async function (req, res) {
  const book = req.body;

  const newBook = await prisma.book.create({
    data: {
      title: book.title,
      author: book.author,
      summary: book.summary,
      isbn: book.isbn,
      is_published: book.is_published,
      published_date: new Date(book.published_date),
    },
  });

  return res.json(
    {
      book: newBook,
    },
    201
  );
});

app.put("/books/:id", async function (req, res) {
  const bookUpdated = await prisma.book.update({
    where: {
      id: Number(req.params.id),
    },
    // es la informacion que vamos a actualizar req.body
    data: req.body,
  });

  return res.json({
    book: bookUpdated,
  });
});

app.delete("/books/:id", async function (req, res) {
  const bookDeleted = await prisma.book.delete({
    where: {
      id: Number(req.params.id),
    },
  });

  return res.json({
    book: bookDeleted,
  });
});

app.listen(9000, function () {
  console.log("El servidor inicio en http://localhost:9000");
});
