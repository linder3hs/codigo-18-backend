const express = require("express");
const { index } = require("../controller/homeController");

const router = express.Router();

router.get("/", index);

export default router;
