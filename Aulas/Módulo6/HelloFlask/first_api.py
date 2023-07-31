from flask import Flask,jsonify,request
import json

app = Flask(__name__)

@app.route('/<id>')
def pessoa(id):
    return jsonify({f"{id}:Nome":"Breno"},{f"{id}:Nome" : "Raysa" },{"Idade":22},{"Idade":32},{"sexo" : "M"},{"sexo" : "F"})

# @app.route("/soma/<int:valor_1>/<int:valor_2>")
# def soma(valor_1,valor_2):
#     return jsonify(f"'soma': {valor_1  +valor_2}")

@app.route("/soma",methods = ["POST","GET"])
def soma():
    if request.method == "POST":
        dados = json.loads(request.data)
        soma_total = sum(dados["valores"])
        print(f"{soma_total}")

    elif request.method == "GET":
        soma_total = int(12 + 43)
    
    return jsonify(f"'soma': {soma_total} ")

if __name__ == "__main__":
    app.run(port = 5565,debug = True)