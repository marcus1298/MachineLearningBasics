## Rede neural utilizando neurônios de McCulloch-Pitts para a função OR exclusivo em Python 
Esse código implementa a Regressão Linear usando o algoritmo Adaline (Adaptive Linear Neuron) em Python.
Este código é um exemplo de como treinar uma ADALINE (Adaptive Linear Neuron) sem usar a biblioteca scikit-learn's LinearRegression, usando somente NumPy e Matplotlib. Ele segue os seguintes passos:

## Requisitos
Python 3.x

## Como usar

Faça o download do código ou clone o repositório para o seu computador

Abra o arquivo "main.py" no seu editor de código

Execute o código usando o seu interpretador Python

## O que o código faz

Para construir uma rede neural utilizando neurônios de McCulloch-Pitts para a função OR exclusivo em Python sem usar a biblioteca numpy, precisamos primeiro entender o que é uma função OR exclusivo e como os neurônios de McCulloch-Pitts funcionam.

A função OR exclusivo é uma função lógica que retorna "verdadeiro" se pelo menos um dos seus inputs é "verdadeiro", mas retorna "falso" se ambos os inputs são "falso". Por exemplo, se tivermos dois inputs A e B, e A é "verdadeiro" e B é "falso", a função OR exclusivo retornaria "verdadeiro".

Os neurônios de McCulloch-Pitts são uma forma simples de simular a atividade de um neurônio biológico. Eles possuem inputs e um peso para cada um desses inputs. A atividade do neurônio é determinada pela soma dos inputs multiplicados pelos seus pesos. Se essa soma for maior do que um determinado limiar, o neurônio é considerado ativo e retorna "verdadeiro", caso contrário, ele é considerado inativo e retorna "falso".

Agora que entendemos o que é a função OR exclusivo e como os neurônios de McCulloch-Pitts funcionam, podemos construir a nossa rede neural.

1.Primeiro, criamos os inputs e os pesos para a nossa rede neural. Usaremos dois inputs A e B e atribuiremos pesos de 1 para ambos:

inputs = [A, B]


weights = [1, 1]

2.Depois, calculamos a soma dos inputs multiplicados pelos pesos:

soma = inputs[0]*weights[0] + inputs[1]*weights[1]

3.Finalmente, definimos o limiar como 0.5 e checamos se a soma é maior do que esse limiar. Se for, retornamos "verdadeiro", caso contrário, retornamos "falso":

limiar = 0.5

if soma > limiar:

    output = "verdadeiro"
    
else:

    output = "falso"
    

## Resultado

Abaixo segue uma imagem do gráfico gerado pelos casos de teste do código:


![alt text](https://github.com/marcus1298/MachineLearningBasics/blob/main/02%20-%20XOR%20logic%20function%20using%20McCulloch-Pitts%20neurons/1Resultado.jpg)

Esse código é apenas um exemplo ilustrativo e pode ser modificado e aprimorado de acordo com suas necessidades. 
Espero que este código seja útil para você e qualquer dúvida ou sugestão, por favor não hesite em entrar em contato ou abrir uma issue no GitHub.
