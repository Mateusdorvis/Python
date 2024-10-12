from flask import Flask, request, jsonify, render_template
from datetime import datetime


app = Flask(__name__, template_folder='template')

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    vocabulario_ois = ['oi','oi?', 'olá', 'olá', 'oi, tudo bem ?', 'olá, tudo bem?' , 'opa', 'opa, como vai?']
    vocabulario_palavrao = ['puta','vagabunda', 'piranha', 'filha da puta', 'prostituta' , 'cadela', 'vadia', 'promiscua']
    mensagem_user = request.form['msg']
    resposta = 'Peço-lhe desculpas ! Podes repetir ? Pois não a entendi.  '
    for cada_oi in vocabulario_ois:
        if mensagem_user.lower().startswith(cada_oi) or mensagem_user.lower().endswith(cada_oi):
            resposta = ' Olá ! Meu nome é Ana e sou sua assistente virtual ! O que você deseja ?'
            break #break evita que gere um loop infinito
    
    for cada_palavra in vocabulario_palavrao:
        if mensagem_user.lower().startswith(cada_palavra) or mensagem_user.lower().endswith(cada_palavra):
            resposta = ' Não fale assim comigo, ok?'
            break
    
    return jsonify({'RespostaUser': f'Mensagem de usuário enviada  às  {datetime.now().replace(microsecond=0)} : {mensagem_user}', 'RespostaChat' : f'Mensagem da Ana (assistente) enviada  às  {datetime.now().replace(microsecond=0)} : {resposta} ?'})#qubra a linha a cada envio da mensagem
    
    
app.run(debug=True)