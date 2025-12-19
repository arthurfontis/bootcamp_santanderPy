INSERT INTO usuarios(id, nome, email, data_nacimento, endereco)
values(1, 'Arthur', 'teste@gmail.com', '2006-07-17', 'Av dos teste 10');


SELECT  * FROM`usuarios`;

UPDATE `usuarios`
SET id = 4
WHERE email = 'teste@gmail.com';