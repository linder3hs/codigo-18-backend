import { Router } from "express";
import {
  index,
  getProducts,
  createProduct,
} from "../controller/homeController";

const router = Router();

router.get("/", index);
router.get("/products", getProducts);
router.post("/products", createProduct);

export default router;
