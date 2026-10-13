CREATE DATABASE IF NOT EXISTS gbg_mexico
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE gbg_mexico;

-- 1. Catalogo de estados
CREATE TABLE IF NOT EXISTS estados (
id_estado INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL UNIQUE
);

-- 2. Catalogo de hospedadores
CREATE TABLE IF NOT EXISTS hospedadores (
id_hospedador INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(30) NOT NULL UNIQUE
);

INSERT IGNORE INTO hospedadores (nombre)
VALUES ('Bovino'), ('Porcino');

-- 3. Datos mensuales importados del Excel
CREATE TABLE IF NOT EXISTS casos_mensuales (
id_registro BIGINT AUTO_INCREMENT PRIMARY KEY,
id_estado INT NOT NULL,
id_hospedador INT NOT NULL,
periodo DATE NOT NULL,


-- Conserva exactamente lo que aparece en Excel
valor_original VARCHAR(20) NOT NULL,

-- Solo se llena cuando la celda contiene un numero
valor_numerico INT NULL,

-- Distingue numeros, guiones y celdas vacias
estado_registro ENUM(
    'numerico',
    'guion',
    'vacio'
) NOT NULL,

fuente_url VARCHAR(500),
fecha_importacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

CONSTRAINT fk_casos_estado
    FOREIGN KEY (id_estado)
    REFERENCES estados(id_estado),

CONSTRAINT fk_casos_hospedador
    FOREIGN KEY (id_hospedador)
    REFERENCES hospedadores(id_hospedador),

CONSTRAINT uq_caso_mensual
    UNIQUE (id_estado, id_hospedador, periodo),

CONSTRAINT chk_valor_no_negativo
    CHECK (valor_numerico IS NULL OR valor_numerico >= 0)


);

-- Indices para consultar por estado y periodo
CREATE INDEX idx_casos_periodo
ON casos_mensuales (periodo);

CREATE INDEX idx_casos_estado_periodo
ON casos_mensuales (id_estado, periodo);
