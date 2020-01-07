# Case itaú
Ambiente desenvolvido para atender a demanda do case do Itaú
# . APLICAÇÃO PYTHON PARA COLETA DOS TWEETS 
- Criei uma conta de desenvolvedor no Twitter, para conseguir coletar dados do Twitter através da sua API. Foi preciso aguardar um período, até que terminassem a análise da minha conta e liberassem o acesso a API do Twitter.
- Desenvolvi uma aplicação, onde escolhi a linguagem de programação Python (versão 3), para conectar na API do Twitter e coletar alguns tweets que contenham as seguintes #tags: #openbanking, #apifirst, #devops, cloudfirst, #microservices, #apigateway,#oauth, #swagger, #raml, #openapis
- Desenvolvi o arquivo app-python-docker-compose.yml, que inicializa o container app-python-coleta-hashtags-twitter para a  aplicação Python, baseado na imagem customizada do arquivo app-python-coleta-hashtags-twitter.dockerfile. Essa aplicação coleta os usuários, quantidade de seguidores, localidade e tweets, que contenham as #tags listadas no tópico anterior. Após a coleta, esse container conecta no banco de dados do MySQL que está em outro container, armazenando as informações coletadas do Twitter.
- Seguir os comandos abaixo para inicializar o container dessa aplicação:
- 1º - docker-compose -f app-python-docker-compose.yml build
- 2º - docker-compose -f app-python-docker-compose.yml up
OBS: É NECESSÀRIO subir o container do banco de dados primeiro, para conseguir armazenar as informações na tabela Tb_hashtags.

# . BANCO DE DADOS MYSQL PARA ARMAZENAMENTO DOS TWEETS
- Modelei uma base de dados em um banco de dados, onde eu escolhi para ser o MySQL (versão 5.7.28), para armazenar essas informações e gerar um filtro de determinados tweets
- Desenvolvi o arquivo db-mysql-docker-compose.yml, que inicializa o container db-mysql para o banco de dados MySQL, baseado na imagem já pronta do MySQL na versão 5.7.28. Esse arquivo já cria automaticamente a base de dados DB_HASHTAGS.
- Aproveitando que a base de dados DB_HASHTAGS já foi criada automaticamente pelo docker-compose, criei manualmente a tabela Tb_hashtags, onde foi definido as colunas para receber o nome do usuário, quantidade de seguidores, localidade e o texto tweetado.
- Seguir os comandos abaixo para inicializar o container desse banco de dados.
- 1º - docker-compose -f db-mysql-docker-compose.yml build
- 2º - docker-compose -f db-mysql-docker-compose.yml up
- 3º - docker exec -it db-mysql /bin/bash
- 4º - mysql
- 5º - copiar (CTRL + C) o conteúdo do arquivo script_db_mysql.sql (anexado nesse repositório) e colar (CTRL + V) o conteúdo dentro do terminal do MySQL, e depois digitar ENTER
