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
