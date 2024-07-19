const express = require("express");
// para poder conectarnos a mongodb vamos a usar mongoose
const mongoose = require("mongoose");
const ubicacionesRouter = require("./routes/ubicacionesRoute");

const app = express();

// Esto se usa para poder un el body JSON de nuestro cliente
app.use(express.json());

app.use("/api/v1", ubicacionesRouter);

// Vamos a conectarnos a la base de datos
mongoose.connect(
  "mongodb://root:root@127.0.0.1:27017/codigo_18_backend?authSource=admin",
  {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  }
);

const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error"));
db.once("open", () => console.log("Connection success"));

app.get("/", function (req, res) {
  res.json({ message: "Hello World" });
});

const PORT = 8000;

app.listen(PORT, function () {
  console.log(`El servidor inicio en http://localhost:${PORT}`);
});
// node app.js
