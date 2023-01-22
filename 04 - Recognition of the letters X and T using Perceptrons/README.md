## Reconhecimento de letras X e T usando Perceptrons
Este repositório contém um exemplo de como utilizar um perceptron para reconhecimento de letras X e T. O código está escrito em Python e utiliza a biblioteca NumPy para trabalhar com arrays.

## Como funciona?

O perceptron é uma técnica de aprendizado supervisionado utilizada para classificação binária. Ele consiste em uma rede neural de uma camada, com um número finito de entradas, pesos e uma saída binária.

Neste exemplo, utilizamos uma base de dados com dois exemplos, um para cada letra (X e T). Os pesos iniciais são definidos aleatoriamente e, através de iterações de treinamento, os pesos são ajustados até que a saída desejada seja alcançada.

## Etapas

Importação das bibliotecas necessárias: O código começa importando a biblioteca numpy que será utilizada para trabalhar com arrays e matrizes.

Definição da base de dados: São definidos dois arrays, um para a letra X e outro para a letra T, que serão utilizados como entrada para o perceptron.

Inicialização dos pesos: São definidos os pesos iniciais do perceptron de forma aleatória.

Definição da taxa de aprendizagem: A taxa de aprendizagem é um parâmetro utilizado para controlar a velocidade de ajuste dos pesos durante o treinamento.

Definição da função de soma ponderada: A função de soma ponderada é responsável por calcular a soma dos pesos multiplicados pelas entradas, subtraindo o bias.

Definição da função de ativação: A função de ativação utilizada é a função degrau, que retorna 1 quando a soma ponderada é maior ou igual a 0 e -1 caso contrário.

Definição da função de saída: A função de saída utiliza a soma ponderada e a função de ativação para calcular a saída do perceptron.

Definição da função de ajuste de pesos: A função de ajuste de pesos é responsável por atualizar os pesos do perceptron com base na saída desejada e obtida durante o treinamento.

Treinamento do perceptron: O treinamento é realizado através de iterações, onde as entradas de X e T são utilizadas para ajustar os pesos do perceptron.

Teste do perceptron: Uma entrada de teste semelhante à letra X é utilizada para testar o perceptron

## Como usar?

Para utilizar este código, é necessário ter o Python e a biblioteca NumPy instalados.

Faça o clone deste repositório para sua máquina:

Entre na pasta do repositório:

Execute o código:

python3 main.py

## Resultado
Ao executar o código, será realizado o treinamento do perceptron e, no final, será realizado um teste com uma entrada de teste semelhante à letra X. O resultado será exibido de forma visual, comparando a entrada de teste e saída do perceptron com a letra X ou T.

![alt text](https://github.com/marcus1298/MachineLearningBasics/blob/main/04%20-%20Recognition%20of%20the%20letters%20X%20and%20T%20using%20Perceptrons/LetraT.jpg)

![alt text](https://github.com/marcus1298/MachineLearningBasics/blob/main/04%20-%20Recognition%20of%20the%20letters%20X%20and%20T%20using%20Perceptrons/LetraX.jpg)

## Observação
Este exemplo foi criado com o objetivo de ser didático e ilustrativo. Ele pode ser usado como base para desenvolver projetos mais complexos envolvendo reconhecimento de padrões.
