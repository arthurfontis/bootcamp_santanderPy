create table usuarios_nova (
    id int,
    nome varchar(255) not null, -- nome do usuário
    email varchar(255) not null unique, -- email do usuário
    data_nascimento date not null, -- data de nascimento do usuário
    endereco varchar(100) not null -- endereço do usuário

);


-- migra dados
INSERT INTO usuarios_nova(id,nome,email,endereco,data_nascimento)
SELECT id,nome,email,endereco,data_nacimento
FROM `usuarios`;

SELECT * FROM usuarios_nova;

-- tabela antiga
--DROP TABLE `usuarios`; 


--ALTER TABLE usuarios_nova RENAME usuarios;

SELECT * FROM `usuarios`;

ALTER TABLE `usuarios` MODIFY COLUMN endereco VARCHAR(150);