from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    texto = "Esse é um teste para um tipo de retorno usando o Flasks"
    return f"{texto}"


if __name__ == "__main__":
    app.run(port = 2222,debug = False) # debug == true -> taxa de atualização do arquivo/programa web em tempo real

