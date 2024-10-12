from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib.parse
#simulando um banco de dados com dados de usuários fictícios
usuarios = [
    {'Nome': 'Mateus', 'Idade ': 30},
    {'Nome': 'Ana', 'Idade ': 20}
]
#para criar um servidor com http é necessário criar uma classe que herda a classe base...
class ServidorHTTP(BaseHTTPRequestHandler):
    #primeiro é necessário criar a resposta
    def _set_response(self):
        #CRIANDO UMA RESPOSTA HTTP
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    
    #requisições do servidor
    def do_GET(self):
        self._set_response()
        #vai exibir os dados do usuários
        self.wfile.write(json.dumps(usuarios).encode('utf-8'))
    

    def do_POST(self):
        self.content = int(self.headers['Content-Length'])
        post_data = self.rfile.read(self.content).decode('utf-8')

        parsed_data = urllib.parse.parse_qs(post_data)
        nome = parsed_data.get('nome', [None])[0]
        idade = parsed_data.get('idade', [None])[0]
        dado = {'Nome': nome, 'Idade': idade}

        usuarios.append(dado)
        #verifico se o usuário foi adicionado ou não
        for user in usuarios:
            print(user)
        
        #cria uma resposta HTTP com JSON
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        dicio = {'Mensagem de sucesso!': 'Você foi cadastrado com sucesso!'}

        self.wfile.write(json.dumps(dicio).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=ServidorHTTP, port=8085):
    server_addres = ('', port)
    httpd = server_class(server_addres, handler_class)
    print(f'Porta do servidor  {httpd}')
    httpd.serve_forever()

run()