#importando todos os módulos e objetos da biblioteca TwitterSearch
from TwitterSearch import *

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
    tso.set_keywords(['cloudfirst'])
    tso.set_keywords(['#microservices'])
    tso.set_keywords(['#apigateway'])
    tso.set_keywords(['#oauth'])
    tso.set_keywords(['#swagger'])
    tso.set_keywords(['#raml'])
    tso.set_keywords(['#openapis'])
    
    #percorrendo o resultado, imprimindo o usuário, qtde de seguidores, localização e tweet que contenha algumas das #tags listadas acima
    for tweet in ts.search_tweets_iterable(tso):
        print( 'Usuário: @%s | Qtde de seguidores: %s | Localização: %s | Tweet: %s' % ( tweet['user']['screen_name'], tweet['user']['followers_count'], tweet['user']['location'], tweet['text'] ) )

#caso ocorra alguma excessão dos códigos estruturados no try, imprima na tela
except TwitterSearchException as e:
    print(e)