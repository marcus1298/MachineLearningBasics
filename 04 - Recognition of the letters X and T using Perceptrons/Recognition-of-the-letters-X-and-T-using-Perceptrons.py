import numpy as np

# Dados iniciais
# Base de dados
# Classe -1 (letra X)
A = np.array([1, -1, -1, -1, 1,
              -1, 1, -1,  1, -1,
              -1, -1, 1,  -1, -1,
              -1, 1, -1, 1, -1,
              1, -1, -1, -1, 1,
              ])
# Classe 1 (letra T)
B = np.array([1, 1, 1, 1, 1,
              -1, -1, 1,  -1, -1,
              -1, -1, 1,  -1, -1,
              -1, -1, 1, -1, -1,
              -1, -1, 1, -1, -1])
# Pesos iniciais
Pesos = np.array([0.4, -0.6, 0.6, 0.5, 0.5,
                  0.4, -0.6, 0.6, 0.5, 0.5,
                  0.4, -0.6, 0.6, 0.5, 0.5,
                  0.4, -0.6, 0.6, 0.5, 0.5,
                  0.4, -0.6, 0.6, 0.5, 0.5])
# Taxa de aprendizagem
eta = 0.4
# Vies
bias = 0.5

# Função para a soma ponderada
def somaPonderada(X, W):
    # m = x0*w0 + x1*w1 + x2*w2
    m = np.multiply(X, W)
    # u = m - 1*0
    u = np.sum(m) - 1*bias
    return u

# Função de ativação
# Função degrau
def funcaoAtivacao(u):
    if u >= 0:
        return 1
    else:
        return -1

# Função de saída
def saida(X, W):
    u = somaPonderada(X, W)
    return funcaoAtivacao(u)

# Função para ajustes dos pesos
# Parte central do processo de aprendizagem
# novo wi -> w1 = wi + DeltaN xi(d  - y)
def ajustaPesos(eta, W, X, bias, d, y):
    e = d - y
    novoW = W + eta*X*e
    novoB = bias + eta*(-1)*e
    return novoW, novoB

# Treinamento

# Iteracao 1

# Entrada 001 saída -1
d = -1
y = saida(A, Pesos)
print(y)
# Ajuste dos pesos
Pesos, bias = ajustaPesos(eta, Pesos, A, bias, d, y)
print(Pesos)
print(bias)
# Entrada 110 saída +1
d = 1
y = saida(B, Pesos)
print(y)
# Ajuste dos pesos
Pesos, bias = ajustaPesos(eta, Pesos, B, bias, d, y)
print(Pesos)
print(bias)

# Iteracao 2

# Entrada 001 saída -1
d = -1
y = saida(A, Pesos)
print(y)
# Ajuste dos pesos
Pesos, bias = ajustaPesos(eta, Pesos, A, bias, d, y)
print(Pesos)
print(bias)

# Entrada 110 saída +1
d = 1
y = saida(B, Pesos)
print(y)
# Ajuste dos pesos
Pesos, bias = ajustaPesos(eta, Pesos, B, bias, d, y)
print(Pesos)
print(bias)

# Repetir as iterações até que a saída desejada seja alcançada

# Teste

# Entrada para reconhecimento
X_teste = np.array([-1, -1, 1, 1, 1,
                    -1, 1, -1, 1, -1,
                    -1, -1, 1, -1, -1,
                    -1, 1, -1, 1, -1,
                    -1, -1, -1, -1, 1])

# Saída do teste
y_teste = saida(X_teste, Pesos)
print(y_teste)

import matplotlib.pyplot as plt
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].imshow(X_teste.reshape(5, 5), cmap='gray')
axs[0].set_title("Entrada de teste")

if y_teste == 1:
    axs[1].imshow(B.reshape(5, 5), cmap='gray')
    axs[1].set_title("Saída: Letra T")
else:
    axs[1].imshow(A.reshape(5, 5), cmap='gray')
    axs[1].set_title("Saída: Letra X")
    
plt.show()
