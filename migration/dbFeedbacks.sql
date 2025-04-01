CREATE DATABASE IF NOT EXISTS db_feedbacks;

USE db_feedbacks;

-- TABELA USUÁRIOS

CREATE TABLE IF NOT EXISTS tb_users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    login VARCHAR(25) NOT NULL,
    password TEXT NOT NULL,
    salt_password VARCHAR(255) NOT NULL
);

-- TABELA COMENTÁRIOS

CREATE TABLE IF NOT EXISTS tb_comments (
	comment_id INT PRIMARY KEY AUTO_INCREMENT,
	user_id INT NOT NULL,
    message TEXT NOT NULL,
    dt DATETIME DEFAULT NOW(),
    likes INT DEFAULT 0,

    CONSTRAINT tbComments_tbUsers
    FOREIGN KEY (user_id)
    REFERENCES tb_users(user_id)
);

-- TRIGGER CRIPTOGRAFIA

DELIMITER $$

CREATE TRIGGER tg_tbUsers_Insert 
BEFORE INSERT
ON tb_users
FOR EACH ROW
BEGIN

    SET NEW.salt_password = UUID();

    SET NEW.password = SHA2(CONCAT(NEW.password, NEW.salt_password), 256);

END $$

DELIMITER ;