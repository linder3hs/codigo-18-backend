"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = require("express");
const bookController_1 = require("../controller/bookController");
const upload_1 = __importDefault(require("../config/upload"));
const router = (0, express_1.Router)();
// recuerden que esto nos va a permitir usar GET, POST, PUT, PATCH y DELETE
router.get("/", bookController_1.getBooks);
router.get("/:id", bookController_1.getBookById);
router.post("/", bookController_1.createBook);
router.put("/:id", bookController_1.updateBook);
router.delete("/:id", bookController_1.deleteBook);
// subir archivos
router.post("/upload", upload_1.default.single("file"), bookController_1.uploadFile);
exports.default = router;
