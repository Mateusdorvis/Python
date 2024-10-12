from flask import Flask, request, render_template, make_response

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')#primeiramente redenriza para a página html normal

@app.route('/cookie_definido') #a rota url será a função abaixo
def cookie_definido(): #esta função serve para definir um cookie padrão
    mensagem_http = make_response('Você pegou este cookie !') #instanciando a função make_response que cria uma mensagem para o navegador ou seja , cria uma mensgame para o usuário como esta
    mensagem_http.set_cookie('cookie_padrao', '10101010101') #este método serve para definir um cookie padrão, 'cookie_padrao' é nome do cookie definido w 101010101 é o valor do cookie definido, OBRIGATORIAMENTE É PRECISO QUE O VALOR DO COOKIE SEJA STRING
    return mensagem_http #vai retornar o valor do cookie 'cookie_padrao'

@app.route('/pegar_cookie') #a rota será a função pegar_cookie 
def pegar_cookie():
    cookie_padrao = request.cookies.get('cookie_padrao') #no caso vai pegar o valor do 'cookie_padrao'
    if cookie_padrao:
        return f'O valor padrão do seu cookie é este : {cookie_padrao}.'
    else:
        return 'Sem cookies ainda !'
    
@app.route('/cookie_removido')
def cookie_removido():
    reposta_http = make_response('Este coookie foi deletado navegador, salve esta informação !')#estou enviado uma notifiação ao navegador que vai na página
    reposta_http.set_cookie('cookie_padrao', '', expires=0)
    return reposta_http

app.run(debug=True) #ativando o servidor Flask no modo debug....