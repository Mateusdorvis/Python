import matplotlib.pyplot as plt

#vamos supor que uma escola fez uma pesquisa com alunos, onde mostra a idade dos alunos de uma turma tem grande maioria 17, 18, e 19, no qual 50% de 30 alunos tem 18 anos, outros 30% tem 17 anos , enquanto uns 20% tem 19 anos
idades  = [17,18,19]
porcentual = [30, 50, 20]

plt.bar(idades,porcentual, color='yellow')
for x in range(3):
    plt.text(idades[x], porcentual[x] +1, f'{porcentual[x]}%' )  #+1 para que o texto suba um pouco para facilitar a leitura
plt.title('Gráfico de barras ')
plt.xlabel('Idade dos alunos')  #legendas
plt.ylabel('Porcentual (%)') #legendas

# Mostra o gráfico
plt.show()
