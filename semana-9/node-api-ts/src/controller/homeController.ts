import type { Request, Response } from "express";

function index(_req: Request, res: Response) {
  return res.json({ message: "Hola mundo!" });
}

function createProduct(req: Request, res: Response) {
  console.log(req.body);
  return res.json({ message: "observando la info" });
}

function getProducts(_req: Request, res: Response) {
  return res.json([
    {
      id: 1,
      title: "Tv 65'",
    },
    {
      id: 2,
      title: "iPhone 14",
    },
  ]);
}

export { index, createProduct, getProducts };
