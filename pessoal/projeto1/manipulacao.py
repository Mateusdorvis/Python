import os 



class ManipulationArchives:
    def novo_file(self):
        try:
            nome_arquivo = input('Clara >> Digite o nome do arquivo :')
            content = input('Clara >Coloque o conteúdo que queira colocar neste arquivo : ')
            if os.path.exists(f'{nome_arquivo}.txt'):
                print('Clara >> Este arquivo existe !')
                return
            else:
                salvar  = input(f'Clara >> Deseja salvar {nome_arquivo}.txt ? (s/n)  :')
                if salvar=='s':
                    with open(f'{nome_arquivo}.txt', 'w') as arquivo:
                        arquivo.write(content)
                        print('Clara >> Arquivo salvo com sucesso !')
              

        except FileNotFoundError:
            print(f'{'\033[31m'} Clara >> Arquivo não existente ! {'\033[0m'}')


    def editar_conteudo_file(self):
        try:
            nome_arquivo = input('Clara >> digite o nome do arquivo que deseja editar :')
            with open(f'{nome_arquivo}.txt', 'r') as file:
                linhas = file.readlines()
                for indice, cada_linha in enumerate(linhas):
                    print(f'Linha {indice+1} : {cada_linha}')
                try:
                    editar = int(input(f'''Clara >> Deseja editar qual uma das  linhas ?''') )
                    if 1 <= editar <= len(linhas):
                        conteudo = input('')
                        linhas[editar-1] = conteudo+'\n'
                        salvar  = input(f'Clara >> Deseja salvar {nome_arquivo}.txt ? (s/n)  :')
                        if salvar.lower()=='s':
                            with open(f'{nome_arquivo}.txt', 'a') as arquivo:
                                arquivo.writelines(linhas)
                                print('Clara >> Arquivo salvo com sucesso !')
                        

                except ValueError:
                    print(f'{'\033[31m'} Clara >> INVÁLIDO !{'\033[0m'}')

        except FileNotFoundError:
            print(f'{'\033[31m'} Clara >> Arquivo não existente ! {'\033[0m'}')
            

    def ler_texto(self):
        try:
            nome_arquivo = input('Clara >> digite o nome do arquivo que deseja editar :')
            if os.path.exists(f'{nome_arquivo}.txt'):
                with open(f'{nome_arquivo}.txt', 'r') as arquivo:
                    print(f'''
Clara >> Conteúdo do arquivo {nome_arquivo}.txt:
{arquivo.read()}           
''')
                    
            else:
                print(f'{'\033[31m'} Clara >> Este arquivo não existe !{'\033[0m'}')
                    
        except FileExistsError as fe:
            print(f'{'\033[31m'} Clara >> Não foi possível abrir  : {fe} {'\033[0m'} ')

        except FileNotFoundError:
            print(f'{'\033[31m'} Clara >> Error ! {'\033[0m'}')

    def apagar_arquivo(self):
        try:
            nome_arquivo = input('Clara >> digite o nome do arquivo que deseja editar :')
            if os.path.exists(f'{nome_arquivo}.txt'):
                os.remove(f'{nome_arquivo}.txt')
                print(f'Clara >> {nome_arquivo}.txt deletado com sucesso !')

            else:
                print(f'{'\033[31m'} Clara >> Este arquivo não existe  !{'\033[0m'}')
                    
        except FileExistsError as fe:
            print(f'{'\033[31m'} Clara >> Não foi possível abrir  : {fe} {'\033[0m'} ')

        except FileNotFoundError:
            print(f'{'\033[31m'} Clara >> Error ! {'\033[0m'}')
