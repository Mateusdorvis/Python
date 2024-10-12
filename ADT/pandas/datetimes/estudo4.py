import pandas as pd
#fazendo um a tabela  de datas com filtragem 
data = pd.date_range(start='20-09-2024', end='10-10-2024', freq='D')

df = pd.DataFrame(data, columns=['dia completo'])
#criando novas colunas como índice data, ano e mês
df['índice'] = range(len(df))
df['dia'] = df['dia completo'].dt.day
df['mes'] = df['dia completo'].dt.month
df['ano'] = df['dia completo'].dt.year

print(df)