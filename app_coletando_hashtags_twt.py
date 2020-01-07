#importando todos os módulos e objetos da biblioteca TwitterSearch
from TwitterSearch import *
#importando biblioteca para conectar o código Python com o MySQL
import pymysql

#estruturando os códigos de autenticação, busca e exibição das #tags dentro do try
try:
    #credenciais para autenticar no Twitter
    ts = TwitterSearch(
        consumer_key = 'zXNzaCQHg9ZKIu5NF0y7sC606',
        consumer_secret = '2sDZqixtELgsdf1XKCBjem5suCIkNH7fKm02pR0gE2w5e8qyzB',
        access_token = '479795955-YpD8w4322J9OjiUl69IPbAkVZtIJVeP7e7Tzlukv',
        access_token_secret = 'WDV0jijkYAKBw5JRMzkVyxwJzZKAiKSPOrKOeJhnn1YNK'
     )
    #buscando no Twitter as #tags listadas abaixo
    tso = TwitterSearchOrder()
    tso.set_keywords(['#openbanking'])
    tso.set_keywords(['#apifirst'])
    tso.set_keywords(['#devops'])
    tso.set_keywords(['#cloudfirst'])
    tso.set_keywords(['#microservices'])
    tso.set_keywords(['#apigateway'])
    tso.set_keywords(['#oauth'])
    tso.set_keywords(['#swagger'])
    tso.set_keywords(['#raml'])
    tso.set_keywords(['#openapis'])
    
    #percorrendo o resultado, imprimindo o usuário, qtde de seguidores, localização e tweet que contenha algumas das #tags listadas acima
    for tweet in ts.search_tweets_iterable(tso):
        #print( 'Usuário: @%s | Qtde de seguidores: %i | Localização: %s | Tweet: %s' % ( tweet['user']['screen_name'], tweet['user']['followers_count'], tweet['user']['location'], tweet['text'] ) )
        
        #abrindo uma conexão com o banco de dados MySQL que está no container db-mysql
        conexao = pymysql.connect(host='db-mysql', db='DB_HASHTAGS', user='root', passwd='', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

        #criando um cursor
        cursor = conexao.cursor()

        #declarando variáveis que vão receber os campos requisitados no Twitter, para inserir na tabela do banco de dados
        usuario = tweet['user']['screen_name']
        qt_seguidor = tweet['user']['followers_count']
        local = tweet['user']['location']
        twt = tweet['text']

        #inserindo valores na tabela Tb_hashtags do banco de dados DB_HASHTAGS
        cursor.execute("insert into Tb_hashtags (nome_usuario, qtde_seguidor, localizacao, texto_tweet) values(%s, %s, %s, %s)", (usuario, qt_seguidor, local, twt))

        #efetuando um commit no banco de dados
        conexao.commit()

        #finalizando a conexão
        conexao.close()
               
#caso ocorra alguma excessão dos códigos estruturados no try, imprima na tela
except TwitterSearchException as e:
    print(e)