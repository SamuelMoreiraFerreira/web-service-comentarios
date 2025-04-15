CREATE DATABASE IF NOT EXISTS db_feedbacks;

USE db_feedbacks;

-- TABELA USUÁRIOS

CREATE TABLE IF NOT EXISTS tb_users (
    login VARCHAR(25) PRIMARY KEY,
    password TEXT NOT NULL,
    username VARCHAR(50) NOT NULL,
    salt_password VARCHAR(255) NOT NULL
);

-- TABELA COMENTÁRIOS

CREATE TABLE IF NOT EXISTS tb_comments (
	comment_id INT PRIMARY KEY AUTO_INCREMENT,
	user_login VARCHAR(25) NOT NULL,
    message TEXT NOT NULL,
    date DATETIME DEFAULT NOW(),
    likes INT DEFAULT 0,

    CONSTRAINT tbComments_tbUsers
    FOREIGN KEY (user_login)
    REFERENCES tb_users(login)
);

-- USUÁRIO ADMIN

CREATE USER 'app_prod_user'@'localhost' IDENTIFIED BY 'Xv8#dJ!3r@TqZ1wL9b$P';
GRANT ALL PRIVILEGES ON db_feedbacks.* TO 'app_prod_user'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

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