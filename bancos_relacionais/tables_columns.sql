create table if not exists usuarios (
    id int,
    nome varchar(255) not null, -- nome do usuário
    email varchar(100) not null unique, -- email do usuário
    endereco varchar(50) not null, -- endereço do usuário
    data_nacimento date not null -- data de nascimento do usuário

);

create table if not exists destinos (
    id int,
    nome varchar(255) not null, -- nome do destino
    descricao varchar(300) not null unique -- descricao do destino

);

create table if not exists reservas (
    id int,
    id_usuario int,
    id_destino int,
    data date,
    status varchar(255) default 'pendente' -- confirmado, pendente, cancelado, etc...
);