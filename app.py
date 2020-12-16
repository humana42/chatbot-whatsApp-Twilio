from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
import json

#instacia as bibliotecas
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

#Abre o roteiro de respostas
with open("models/respostas.json", "r") as r:
    roteiro = json.load(r)

#inicia o servidor flask
@app.route("/")
def hello():
    return "O sistema está ok..."

#script de envios e recebimento de mensagens
@app.route("/sms", methods=['POST', 'GET'])
def sms_reply():
    """Responde mensagens no whats app."""
    cont = session.get('contador', 0)
    cont +=0
    if cont == 0:
        response = roteiro['Etapa1']
        resp = MessagingResponse()
        resp.message(str(response))
        cont+=1
        session['contador'] = cont
    else:
        msg = request.form.get('Body')
        preco = 1200
        response = roteiro['Etapa2'].format(msg,preco)
        resp = MessagingResponse()
        resp.message(str(response))
        msg = request.form.get('Body').lower()
        if msg == 'sim' and cont >=1:
            response = roteiro['Etapa3']
            resp = MessagingResponse()
            resp.message(str(response))
            session['contador'] = 0
        elif msg == 'nao':
            response = roteiro['Etapa4']
            resp = MessagingResponse()
            resp.message(str(response))
            session['contador'] = 0

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
