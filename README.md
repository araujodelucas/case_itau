# Case itaú
Ambiente desenvolvido para atender a demanda do case do Itaú
# . Primeira parte do case - concluída 
- Criei uma conta de desenvolvedor no Twitter, para conseguir coletar dados do Twitter através da sua API. Foi preciso aguardar um período, até que terminassem a análise da minha conta e liberassem o acesso a API do Twitter.
- Desenvolvi uma aplicação, onde escolhi a linguagem de programação Python (versão 3), para conectar na API do Twitter e coletar alguns tweets que contenham as seguintes #tags: #openbanking, #apifirst, #devops, cloudfirst, #microservices, #apigateway,#oauth, #swagger, #raml, #openapis

# . Segunda parte do case - concluída
- Modelar uma base de dados em um banco de dados, onde eu escolhi para ser o MySQL (versão 14.14), para armazenar esses tweets e gerar um filtro de determinados tweets
- Foi criado a base de dados DB_HASHTAGS, e dentro dessa base de dados, a tabela Tb_hashtags, onde foi definido as colunas para receber nome do usuário, quantidade de seguidores, localidade e o texto tweetado.

# OBSERVAÇÃO
- Conforme foi recomendado, a idéia é subir todo o ambiente em Docker, para evitar que seja executado com sucesso na minha máquina, e em outras não. Para agilizar, estou desenvolvendo o ambiente localmente, e irei montar Dockerfile e Docker-Compose para facilitar na reutilização e gerenciamento do ambiente
