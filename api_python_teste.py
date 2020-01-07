#!/usr/bin/python3
#importando módulos da biblioteca flask
from flask import Flask, jsonify, request

app = Flask(__name__)

#criando lista
devs = [
	{   
        'id': 1,
		'name': 'Lucas de Araújo',
		'lang':	'Python'

	},
    {   
        'id': 2,
		'name': 'Jubileu Serafim',
		'lang':	'Python'

	},
    {   
        'id': 3,
		'name': 'Aristoteles Bartolomeu',
		'lang':	'Python'

	},
    {   
        'id': 4,
        'name': 'Joãozinho Batoré',
        'lang': 'NodeJS'
    }
]

#obs: não é necessário usar o método GEt, pois o mesmo já é o padrão de uma rota
#criando rota / endpoint da API
@app.route('/devs', methods=['GET'])
#criando função para retornar a lista
def home():
	return jsonify(devs), 200

#criando nova rota para filtrar os devs pela a linguagem. Caso não seja localizado nenhum objeto da lista que atende a esse filtro, não retornará nada
@app.route('/devs/<string:lang>', methods=['GET'])
#criando função para percorrer a lista e retornar o filtro definido
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_per_lang), 200

#alterando via PUT
@app.route('/devs/<int:id>', methods=['PUT'])
def change_lang(id):
    for dev in devs:
        if dev['id'] == id
            dev['lang'] = request.get_json().get('lang')

            return jsonify(dev), 200
    return jsonify({'error': 'dev not found'}), 404

#criando rota para filtrar a lista pelo o id do dev
@app.route('/devs/<int:id>', methods=['GET'])
#criando função para percorrer a lista, procurando pelo o id
#caso o parametro passado na função não seja igual o id do dev, retornar uma mensagem de erro
def devs_per_id(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200
    
    return jsonify({'error': 'not found'}), 404

#criando rota (endpoint) para add novo dev
@app.route('/dev', methods=['POST'])
def save_dev():
    data = request.get_json()
    #dando append para salvar em memória o dev recebido
    devs.append(data)
    return jsonify(data), 201
    
#deletando valores
@app.route('/devs/<int:id>', methods=['DELETE'])
def remove_dev(id):
    index = id - 1
    del devs[index]

    return jsonify({'message': 'Dev is no longer alive'}), 200

#ativando o modó debug na execução
if __name__ == '__main__':
	app.run(debug=True)

#executar a app .py no terminal