/*usando base dados criada*/
USE DB_HASHTAGS;

/*criando tabela para receber os tweets*/
CREATE TABLE Tb_hashtags (nome_usuario VARCHAR(30) NOT NULL, qtde_seguidor INT NOT NULL, localizacao VARCHAR(30), texto_tweet TEXT NOT NULL);

/*configurando a base de dados e a tabela, aceitando receber caracteres utf8*/
ALTER DATABASE DB_HASHTAGS CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE Tb_hashtags CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;