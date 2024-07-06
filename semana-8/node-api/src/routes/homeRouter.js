const express = require("express");
const {
  index,
  getProducts,
  createProduct,
} = require("../controller/homeController");

const router = express.Router();

router.get("/", index);
router.get("/products", getProducts);
router.post("/products", createProduct);

module.exports = router;
