#from flask import Flask
#from flask import *
#from app import app
#from flaskext.mysql import MySQL
#import pymysql
#from db_config import mysql
#from flask import jsonify
#from flask import flash, request
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

#mysql = MySQL()
mysql = ""

#MySQL configurations
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='DB_HASHTAGS'
app.config['MYSQL_DATABASE_HOST']='db-mysql'
mysql.init_app(app)

@app.route('/qtde_seguidores', methods=['GET'])
def qtde_seguidores():
    try:
        conexao = mysql.connect()
        cursor = conexao.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select distinct nome_usuario as 'Nome do Usuario', qtde_seguidor as 'Quantidade de seguidores' from Tb_hashtags order by qtde_seguidor desc limit 5;")
        rows=cursor.fetchall()
        resp=jsonify(rows)
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conexao.close()
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()
