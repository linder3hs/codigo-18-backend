"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = require("express");
const homeController_1 = require("../controller/homeController");
const router = (0, express_1.Router)();
router.get("/", homeController_1.index);
router.get("/products", homeController_1.getProducts);
router.post("/products", homeController_1.createProduct);
exports.default = router;
