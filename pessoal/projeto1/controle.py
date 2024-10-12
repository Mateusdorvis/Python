import random
from modelo import GerenciaUsuario
from services import ServicesChat

logo = r'''
                                                   
                                                   
            ,--,                                   
          ,--.'|                                   
          |  | :                __  ,-.            
          :  : '              ,' ,'/ /|            
   ,---.  |  ' |     ,--.--.  '  | |' | ,--.--.    
  /     \ '  | |    /       \ |  |   ,'/       \   
 /    / ' |  | :   .--.  .-. |'  :  / .--.  .-. |  
.    ' /  '  : |__  \__\/: . .|  | '   \__\/: . .  
'   ; :__ |  | '.'| ," .--.; |;  : |   ," .--.; |  
'   | '.'|;  :    ;/  /  ,.  ||  , ;  /  /  ,.  |  
|   :    :|  ,   /;  :   .'   \---'  ;  :   .'   \ 
 \   \  /  ---`-' |  ,     .-./      |  ,     .-./ 
  `----'           `--`---'           `--`---'     
                                                   
'''



           
class Autenticacao:
    def __init__(self):
        self.usuario_logado = False
        self.dados_salvos = {} #dicio que salva os dados temporariomente
        self.resposta_usuario = ['oi', 'oi, tudo bem?', 'olá !', 'olá', 'olá ! como vai você ?']

        self.respostas_tchau = ['Tchau ! Até Mais', 'Tchau !', 'Até !', 'A gente se vê logo  mais ;) !', 'Foi bom falar com você ! Até logo !']

        self.saudacao = ['Olá  😉 !', 'Oi  😉 ! Tudo bem ?', 'Seja bem - vindo (a) !', 'Olá ! Seja bem-vindo(a) 😉 !', 'Tudo bem ?', 'Bem?', 'Qual a boa ?', 'Olá ! Tudo bem ?', 'Suadações 😉 !', 'Como vai ? ', 'Prazer 😉 !']

        self.modelo = GerenciaUsuario()
        self.servico = ServicesChat()
 

   
    def fazer_login(self):
        nome = input('Clara >> Insira seu nome :')
        senha = input ('Clara >> Insira sua senha :')
        if self.modelo.get_user(nome, senha) is True:#se a função retorna True
            print(f'Seja bem -vindo (a) novamente {nome} !')
            self.dados_salvos['Nome'] = nome
            self.dados_salvos['Senha'] = senha
            return True
        else:#se retorna falsa
            return False
        
    def novo_login(self):
        nome = input('Clara >> Insira seu nome :')
        senha = input ('Clara >> Insira sua senha :')
        if self.modelo.post(nome, senha) is True:
            print(f'Seja bem -vindo (a)  {nome} !')
            self.dados_salvos['Nome'] = nome
            self.dados_salvos['Senha'] = senha
            return True
        else:
            return False
        


    def apagar_login(self):
        nome = input('Clara >> Insira seu nome :')
        senha = input ('Clara >> Insira sua senha :')
        self.modelo.delete_conta(nome, senha)
        
    def login(self):
        corYellow = '\033[33m'
        msg=  f'{corYellow} sua assistente virtual  {'\033[0m'}!'
        stop = False
        while True:
            try:
                escolha = int(input(f'''
Clara >> {random.choice(self.saudacao)}  Meu nome é clara e sou {msg} ! Por favor escolha uma opção abaixo :
Opções :
[1] Fazer login,
[2] Realizar novo registro,
[3] Apagar login
[4] Sair do programa,
[5] Acessar serviços disponíveis pela Clara,
[6] Mostrar informações,
[8] Atualizar nome ou senha
Opção escolhida :'''))
                if escolha==1:
                    if self.usuario_logado is False:
                        if self.fazer_login() is False: #se a função retorna falsa 
                            print('Tente novamente')
                            self.usuario_logado = False
                        else:
                            self.usuario_logado = True
                    else:
                      print('Você já está logado !')

                elif escolha==2:
                    if self.usuario_logado is False:
                        if self.novo_login() is False:
                            print('Tente novamente')
                            self.usuario_logado = False
                        else:
                            self.usuario_logado = True
                    else:
                      print('Você já está logado !')
                        

                elif escolha==3:
                    self.apagar_login()

                elif escolha==4:
                    print('Clara >> ', random.choice(self.respostas_tchau))
                    stop = True
                    return stop
                
                
                
                elif escolha==5:
                    if self.usuario_logado is False:
                        print('Clara >> Você não pode acessar esta opção no momento , pois tu não realizaste seu cadastro  !')
                    else:
                        self.servico.servico_escolhido()
                
                elif escolha==6:
                    if self.usuario_logado is False:
                        print('Clara >> Você não pode acessar esta opção no momento , pois tu não realizaste seu cadastro  !')
                    else:
                        self.modelo.show_informations(self.dados_salvos['Nome'], self.dados_salvos['Senha'])

                elif escolha==7:
                        if self.usuario_logado is False:
                            print('Clara >> Você não pode acessar esta opção no momento , pois tu não realizaste seu cadastro  !')
                        else:
                            self.modelo.update_user(self.dados_salvos['Nome'], self.dados_salvos['Senha'], self.dados_salvos)

                else:
                    print('Clara >> Sua opção escolhida não é válida no momento !')

                if stop is True:
                    break
                

                

            except ValueError:
                print('Clara >> OPÇÃO INVÁLIDA !')


   
    def iniciar(self):
            print(logo)
            while True:
                    print('Diga oi a Clara !')
                    prompt = input('Você >> ').lower()

                    if prompt in self.resposta_usuario:
                        if self.login() is True: #se a função retornar true pare imediatamente o loop
                            break
                    else:
                        print('Hum...')
    

if __name__=='__main__':
    chatbot = Autenticacao()
    chatbot.iniciar() 
        

   