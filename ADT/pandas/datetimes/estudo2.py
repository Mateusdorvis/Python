import pandas as pd

#cria um dataframe com intervlo de datas D
data = pd.bdate_range(start='10-10-2024', end='20-10-2024', freq='D')

#cria uma tabela com a dataframe e com a coluna data
dataframe = pd.DataFrame(data, columns=['data completa'])
dataframe['indice'] = range(len(dataframe))
dataframe.set_index('data completa', inplace=True) #mostra o índice de cada data
print(dataframe)

data_hora = pd.date_range(start='01-01-2024', end='20-10-2024', freq='H')#data frame com frequencia de horas 
dataframe_hora = pd.DataFrame(data_hora, columns=['Data e hora'])
