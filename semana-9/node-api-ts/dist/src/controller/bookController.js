"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.getBooks = getBooks;
exports.getBookById = getBookById;
exports.createBook = createBook;
exports.updateBook = updateBook;
exports.deleteBook = deleteBook;
exports.uploadFile = uploadFile;
const db_1 = __importDefault(require("../utils/db"));
function getBooks(_req, res) {
    return __awaiter(this, void 0, void 0, function* () {
        const books = yield db_1.default.book.findMany();
        return res.json({
            books,
        });
    });
}
function getBookById(req, res) {
    return __awaiter(this, void 0, void 0, function* () {
        // string -> number
        const bookId = Number(req.params.id);
        const book = yield db_1.default.book.findUnique({
            where: {
                id: bookId,
            },
        });
        return res.json({
            book,
        });
    });
}
function createBook(req, res) {
    return __awaiter(this, void 0, void 0, function* () {
        const book = req.body;
        const newBook = yield db_1.default.book.create({
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
    });
}
function updateBook(req, res) {
    return __awaiter(this, void 0, void 0, function* () {
        const bookUpdated = yield db_1.default.book.update({
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
}
function deleteBook(req, res) {
    return __awaiter(this, void 0, void 0, function* () {
        const bookDeleted = yield db_1.default.book.delete({
            where: {
                id: Number(req.params.id),
            },
        });
        return res.json({
            book: bookDeleted,
        });
    });
}
function uploadFile(req, res) {
    if (!req.file) {
        return res.status(400).json({
            message: "No existe un archivo a subir",
        });
    }
    res.json({
        message: "File uploaded",
    });
}
