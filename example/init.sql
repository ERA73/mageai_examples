-- Conectar a la base de datos
\c postgres;

-- Crear una tabla de ejemplo
CREATE TABLE ejemplo (
    id serial PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    salario DECIMAL(10, 2),
    fecha_nacimiento TIMESTAMP,
    correo_electronico VARCHAR(255),
    is_student BOOLEAN
);

-- Insertar algunos registros de ejemplo
INSERT INTO ejemplo (nombre, edad, salario, fecha_nacimiento, correo_electronico, is_student)
VALUES
    ('Juan Pérez', 30, 50000.50, '1992-05-15', 'juan@example.com', false),
    ('María Gómez', 25, 60000.75, '1997-08-22', 'maria@example.com', false),
    ('Carlos Rodríguez', 35, 75000.00, '1987-03-10', 'carlos@example.com', true),
    ('Ana López', 28, 45000.80, '1994-11-18', 'ana@example.com', true),
    ('Pedro Sánchez', 32, 70000.25, '1990-09-25', 'pedro@example.com', false),
    ('Luisa Martínez', 27, 55000.60, '1995-06-30', 'luisa@example.com', true),
    ('Miguel García', 40, 80000.90, '1982-12-05', 'miguel@example.com', false),
    ('Laura Fernández', 22, 40000.45, '2000-02-08', 'laura@example.com', true),
    ('Eduardo Vargas', 38, 90000.70, '1984-07-14', 'eduardo@example.com', false),
    ('Isabel Torres', 29, 60000.30, '1993-04-20', 'isabel@example.com', true),
    (null, null, null, null, null, null);

-- ##########################################################################################
-- ##########################################################################################
-- ##########################################################################################
-- TODO inventar mas errores
-- ##########################################################################################
-- ##########################################################################################
-- ##########################################################################################

-- Consultar los registros insertados
-- SELECT * FROM ejemplo;
