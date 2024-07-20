// sera el modelo donde vamos a definir los campos de nuestras colecciones
const mongoose = require("mongoose");

const ubicationSchema = new mongoose.Schema({
  latitude: String,
  longitude: String,
  company: String,
  country: String,
});

module.exports = mongoose.model("ubicaciones", ubicationSchema);
