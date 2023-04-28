function Catalogo() {
  const productos = [
    { id: 1, nombre: "Producto 1", precio: 10 },
    { id: 2, nombre: "Producto 2", precio: 20 },
    { id: 3, nombre: "Producto 3", precio: 30 },
  ];

  return (
    <div>
      <h1>Catálogo de productos</h1>
      <ul>
        {productos.map((producto) => (
          <li key={producto.id}>
            <h2>{producto.nombre}</h2>
            <p>Precio: ${producto.precio}</p>
            <button>Comprar</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Catalogo;