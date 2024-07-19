const express = require("express");
const router = express.Router();
const { list, create } = require("../controllers/ubicacionesController");

router.get("/ubicaciones", list);
router.post("/ubicaciones", create);

module.exports = router;
