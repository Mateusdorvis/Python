import matplotlib.pyplot as plt

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Cria o gráfico
plt.plot(x, y, marker='o')

# Adiciona título e rótulos dentro do gráfico
plt.title('Gráfico de Linhas Exemplo')
plt.xlabel('Eixo X')  #legendas
plt.ylabel('Eixo Y') #legendas

# Mostra o gráfico
plt.show()
