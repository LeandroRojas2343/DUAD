-- ============================================
-- NORMALIZACION DE BASE DE DATOS
-- PROCESO COMPLETO: 1FN → 2FN → 3FN
-- ============================================

-- =========================================================
-- ======================= ORDENES ==========================
-- =========================================================

-- ============================================
-- 1FN: Eliminación de grupos repetidos
-- ============================================

CREATE TABLE ORDENES_1FN (
  OrderID VARCHAR(10),
  CustomerName VARCHAR(100),
  CustomerPhone VARCHAR(20),
  Address VARCHAR(200),
  ItemID VARCHAR(10),
  ItemName VARCHAR(100),
  Price DECIMAL(5,2),
  Quantity INT,
  SpecialRequest VARCHAR(200),
  DeliveryTime TIME,
  PRIMARY KEY (OrderID, ItemID)
);

-- ============================================
-- 2FN: Eliminación de dependencias parciales
-- ============================================

CREATE TABLE ORDENES_2FN (
  OrderID VARCHAR(10) PRIMARY KEY,
  CustomerName VARCHAR(100),
  CustomerPhone VARCHAR(20),
  Address VARCHAR(200),
  DeliveryTime TIME
);

CREATE TABLE ITEMS_2FN (
  ItemID VARCHAR(10) PRIMARY KEY,
  ItemName VARCHAR(100),
  Price DECIMAL(5,2)
);

CREATE TABLE DETALLE_ORDEN_2FN (
  OrderID VARCHAR(10),
  ItemID VARCHAR(10),
  Quantity INT,
  SpecialRequest VARCHAR(200),
  PRIMARY KEY (OrderID, ItemID),
  FOREIGN KEY (OrderID) REFERENCES ORDENES_2FN(OrderID),
  FOREIGN KEY (ItemID) REFERENCES ITEMS_2FN(ItemID)
);

-- ============================================
-- 3FN: Eliminación de dependencias transitivas
-- ============================================

CREATE TABLE CLIENTES_3FN (
  CustomerID INT PRIMARY KEY,
  CustomerName VARCHAR(100),
  CustomerPhone VARCHAR(20)
);

CREATE TABLE DIRECCIONES_3FN (
  AddressID INT PRIMARY KEY,
  Address VARCHAR(200),
  CustomerID INT,
  FOREIGN KEY (CustomerID) REFERENCES CLIENTES_3FN(CustomerID)
);

CREATE TABLE ORDENES_3FN (
  OrderID VARCHAR(10) PRIMARY KEY,
  CustomerID INT,
  AddressID INT,
  DeliveryTime TIME,
  FOREIGN KEY (CustomerID) REFERENCES CLIENTES_3FN(CustomerID),
  FOREIGN KEY (AddressID) REFERENCES DIRECCIONES_3FN(AddressID)
);

CREATE TABLE ITEMS_3FN (
  ItemID VARCHAR(10) PRIMARY KEY,
  ItemName VARCHAR(100),
  Price DECIMAL(5,2)
);

CREATE TABLE DETALLE_ORDEN_3FN (
  OrderID VARCHAR(10),
  ItemID VARCHAR(10),
  Quantity INT,
  SpecialRequest VARCHAR(200),
  PRIMARY KEY (OrderID, ItemID),
  FOREIGN KEY (OrderID) REFERENCES ORDENES_3FN(OrderID),
  FOREIGN KEY (ItemID) REFERENCES ITEMS_3FN(ItemID)
);

-- =========================================================
-- ===================== AUTOMOVILES ========================
-- =========================================================

-- ============================================
-- 1FN: Datos atómicos
-- ============================================

CREATE TABLE AUTOMOVILES_1FN (
  VIN VARCHAR(20),
  Make VARCHAR(50),
  Model VARCHAR(50),
  Year INT,
  Color VARCHAR(30),
  OwnerID INT,
  OwnerName VARCHAR(100),
  OwnerPhone VARCHAR(20),
  InsuranceCompany VARCHAR(100),
  InsurancePolicy VARCHAR(50),
  PRIMARY KEY (VIN, OwnerID)
);

-- ============================================
-- 2FN: Cambio solicitado
-- ============================================

CREATE TABLE VEHICULOS_2FN (
  VIN VARCHAR(20) PRIMARY KEY,
  ModelID INT,
  Year INT,
  Color VARCHAR(30)
);

-- NUEVA TABLA: MODELOS (reutiliza Make/Model)
CREATE TABLE MODELOS_2FN (
  ModelID INT PRIMARY KEY,
  Make VARCHAR(50),
  Model VARCHAR(50)
);

CREATE TABLE PROPIETARIOS_2FN (
  OwnerID INT PRIMARY KEY,
  OwnerName VARCHAR(100),
  OwnerPhone VARCHAR(20)
);

CREATE TABLE VEHICULO_PROPIETARIO_2FN (
  VIN VARCHAR(20),
  OwnerID INT,
  PRIMARY KEY (VIN, OwnerID),
  FOREIGN KEY (VIN) REFERENCES VEHICULOS_2FN(VIN),
  FOREIGN KEY (OwnerID) REFERENCES PROPIETARIOS_2FN(OwnerID)
);

ALTER TABLE VEHICULOS_2FN
ADD FOREIGN KEY (ModelID) REFERENCES MODELOS_2FN(ModelID);

-- ============================================
-- 3FN: Eliminación de dependencias transitivas
-- ============================================

-- NUEVA TABLA: COMPAÑIAS
CREATE TABLE COMPANIAS_SEGURO_3FN (
  CompanyID INT PRIMARY KEY,
  CompanyName VARCHAR(100)
);

-- NUEVA TABLA: TIPOS DE SEGURO
CREATE TABLE TIPOS_SEGURO_3FN (
  PolicyTypeID INT PRIMARY KEY,
  PolicyName VARCHAR(50),
  CompanyID INT,
  FOREIGN KEY (CompanyID) REFERENCES COMPANIAS_SEGURO_3FN(CompanyID)
);

-- TABLA RELACIONAL FINAL
CREATE TABLE VEHICULO_PROPIETARIO_SEGURO_3FN (
  VIN VARCHAR(20),
  OwnerID INT,
  PolicyTypeID INT,
  PRIMARY KEY (VIN, OwnerID, PolicyTypeID),
  FOREIGN KEY (VIN) REFERENCES VEHICULOS_2FN(VIN),
  FOREIGN KEY (OwnerID) REFERENCES PROPIETARIOS_2FN(OwnerID),
  FOREIGN KEY (PolicyTypeID) REFERENCES TIPOS_SEGURO_3FN(PolicyTypeID)
);

-- ============================================
-- FIN DEL PROCESO DE NORMALIZACION
-- ============================================
