import type { Request, Response } from "express";
import prisma from "../utils/db";

async function getBooks(_req: Request, res: Response) {
  const books = await prisma.book.findMany();

  return res.json({
    books,
  });
}

async function getBookById(req: Request, res: Response) {
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

async function createBook(req: Request, res: Response) {
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

async function updateBook(req: Request, res: Response) {
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

async function deleteBook(req: Request, res: Response) {
  const bookDeleted = await prisma.book.delete({
    where: {
      id: Number(req.params.id),
    },
  });

  return res.json({
    book: bookDeleted,
  });
}

export { getBooks, getBookById, createBook, updateBook, deleteBook };
