import express from "express";
import homeRouter from "./routes/homeRouter";
import bookRouter from "./routes/bookRouter";

const app = express();

app.use(express.json());

// v1: version 1
app.use("/api/v1", homeRouter);
app.use("/api/v1/books", bookRouter);

app.listen(9000, function () {
  console.log("El servidor inicio en http://localhost:9000");
});
