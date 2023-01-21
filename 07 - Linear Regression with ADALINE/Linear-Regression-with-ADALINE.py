# Importar as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

# Construindo a base de observações
np.random.seed(0)
x = np.random.rand(100, 1)
y = 2 + 3 * x + np.random.rand(100, 1)

# Inicializando os pesos
weights = np.random.rand(2, 1)

# Taxa de aprendizado
learning_rate = 0.01

# Número de iterações
num_iterations = 1000

# Armazenando os custos para plotar
costs = []

# Treinando a ADALINE com a base de observações
for i in range(num_iterations):
    # Adicionando uma coluna de 1's para x
    x_bias = np.c_[np.ones((x.shape[0], 1)), x]
    
    # Fazendo a predição
    y_predict = x_bias.dot(weights)
    
    # Calculando o erro
    error = y_predict - y
    
    # Calculando o custo
    cost = (error ** 2).sum() / (2 * x.shape[0])
    
    # Armazenando o custo
    costs.append(cost)
    
    # Atualizando os pesos
    weights = weights - learning_rate * x_bias.T.dot(error) / x.shape[0]

# Trace uma linha de regressão linear
y_pred = x_bias.dot(weights)

# Plotando os resultados de regressão
plt.scatter(x, y, color='b')
plt.plot(x, y_pred, color='k')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Comparando os resultados de regressão com os obtidos utilizando as equações de a e b
print('Equation of line obtained from ADALINE: y = ', weights[0][0], '+', weights[1][0], 'x')

# Encontrando o coeficiente de correlação de Pearson
corr = np.corrcoef(x.T, y.T)[0, 1]
print('Pearson Correlation Coefficient:', corr)

# Encontrando o coeficiente de determinação
y_mean = np.mean(y)
SST = ((y - y_mean)**2).sum()
SSR = ((y_pred - y_mean)**2).sum()
R_2 = SSR/SST
print('Coefficient of Determination (R^2):', R_2)
