-- Inserir dados na tabela tiposMensagem
INSERT INTO `tiposMensagem` (tipo) VALUES
('texto'),
('imagem');

-- Inserir dados na tabela usuarios
INSERT INTO `usuarios` (user_id, first_name, last_name) VALUES
(101, 'João', 'Silva'),
(102, 'Maria', 'Oliveira');

-- Inserir dados na tabela mensagens
INSERT INTO `mensagens` (id_tipo_mensagem, usuarios_id, timestamp_cod, text_msg) VALUES
(1, 1, 1631234567, 'Olá, como você está?'),
(2, 1, 1631234590, 'Aqui está uma imagem.');
