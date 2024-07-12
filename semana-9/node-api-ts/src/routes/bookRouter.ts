import { Router } from "express";
import {
  getBooks,
  getBookById,
  createBook,
  updateBook,
  deleteBook,
  uploadFile,
} from "../controller/bookController";
import upload from "../config/upload";

const router = Router();
// recuerden que esto nos va a permitir usar GET, POST, PUT, PATCH y DELETE

router.get("/", getBooks);
router.get("/:id", getBookById);
router.post("/", createBook);
router.put("/:id", updateBook);
router.delete("/:id", deleteBook);
// subir archivos
router.post("/upload", upload.single("file"), uploadFile);

export default router;
