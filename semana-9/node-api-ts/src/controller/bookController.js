const prisma = require("../utils/db");

async function getBooks(req, res) {
  const books = await prisma.book.findMany();

  return res.json({
    books,
  });
}

async function getBookById(req, res) {
  // string -> number
  const bookId = Number(req.params.id);

  const book = await prisma.book.findUnique({
    where: {
      id: bookId,
    },
  });

  return res.json({
    book,
  });
}

async function createBook(req, res) {
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

  return res.status(201).json({
    book: newBook,
  });
}

async function updateBook(req, res) {
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
}

async function deleteBook(req, res) {
  const bookDeleted = await prisma.book.delete({
    where: {
      id: Number(req.params.id),
    },
  });

  return res.json({
    book: bookDeleted,
  });
}

module.exports = { getBooks, getBookById, createBook, updateBook, deleteBook };
