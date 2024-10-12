from rich.table import Table
from rich.console import Console
from rich  import print
#construindo uma tabela com a biblioteca rich
terminal = Console() #incia o console
def tabela():
    #criando colunas 
    tabela_usuarios = Table()
    tabela_usuarios.add_column('Nome')
    tabela_usuarios.add_column('Idade')
    tabela_usuarios.add_column('Senha')
    #adicionado
    lista = [
        {'Nome': 'Mateus', 'Idade': 19, 'Senha': 'asasasa'},
        {'Nome': 'Ana', 'Idade': 23, 'Senha': 'calabouca'}
    ]
    for cada_dicionario in lista:
        tabela_usuarios.add_row(cada_dicionario['Nome'], str(cada_dicionario['Idade']), cada_dicionario['Senha'])#a idade deve ser string, pois as tabelas do rich aceitam apenas strings 
    return tabela_usuarios #retorna com a tabela modificada 
terminal.print(tabela())