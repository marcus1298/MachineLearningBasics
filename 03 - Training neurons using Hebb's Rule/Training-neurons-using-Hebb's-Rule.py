import numpy as np
import seaborn as sns

# Função para gerar a tabela verdade para todas as funções lógicas
def generate_tables():
    t=np.zeros((16,4))
    for i in range(16):
        num = i
        j=3
        while(j>=0):
            if(num%2==1):
                t[i][j]=1
            else:
                t[i][j]=0
            num=int(num/2)
            j-=1
    return t

# Função para treinar a rede neural usando a regra de Hebb
def train_hebb(t, s):
    wNovo=np.zeros((16,2))
    bNovo=np.zeros(16)
    for i in range(16):
        wAnterior=[0,0]
        bAnterior=0
        for j in range(4):
            for z in range(2):
                wNovo[i][z]=wAnterior[z]+s[j][z]*t[i][j]
                wAnterior[z]=wNovo[i][z]
            bNovo[i]=bAnterior+t[i][j]
            bAnterior=bNovo[i]
    return wNovo,bNovo

# Função para validar a rede neural com as entradas
def validate(w, b, input_data):
    result = np.zeros(16)
    for i in range(16):
        net = 0
        for j in range(2):
            net += w[i][j] * input_data[j]
        net += b[i]
        if net >= 0:
            result[i] = 1
    return result

# Gerando as tabelas verdade
tables = generate_tables()
# Treinando a rede neural
weights, bias = train_hebb(tables, [[1, 1], [1, -1], [-1, 1], [-1, -1]])

# Testando a rede neural com as entradas
inputs = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
outputs = []
for input_data in inputs:
    output = validate(weights, bias, input_data)
    outputs.append(output)
    print(f'Inputs: {input_data} Output: {output}')

#Plotando os resultados com seaborn
logic_gates = ["And", "Nand", "Or", "Xor", "Nor", "Xnor", "Not And", "Not Or", "Not Xor", "Not And Not", "Not Or Not", "Not", "And Not", "Or Not", "Xor Not", "Not Xnor"]
sns.heatmap(np.array(outputs), annot=True, xticklabels=logic_gates)
plt.title("Resultados das portas lógicas")
plt.xlabel("Funções Lógicas")
plt.ylabel("Entradas A e B")
plt.show()

#Explicação:
# O código acima faz uso da regra de Hebb para treinar uma rede neural com neurônios de McCulloch-Pitts para as 14 funções lógicas possíveis (usando representação bipolar).
#A função generate_tables() gera a tabela verdade para todos os casos de teste.
# A função train_hebb() realiza o treinamento da rede neural usando a regra de Hebb e retorna os pesos e bias finais.
