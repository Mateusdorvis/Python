import pandas as pd
#cria um data frame 
data_frame = pd.date_range(start='10-01-2024', end='10-10-2024', freq='D')
dataframeindex = pd.DatetimeIndex(data=data_frame) #instancia a classe 

print(dataframeindex) #mostra na tabela