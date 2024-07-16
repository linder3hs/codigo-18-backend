"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
require("dotenv/config");
const express_1 = __importDefault(require("express"));
const homeRouter_1 = __importDefault(require("./routes/homeRouter"));
const bookRouter_1 = __importDefault(require("./routes/bookRouter"));
const app = (0, express_1.default)();
app.use(express_1.default.json());
// v1: version 1
app.use("/api/v1", homeRouter_1.default);
app.use("/api/v1/books", bookRouter_1.default);
app.listen(9000, function () {
    console.log("El servidor inicio en http://localhost:9000");
});
