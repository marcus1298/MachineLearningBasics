## MLP para aproximação de função
Este repositório tem como objetivo aproximar uma função através da utilização de uma rede neural multicamada (MLP) utilizando o Pytorch.

## Requisitos

Pytorch

Matplotlib

Numpy

## Como funciona?

O perceptron é uma técnica de aprendizado supervisionado utilizada para classificação binária. Ele consiste em uma rede neural de uma camada, com um número finito de entradas, pesos e uma saída binária.

Neste exemplo, utilizamos uma base de dados com dois exemplos, um para cada letra (X e T). Os pesos iniciais são definidos aleatoriamente e, através de iterações de treinamento, os pesos são ajustados até que a saída desejada seja alcançada.


## Etapas

1. O código define os pontos amostrados da função a ser aproximada e transforma-os em tensores do Pytorch

2. Define a arquitetura da rede neural multicamada (MLP) com uma camada oculta de 10 neurônios e uma camada de saída de 1 neurônio

3. Realiza o treinamento da MLP através da definição de uma função de perda (mean squared error) e otimizador (Adam

4. Realiza a avaliação da MLP com os pontos de teste

5. Plota o gráfico comparando a função real com a função aproximada pela MLP

## Como usar?

Para utilizar este código, é necessário ter o Python e a biblioteca NumPy instalados.

Faça o clone deste repositório

Instale as bibliotecas necessárias (Pytorch, Matplotlib e Numpy)

Execute o arquivo main.py

## Resultado
Ao final do treinamento e avaliação, é exibido um gráfico comparando a função real com a aproximação realizada pela MLP. É possível observar que a MLP consegue aproximar com boa precisão a função desejada.

![alt text](https://github.com/marcus1298/MachineLearningBasics/blob/main/08%20-%20Functional%20Approach/8Resultado.jpg)


## Observação
Este código mostra como é possível utilizar uma rede neural multicamada (MLP) para aproximar uma função através da utilização do Pytorch. Além disso, é possível observar a facilidade de utilização desta biblioteca para treinamento e avaliação de redes neurais.

