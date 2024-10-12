import pandas as pd
#dicionario de dados
tabela_dados_usuarios  = {'Nomes do usuário ': ['Mateus', 'Jorge', 'Felipe', 'Ana', 'Jussara'], 'Idades': [19, 20, 30, 29, 17]}
#exibindo o dicionario como se fosse tabela
tabela_pandas =  pd.DataFrame(tabela_dados_usuarios)

#mostrando a tabela na tela
print(tabela_pandas)

#tabela filtrada
tabela_filtrada = tabela_pandas[tabela_pandas['Idades'] > 20]

print('Tabela filtrada')


#adicionando novas colunas 
tabela_pandas['Cidades'] =  ['Porto Alegre', 'Curitiba', 'São Paulo', 'Rio de Janeiro', 'Brasília']


