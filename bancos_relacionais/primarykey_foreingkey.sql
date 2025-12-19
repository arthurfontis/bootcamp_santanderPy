ALTER TABLE `usuarios`
MODIFY COLUMN id int AUTO_INCREMENT,
ADD PRIMARY KEY (id);

DESCRIBE `usuarios`;

ALTER TABLE `destinos`
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY(id);

ALTER TABLE `reservas`
MODIFY COLUMN id int AUTO_INCREMENT,
ADD PRIMARY KEY(id);

SELECT * FROM `reservas`;

ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY(id_usuario) REFERENCES usuarios (id);


ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_destinos
FOREIGN KEY(id_destino) REFERENCES destinos (id);


INSERT INTO reservas(id_usuario, id_destino, data)
VALUES(1,6,'2025-12-19');


SHOW CREATE TABLE reservas;






