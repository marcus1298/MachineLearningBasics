## Reconhecimento de IRIS 

Esse código é um exemplo básico de como usar aprendizado de máquina para classificação de dados. Ele pode ser usado como base para construir modelos mais sofisticados e para entender como os diferentes componentes de um pipeline de aprendizado de máquina se relacionam

## Requisitos

Python 3 instalado

Para executar este programa, você precisará das seguintes bibliotecas:

Biblioteca pandas (pode ser instalada com o comando pip install pandas)

Biblioteca numpy (pode ser instalada com o comando pip install numpy)

Biblioteca scikit-learn (pode ser instalada com o comando pip install -U scikit-learn)

Biblioteca seaborn (pode ser instalada com o comando pip install seaborn)

Biblioteca matplotlib (pode ser instalada com o comando pip install matplotlib)

Biblioteca keras (pode ser instalada com o comando pip install keras)

Biblioteca tensorboard (pode ser instalada com o comando pip install tensorboard)

Biblioteca visdom (pode ser instalada com o comando pip install visdom)

Uma conexão com a internet para baixar os dados do iris.


## Como funciona?

Este código é um exemplo de como utilizar o algoritmo de aprendizado de máquina chamado "Rede Neural Multi-Camadas Perceptron" (MLP) para classificar flores Iris. O objetivo é prever a qual espécie de Iris uma flor pertence (setosa, versicolor ou virginica) com base nas suas medidas de comprimento e largura de sépala e pétala.

Primeiramente, ele baixa e carrega os dados do iris a partir de um arquivo online. Os dados incluem medidas de 150 flores de Iris, juntamente com a espécie a qual elas pertencem. Em seguida, os dados são divididos em conjuntos de treinamento e teste. O conjunto de treinamento é utilizado para "ensinar" a rede neural como classificar as flores, enquanto o conjunto de teste é usado para avaliar a precisão do modelo treinado.

Em seguida, as classes são codificadas como números inteiros (0, 1, 2) e convertidas em vetores de variáveis fictícias (também conhecidos como "one-hot encoded"). Isso é necessário para que o algoritmo MLP possa processar os dados.

O próximo passo é criar a estrutura da rede neural MLP. Isso é feito usando a biblioteca Keras e especificando a quantidade de camadas e neurônios em cada camada. Neste caso, temos uma camada de entrada com 4 neurônios (correspondentes às 4 medidas de cada flor), uma camada oculta com 10 neurônios e uma camada de saída com 3 neurônios (correspondentes às 3 espécies de Iris).

Depois de definir a estrutura da rede, ela é compilada, o que significa que é configurada para usar uma determinada função de perda (neste caso, entropia cruzada categórica) e um otimizador (Adam).

## Etapas

Este código é um exemplo de como usar uma técnica chamada aprendizado de máquina para classificar diferentes tipos de flores de íris. O código faz as seguintes coisas:

Baixa e carrega os dados: O código baixa os dados de flores de íris de um website e os carrega em uma estrutura de dados chamada dataframe.

Divide os dados em conjuntos de treinamento e teste: Os dados são divididos aleatoriamente em dois conjuntos, um para treinar o modelo e outro para testar a precisão dele.

Prepara os dados para o modelo: As classes das flores são convertidas em números e os dados são transformados em um formato conhecido como "dummy variables" (variáveis fictícias).

Cria o modelo: O código cria um modelo de rede neural chamado Multi-Layer Perceptron (MLP) com três camadas.

Treina o modelo: O modelo é treinado com os dados de treinamento.

Testa o modelo: O modelo é usado para fazer previsões com os dados de teste e a precisão é medida comparando as previsões com as respostas reais.

Plota os dados: Os dados são plotados usando uma biblioteca chamada Seaborn para que possam ser visualizados de forma mais fácil.

Usa o modelo para fazer previsões em novos dados: O modelo é usado para fazer previsões em um conjunto de dados novo e a classe prevista é exibida.

## Como usar?

Para utilizar este código, é necessário ter o Python e a biblioteca NumPy instalados.

Faça o clone deste repositório para sua máquina:

Entre na pasta do repositório:

Execute o código:

python3 main.py

## Resultado
O modelo atingiu uma precisão de aproximadamente 0,98 no conjunto de teste
O modelo foi capaz de fazer previsões com novos dados

![alt text](https://github.com/marcus1298/MachineLearningBasics/blob/main/10%20-%20Flower%20recognition%20using%20an%20MLP/Captura%20de%20tela%202023-01-24%20234318.jpg)


## Observação
O código utiliza o algoritmo Multi Layer Perceptron (MLP) para treinar o modelo

O dataset Iris é um conjunto de dados com informações sobre três espécies de flores (setosa, versicolor e virginica) e suas medidas de sépala e pétala. É amplamente utilizado como exemplo para aprendizado de máquina.

O código divide os dados em conjunto de treinamento e teste, onde o modelo é treinado com o conjunto de treinamento e avaliado com o conjunto de teste

O código utiliza a biblioteca Seaborn para visualizar os dados e ver a distribuição das flores em relação às suas medidas de sépala e pétala.

O código utiliza a função de ativação ReLU para as camadas ocultas e Softmax para a camada de saída.

O código usa a perda categorical_crossentropy e o otimizador Adam para a compilação do modelo, e treina o modelo com 100 épocas e tamanho de lote de 10.


