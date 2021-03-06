# CASE ITAÚ
- Ambiente desenvolvido para atender a demanda do case do Itaú
- Em anexo nesse repositório, está o arquivo Plano_de_trabalho_App_Proc_Selet_Itau.docx, contendo os detalhes gerenciais do que foi planejado, realizado, os desvios e outras informações. OBS: O conteúdo do arquivo foi escrito no Microsoft Word 2016 

# PRÉ-REQUISITOS
- Ter o Docker-EE ou Docker-CE e Docker-Compose instalado na máquina local para reutilizar esse ambiente.

# . APLICAÇÃO PYTHON PARA COLETA DOS TWEETS 
- Criei uma conta de desenvolvedor no Twitter, para conseguir coletar dados do Twitter através da sua API. Foi preciso aguardar um período, até que terminassem a análise da minha conta e liberassem o acesso a API do Twitter.
- Desenvolvi uma aplicação, onde escolhi a linguagem de programação Python (versão 3), para conectar na API do Twitter e coletar alguns tweets que contenham as seguintes #tags: #openbanking, #apifirst, #devops, #cloudfirst, #microservices, #apigateway,#oauth, #swagger, #raml, #openapis
- Desenvolvi o arquivo app-python-docker-compose.yml, que inicializa o container app-python-coleta-hashtags-twitter para a  aplicação Python, baseado na imagem customizada do arquivo app-python-coleta-hashtags-twitter.dockerfile. Essa aplicação coleta os usuários, quantidade de seguidores, localidade e tweets, que contenham as #tags listadas no tópico anterior. Após a coleta, esse container conecta no banco de dados do MySQL que está em outro container, armazenando as informações coletadas do Twitter.
- Supondo que já tenha clonado e esteja dentro do diretório desse repositório local, seguir os comandos abaixo para inicializar o container da aplicação:
- 1º - docker-compose -f app-python-docker-compose.yml build
- 2º - docker-compose -f app-python-docker-compose.yml up
- OBS: É NECESSÀRIO subir o container do banco de dados primeiro, para conseguir armazenar as informações na tabela Tb_hashtags.
- Caso queira explorar outras opções administrativas do container, além do build e up, analisar as possibilidades executando o comando abaixo:
- docker-compose --help

# . BANCO DE DADOS MYSQL PARA ARMAZENAMENTO DOS TWEETS
- Modelei uma base de dados em um banco de dados, onde eu escolhi para ser o MySQL (versão 5.7.28), para armazenar essas informações e gerar um filtro de determinados tweets
- Desenvolvi o arquivo db-mysql-docker-compose.yml, que inicializa o container db-mysql para o banco de dados MySQL, baseado na imagem já pronta do MySQL na versão 5.7.28. Esse arquivo já cria automaticamente a base de dados DB_HASHTAGS, logando com o usuário root, sem a necessida de digitar a senha.
- Aproveitando que a base de dados DB_HASHTAGS já foi criada automaticamente pelo docker-compose, criei manualmente a tabela Tb_hashtags, onde foi definido as colunas para receber o nome do usuário, quantidade de seguidores, localidade e o texto tweetado.
- Supondo que já tenha clonado e esteja dentro do diretório desse repositório local, seguir os comandos abaixo para inicializar o container do banco de dados.
- 1º - docker-compose -f db-mysql-docker-compose.yml build
- 2º - docker-compose -f db-mysql-docker-compose.yml up
- 3º - docker exec -it db-mysql /bin/bash
- 4º - mysql -u root
- 5º - copiar (CTRL + C) o conteúdo do arquivo script_db_mysql.sql (anexado nesse repositório) e colar (CTRL + V) o conteúdo dentro do terminal do MySQL, e depois digitar ENTER
- Caso queira explorar outras opções administrativas do container, além do build e up, analisar as possibilidades executando o comando abaixo:
- docker-compose --help
- Após todos os tópicos anteriores realizados com sucesso (todos os tópicos dos dois containers), execute os comandos abaixo para filtrar quais são os cinco usuários, da amostra coletada e armazenada, com mais seguidores no Twitter:
- 1º - docker exec -t db-mysql /bin/bash
- 2º - mysql -u root
- 3º - use DB_HASHTAGS;
- 4º - select distinct nome_usuario as 'Nome do Usuario', qtde_seguidor as 'Quantidade de seguidores' from Tb_hashtags order by qtde_seguidor desc limit 5;
