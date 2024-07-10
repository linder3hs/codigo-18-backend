function index(req, res) {
  return res.json({ message: "Hola mundo!" });
}

function createProduct(req, res) {
  console.log(request.body);

  return response.json({ message: "observando la info" });
}

function getProducts(req, res) {
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

// export
module.exports = { index, createProduct, getProducts };
