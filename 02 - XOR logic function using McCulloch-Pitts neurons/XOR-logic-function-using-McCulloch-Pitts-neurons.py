import matplotlib.pyplot as plt
#Primeiro, criamos os inputs e os pesos para a nossa rede neural. Usaremos dois inputs A e B e atribuiremos pesos de 1 para ambos:
inputs = [1,1] #A e B são nossos inputs
weights = [1, 1]

#Depois, calculamos a soma dos inputs multiplicados pelos pesos:
soma = inputs[0]*weights[0] + inputs[1]*weights[1]

#Finalmente, definimos o limiar como 0.5 e checamos se a soma é maior do que esse limiar. Se for, retornamos "verdadeiro", caso contrário, retornamos "falso":
limiar = 0.5
if soma > limiar:
    output = "verdadeiro"
else:
    output = "falso"
print(output)

# criando uma tabela verdade para os casos de teste
A = [0, 0, 1, 1]
B = [0, 1, 0, 1]
output = []

#calculando a saída
for i in range(4):
    soma = A[i]*weights[0] + B[i]*weights[1]
    if soma > limiar:
        output.append(1)
    else:
        output.append(0)

# plotando o gráfico de barras
plt.bar(['A = 0, B = 0', 'A = 0, B = 1', 'A = 1, B = 0', 'A = 1, B = 1'], output)
plt.xlabel('Entradas A e B')
plt.ylabel('Saída')
plt.show()
