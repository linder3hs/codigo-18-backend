import type { Request, Response } from "express";
import Ubicacion from "../models/ubicaciones";

async function list(_req: Request, res: Response) {
  try {
    const ubications = await Ubicacion.find();
    return res.json({
      data: ubications,
    });
  } catch (error: unknown) {
    return res.status(500).json({
      message: error,
    });
  }
}

async function create(req: Request, res: Response) {
  try {
    // recuerden que la informacion que envia el cliente esta
    // en el req.body
    const newUbication = new Ubicacion(req.body);
    await newUbication.save();

    return res.status(201).json({
      message: "ubication created",
    });
  } catch (error: unknown) {
    return res.status(500).json({
      message: error,
    });
  }
}

// Crearemos un endpoint para eliminar un registro especifico
async function deleteId(req: Request, res: Response) {
  try {
    // Debemos de enviar el id
    // api/v1/ubicaciones/669afccf0410834741e2f776
    // Para capturar el valor de la URL lo capturamos con
    // req.params
    // Cuando yo vaya a crear la ruta yo pondre
    // api/v1/ubicaciones/:id
    const { id } = req.params;
    // Siempre va en este orden
    // Modelo.metodo
    await Ubicacion.findByIdAndDelete(id);
    return res.status(201).json({
      message: "Se elimino exitosamente 👍🔥",
    });
  } catch (error: unknown) {
    return res.status(500).json({
      message: error,
    });
  }
}

// Crearemos un endpoint para actualizar la data de mi registro
async function updateId(req: Request, res: Response) {
  try {
    const { id } = req.params;
    const dataRecibida = req.body;

    // findByIdAndUpdate ( 1 "id", 2 "data")
    await Ubicacion.findByIdAndUpdate(id, dataRecibida);
    return res.status(201).send({
      message: "Actualizacion exitosa 🐱‍👤🐱‍💻",
    });
  } catch (error: unknown) {
    return res.status(500).json({
      message: error,
    });
  }
}

export { list, create, deleteId, updateId };
