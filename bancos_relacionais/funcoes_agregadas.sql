SELECT COUNT(*) AS total_usuarios FROM usuarios;

SELECT COUNT(*) AS total_reservas FROM usuarios u
INNER JOIN reservas r ON u.id = r.id_usuario;


SELECT MAX(TIMESTAMPDIFF(YEAR, data_nascimento, CURDATE())) AS maior_idade FROM usuarios;

