CREATE DATABASE IF NOT EXISTS db_feedbacks;

USE db_feedbacks;

CREATE TABLE IF NOT EXISTS tb_comentarios (
	pk_id INT PRIMARY KEY AUTO_INCREMENT,
	usuario VARCHAR(150) NOT NULL,
    texto_comentario TEXT NOT NULL,
    dt DATETIME DEFAULT NOW()
);