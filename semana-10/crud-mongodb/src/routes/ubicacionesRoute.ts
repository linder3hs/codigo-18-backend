import { Router } from "express";
import {
  list,
  create,
  deleteId,
  updateId,
} from "../controllers/ubicacionesController";

const router = Router();

router.get("/ubicaciones", list);
router.post("/ubicaciones", create);
router.delete("/ubicaciones/:id", deleteId);
router.put("/ubicaciones/:id", updateId);

export default router;
