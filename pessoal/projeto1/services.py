import webbrowser
import datetime
from manipulacao import ManipulationArchives

class ServicesChat:
    def servico_escolhido(self):
        self.sair = False
        while True:
            try:
                escolher = int(input('''
Clara >> Escolha um serviço que deseja :
SERVIÇOS OFERECIDOS:
[1] Mostrar hora e data real,
[2] Abrir uma página web,
[3] Voltar,
[4] Manipulação de arquivos txt,
[5] Calculadora simples
Opção escolhida : '''))
                match escolher:
                    case 1:
                        self.hora()
                    case 2:
                        self.browser()
                    case 3:
                        break
                    case 4:
                        self.arquivs()
                    case 5:
                        self.calculo()
                    case _:
                        print('Clara >> Indisponível no momento !')

                
                    
            except ValueError:
             print('Clara >> Opção indisponível !')

    def hora(self):
        hora  = datetime.datetime.now().replace(microsecond=0)
        hora_formatada = hora.strftime('%d-%m-%Y %H:%M:%S')
        print('Clara >> Data e horário de agora : ', hora_formatada)
    
    def browser(self):
        pagina = input(f' Clara >> digite o nome do site tudo junto que queira abrir :  ').lower()
        if  webbrowser.open(f'www.{pagina}.com'):
           print(f'Clara >> Abrindo a página  {pagina} !')
        else:
            print('Clara >> Não foi possível abrir a página !')

    def arquivs(self):
        while True:
            manipulacao_arquivo = ManipulationArchives()
            try:
                opcao = int(input('''
    Clara >> Escolha um opção :
    [1] Criar um  novo arquivo de texto,
    [2] Ler um arquivo de texto,
    [3] Deletar um  arquivo de texto,
    [4] Editar um arquivo de texto
    [5] Voltar 
    Opção escolhida : '''))
                match opcao:
                    case 1:
                        manipulacao_arquivo.novo_file()
                    case 2:
                        manipulacao_arquivo.ler_texto()
                    case 3:
                        manipulacao_arquivo.apagar_arquivo()
                    case 4:
                        manipulacao_arquivo.editar_conteudo_file()
                    case 5:
                        break

                    case _:
                        print(f'{'\033[31m'} Clara >> Opção indisponível no momento ! {'\033[0m'}')


            except ValueError:
                print(f'{'\033[31m'} Clara >> Inválido ! {'\033[0m'}')

    def calculo(self):
        try:
            print('''
OPERAÇÕES UTILIZADAS :
[+] Adição,
[-] Subtração,
[*] Multiplicação,
[**] Potência
[/] Divisão
''')
            expressao = input('Clara : Faça um cálculo válido :')

            if any(char.isalpha() for char in expressao):#verifica se pelo menos há uma alfabeto
                print('Clara >> Por favor ! Digite uma expressõa válida !')

            else:
              resultado = eval(expressao)
              print('Clara >> O resultado é :', resultado)


        except ValueError:
            print('inválido !')
            
