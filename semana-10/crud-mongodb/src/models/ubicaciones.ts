// sera el modelo donde vamos a definir los campos de nuestras colecciones
import { Schema, model } from "mongoose";

const ubicationSchema = new Schema({
  latitude: String,
  longitude: String,
  company: String,
  country: String,
});

export default model("ubicaciones", ubicationSchema);
