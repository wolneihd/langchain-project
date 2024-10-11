CREATE DATABASE IF NOT EXISTS aplicacao;
USE aplicacao;
CREATE TABLE IF NOT EXISTS mensagens (
	id INT PRIMARY KEY auto_increment,
    message_id INT NOT NULL,
    user_id INT NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    timestamp_cod INT NOT NULL,
    text_msg VARCHAR(255) NOT NULL    
);
