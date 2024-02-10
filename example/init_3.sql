-- Crear la tabla
CREATE TABLE ejemplo (
    id SERIAL PRIMARY KEY,
    column1 INT,
    column2 TEXT,
    column3 TIMESTAMP,
    column4 VARCHAR(255),
    column5 BOOLEAN,
    column6 NUMERIC,
    column7 DATE,
    column8 JSONB,
    column9 SMALLINT,
    column10 SMALLINT,
    column11 BIGINT,
    column12 REAL,
    column13 DOUBLE PRECISION,
    column14 CHAR(20),
    column15 VARCHAR(1000),
    column16 TEXT,
    column17 TIMESTAMP WITHOUT TIME ZONE,
    column18 TIMESTAMP WITH TIME ZONE,
    column19 DATE,
    column20 TIME,
    column21 SMALLINT,
    column22 BOOLEAN,
    column23 BIGINT,
    column24 BIGINT,
    column25 MACADDR,
    column26 CIDR,
    column27 INET,
    column28 XML,
    column29 BIGINT,
    column30 POINT
);


-- Generar los datos de prueba
INSERT INTO ejemplo (column1, column2, column3, column4, column5, column6, column7, column8, column9, column10, column11, column12, column13, column14, column15, column16, column17, column18, column19, column20, column21, column22, column23, column24, column25, column26, column27, column28, column29, column30)
SELECT
    random() * 1000,
    'Text ' || i,
    NOW() - INTERVAL '1' YEAR * random(),
    'Some data ' || i,
    CASE WHEN random() < 0.5 THEN TRUE ELSE FALSE END,
    random() * 100,
    CURRENT_DATE - INTERVAL '365' * random(),
    jsonb_build_object('key', 'value' || i),
    random() * 1000,
    random() * 1000,
    random() * 1000000000,
    random() * 1000,
    random() * 1000,
    'Char ' || i,
    'Varchar ' || i,
    'Text ' || i,
    NOW() - INTERVAL '1' YEAR * random(),
    NOW() - INTERVAL '1' YEAR * random(),
    CURRENT_DATE - INTERVAL '365' * random(),
    CURRENT_TIME - INTERVAL '1' HOUR * random(),
    random() * 1000,
    CASE WHEN random() < 0.5 THEN TRUE ELSE FALSE END,
    random() * 1000000000,
    random() * 1000000000,
    '08:00:2b:01:02:03'::macaddr,
    '192.168.1.0/24'::cidr,
    '192.168.1.1'::inet,
    '<root><element>value</element></root>'::xml,
    random() * 1000000000,
    POINT(random() * 180 - 90, random() * 360 - 180)
FROM generate_series(1, 250000) AS i;

SELECT 
    column1, column2, column3, column4, column5, column6, column7, column8, column9, column10, column11, column12, column13, column14, column15, column16, column17, column18, column19, column20, column21, column22, column23, column24, column25, column26, column27, column28, column29, column30
INTO my_table_1
FROM ejemplo;

SELECT 
    column1, column2, column3, column4, column5, column6, column7, column8, column9, column10, column11, column12, column13, column14, column15, column16, column17, column18, column19, column20, column21, column22, column23, column24, column25, column26, column27, column28, column29, column30
INTO my_table_2
FROM ejemplo;

SELECT 
    column1, column2, column3, column4, column5, column6, column7, column8, column9, column10, column11, column12, column13, column14, column15, column16, column17, column18, column19, column20, column21, column22, column23, column24, column25, column26, column27, column28, column29, column30
INTO my_table_3
FROM ejemplo;