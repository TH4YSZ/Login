create database login;

use login;

create table usuarios(
	id int(3) primary key auto_increment,
    nome varchar(20),
    email varchar(50),
    senha varchar(8)
);

insert into usuarios(nome, email, senha) values
('Administrador', 'admin@example.com', 'admin123'),
('Usuario1', 'usuario1@example.com', 'senha123'),
('Usuario2', 'usuario2@example.com', 'senha456');
