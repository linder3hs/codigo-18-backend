const express = require("express");
const router = express.Router();
const { list, create, deleteId, updateId } = require("../controllers/ubicacionesController");

router.get("/ubicaciones", list);
router.post("/ubicaciones", create);
router.delete("/ubicaciones/:id", deleteId);
router.put("/ubicaciones/:id", updateId);

module.exports = router;
