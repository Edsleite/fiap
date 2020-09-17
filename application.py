from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Hola FIAP! Eduardo Leite - Teste MBA - Modificando o arquivo original</h1>\nMBA! o/"

if __name__ == '__main__':
    # application.run()
    application.run(host='0.0.0.0',debug=True)
