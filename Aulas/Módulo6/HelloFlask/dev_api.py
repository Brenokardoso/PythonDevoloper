from flask import Flask,jsonify,request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        "nome" : "Breno",
        "habilidades" : ["python","sql","flask"]
    },
    {
        "nome" : "Lucas",
        "habilidades" : ["django,javascript","forense"]
    }
]

# Devolve um desenvolvedor pelo ID,tambem altera e deleta o mesmo
@app.route("/dev/<int:id>",methods = ["GET","PUT","DELETE"])
def desenvolvedor(id):
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f"desenvolvidor de id {id} não existe"
            response = {f'"Status":"Falha","Mensagem":{mensagem}'}
        except Exception:
            mensagem = f"desenvolvidor de id {id} não existe"
            response = {f'"Status":"Error","Mensagem":{mensagem}'}

        return jsonify(response)
    
    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({"status":"sucesso","mensagem" : "Registro excluído"})
    
# Lista todos os desenvolvedores e tambem nos permite criar 
@app.route("/dev/",methods = ["POST","GET"])
def lista_desenvolvedores():
    if request.method == "POST":
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({"Status":"Sucesso","Mensagem":"Registro Inserido"})
    elif request.method == "GET": # retona ao meu dicionarío de json's
        return jsonify(desenvolvedores)



if __name__ == "__main__":
    app.run(port = 5547,debug = True)