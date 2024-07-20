import express, {
  type Application,
  type Request,
  type Response,
} from "express";
import mongoose from "mongoose";
import ubicacionesRouter from "./routes/ubicacionesRoute";

const app: Application = express();

// Esto se usa para poder un el body JSON de nuestro cliente
app.use(express.json());

app.use("/api/v1", ubicacionesRouter);

// Vamos a conectarnos a la base de datos
mongoose.connect(
  "mongodb://root:root@127.0.0.1:27017/codigo_18_backend?authSource=admin"
);

const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error"));
db.once("open", () => console.log("Connection success"));

app.get("/", function (_req: Request, res: Response) {
  res.json({ message: "Hello World" });
});

const PORT = 8000;

app.listen(PORT, function () {
  console.log(`El servidor inicio en http://localhost:${PORT}`);
});
// node app.js
