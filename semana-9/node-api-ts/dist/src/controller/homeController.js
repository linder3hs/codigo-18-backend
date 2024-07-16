"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.index = index;
exports.createProduct = createProduct;
exports.getProducts = getProducts;
function index(_req, res) {
    return res.json({ message: "Hola mundo!" });
}
function createProduct(req, res) {
    console.log(req.body);
    return res.json({ message: "observando la info" });
}
function getProducts(_req, res) {
    return res.json([
        {
            id: 1,
            title: "Tv 65'",
        },
        {
            id: 2,
            title: "iPhone 14",
        },
    ]);
}
