CREATE TABLE empleados ( 
    id_empleado INTEGER PRIMARY KEY AUTOINCREMENT, 
    nombre TEXT NOT NULL 
);

CREATE TABLE categorias (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_categoria TEXT NOT NULL,
    descripcion TEXT
);

CREATE TABLE productos (
    codigo_producto TEXT PRIMARY KEY,
    nombre_producto TEXT NOT NULL,
    precio REAL NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha_ingreso TEXT NOT NULL,
    marca TEXT NOT NULL,
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

CREATE TABLE usuarios (
    id_usuario TEXT PRIMARY KEY, 
    nombre_completo TEXT NOT NULL, 
    correo_comprador TEXT NOT NULL, 
    fecha_registro TEXT NOT NULL 
);

CREATE TABLE facturas (
    numero_factura TEXT PRIMARY KEY,
    fecha_compra TEXT NOT NULL,
    correo_comprador TEXT NOT NULL,
    monto_total REAL NOT NULL,
    telefono TEXT,
    codigo_cajero TEXT DEFAULT 'N/A',
    id_empleado INTEGER,
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado)
);

CREATE TABLE detalle_factura (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_factura TEXT,
    codigo_producto TEXT,
    cantidad INTEGER NOT NULL,
    FOREIGN KEY (numero_factura) REFERENCES facturas(numero_factura),
    FOREIGN KEY (codigo_producto) REFERENCES productos(codigo_producto)
);

CREATE TABLE carrito_compras(
    id_carrito INTEGER PRIMARY KEY AUTOINCREMENT,
    correo_comprador TEXT NOT NULL,
    codigo_producto TEXT NOT NULL,
    cantidad_unidades INTEGER NOT NULL,
    FOREIGN KEY (codigo_producto) REFERENCES productos(codigo_producto)
);

INSERT INTO categorias (nombre_categoria, descripcion)
VALUES ('Electrónica', 'Dispositivos electrónicos y tecnología');

INSERT INTO categorias (nombre_categoria, descripcion)
VALUES ('Ropa', 'Prendas de vestir');

INSERT INTO categorias (nombre_categoria, descripcion)
VALUES ('Hogar', 'Artículos para el hogar');


INSERT INTO productos (codigo_producto, nombre_producto, precio, cantidad, fecha_ingreso, marca, id_categoria)
VALUES ('P001', 'Laptop HP', 15000.50, 5, '2024-01-10', 'HP', 1);

INSERT INTO productos VALUES ('P002', 'Mouse Inalámbrico', 350.99, 20, '2024-01-12', 'Logitech', 1);
INSERT INTO productos VALUES ('P003', 'Teclado Mecánico', 1200.00, 10, '2024-01-15', 'Redragon', 1);
INSERT INTO productos VALUES ('P004', 'Monitor 24 pulgadas', 3200.75, 8, '2024-01-18', 'Samsung', 1);
INSERT INTO productos VALUES ('P005', 'Impresora Epson', 2800.00, 4, '2024-01-20', 'Epson', 1);
INSERT INTO productos VALUES ('P006', 'Disco Duro 1TB', 950.50, 15, '2024-01-25', 'Seagate', 1);
INSERT INTO productos VALUES ('P007', 'Memoria USB 64GB', 180.00, 30, '2024-01-28', 'Kingston', 1);
INSERT INTO productos VALUES ('P008', 'Silla Gamer', 4500.99, 3, '2024-02-01', 'Razer', 3);
INSERT INTO productos VALUES ('P009', 'Tablet Samsung', 7800.00, 6, '2024-02-05', 'Samsung', 1);
INSERT INTO productos VALUES ('P010', 'Audífonos Bluetooth', 650.40, 12, '2024-02-07', 'Sony', 1);


-- Ver todos los productos
SELECT * FROM productos;

-- Productos con precio mayor a 50000
SELECT * FROM productos
WHERE precio > 50000;

-- 5 productos más caros
SELECT * FROM productos
ORDER BY precio DESC
LIMIT 5;

-- Facturas con teléfono vacío o NULL
SELECT * FROM facturas
WHERE telefono IS NULL OR telefono = '';

-- Buscar factura específica
SELECT * FROM facturas
WHERE numero_factura = 'F001';
