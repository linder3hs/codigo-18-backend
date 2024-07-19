const Ubicacion = require("../models/ubicaciones");

async function list(_req, res) {
  try {
    const ubications = await Ubicacion.find();
    return res.json({
      data: ubications,
    });
  } catch (error) {
    return res.status(500).json({
      message: error.message,
    });
  }
}

async function create(req, res) {
  try {
    // recuerden que la informacion que envia el cliente esta
    // en el req.body
    const newUbication = new Ubicacion(req.body);
    await newUbication.save();

    return res.status(201).json({
      message: "ubication created",
    });
  } catch (error) {
    return res.status(500).json({
      message: error.message,
    });
  }
}

module.exports = { list };
