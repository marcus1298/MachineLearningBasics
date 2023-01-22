## MLP para aproximação de função
Este repositório tem como objetivo aproximar uma função através da utilização de uma rede neural multicamada (MLP) utilizando o Pytorch.

## Requisitos

Pytorch

Matplotlib

Numpy

## Como funciona?

ma Rede Neural Multicamada (MLP) é uma técnica de aprendizado supervisionado que pode ser utilizada para aproximar uma função a partir de dados amostrados. Ela é composta por várias camadas de neurônios interconectadas, onde cada camada é responsável por extrair características mais complexas a partir das características já extraídas na camada anterior.

A aproximação de uma função utilizando MLP é realizada através do treinamento da rede. Primeiramente, é necessário fornecer uma base de dados amostrados da função desejada, onde cada amostra é composta por uma entrada (x) e uma saída (t) esperada. A rede é então treinada utilizando esses dados, ajustando os pesos das conexões entre neurônios de forma a minimizar o erro entre a saída gerada pela rede e a saída esperada.

Para esse processo, é utilizado o algoritmo de backpropagation, onde é calculado o erro gerado pela rede e este erro é propagado de volta através das camadas, ajustando os pesos das conexões para minimizar o erro. Esse processo é repetido várias vezes até que o erro seja minimizado o suficiente.

Uma vez treinada, a rede é capaz de realizar a aproximação da função desejada para novos valores de entrada (x) que não fazem parte da base de dados de treinamento.

Para implementar essa técnica em Python, é comum utilizar bibliotecas como o PyTorch, que possuem classes e funções prontas para a construção e treinamento de redes neurais, facilitando a implementação.


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

