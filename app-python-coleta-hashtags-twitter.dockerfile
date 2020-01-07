#utilizand como base a imagem do Python na versão 3 
FROM python:3

#responsável por manter a imagem
MAINTAINER Lucas de Araujo (lucasdearaujo.trabalho@gmail.com)

#copiando a aplicação Python do diretório atual da máquina, para o diretório /tmp do container
COPY ./app_coletando_hashtags_twt.py /tmp

#diretório de trabalho (inicial) do container
WORKDIR /tmp

#atualizando os pacotes do container e instalando bibliotecas que serão utilizadas pela a aplicação Python, através do gerenciador de pacotes do Python (pip)
RUN apt-get update && pip install TwitterSearch && pip install pymysql

#comando inicial do container para inserir os tweets coletados no db-mysql
ENTRYPOINT [ "python3", "app_coletando_hashtags_twt.py" ]