from flask import Flask, jsonify, request
import pandas as pd
import csv

app = Flask(__name__)


# Dados das cidades
cidades = [
    {"id": 1, "nome": "Rio de Janeiro", "temperatura": 28, "descricao": "Nuvens Dispersas", "umidade": 70},
    {"id": 2, "nome": "São Paulo", "temperatura": 25, "descricao": "Ensolarado", "umidade": 60},
    {"id": 3, "nome": "Belo Horizonte", "temperatura": 30, "descricao": "Chuva", "umidade": 80},
]

# Escrever os dados no arquivo CSV
with open('cidades.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "nome", "temperatura", "descricao", "umidade"])
    writer.writeheader()
    writer.writerows(cidades)

@app.route('/cidades', methods=['GET'])
def obter_cidades():
    return jsonify(cidades)

# Operação GET para obter uma cidade específica
@app.route('/cidades/<int:id>', methods=['GET'])
def obter_cidade(id):
    cidade = next((cidade for cidade in cidades if cidade["id"] == id), None)
    if cidade:
        return jsonify(cidade)
    else:
        return jsonify({"mensagem": "Cidade não encontrada"}), 404

# Operação POST para adicionar uma nova cidade
@app.route('/cidades', methods=['POST'])
def adicionar_cidade():
    nova_cidade = request.json
    nova_cidade["id"] = max(cidade["id"] for cidade in cidades) + 1
    cidades.append(nova_cidade)
    return jsonify(nova_cidade), 201

# Operação PUT para atualizar uma cidade existente
@app.route('/cidades/<int:id>', methods=['PUT'])
def atualizar_cidade(id):
    cidade = next((cidade for cidade in cidades if cidade["id"] == id), None)
    if cidade:
        cidade_atualizada = request.json
        cidade_atualizada["id"] = cidade["id"]
        cidades[cidades.index(cidade)] = cidade_atualizada
        return jsonify(cidade_atualizada)
    else:
        return jsonify({"mensagem": "Cidade não encontrada"}), 404

# Operação DELETE para excluir uma cidade existente
@app.route('/cidades/<int:id>', methods=['DELETE'])
def excluir_cidade(id):
    cidade = next((cidade for cidade in cidades if cidade["id"] == id), None)
    if cidade:
        cidades.remove(cidade)
        return jsonify({"mensagem": "Cidade excluída com sucesso"})
    else:
        return jsonify({"mensagem": "Cidade não encontrada"}), 404

if __name__ == '__main__':
    app.run()
