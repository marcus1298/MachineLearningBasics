## Reconhecimento de digitos usando MLB
O seguinte repositório apresenta um exemplo de como treinar e avaliar uma rede neural de uma camada com o conjunto de dados MNIST usando PyTorch.

## Requisitos

Para executar este programa, você precisará das seguintes bibliotecas:

torch: Biblioteca PyTorch para computação em tensores e modelos de aprendizado de máquina

torchvision: Biblioteca PyTorch com conjuntos de dados e ferramentas de visão computacional

numpy: Biblioteca para computação científica com Python

matplotlib: Biblioteca para plotagem de gráficos e visualização de dados

Além disso, você precisará de uma GPU para treinar a rede neural. Se você não tiver uma GPU, poderá usar o pacote torch.no_grad() para treinar a rede sem a GPU.

Também seria necessário ter o python instalado na versão 3.x e as bibliotecas mencionadas acima instaladas antes de rodar o programa.


## Como funciona?

O que é PyTorch?

PyTorch é uma biblioteca de aprendizado de máquina open-source baseada em Torch, desenvolvida pelo Facebook. Ela fornece ferramentas para construir modelos de aprendizado de máquina, além de uma ampla variedade de funcionalidades para lidar com tarefas de processamento de dados e aprendizado de máquina.

O que é uma Rede Neural?

Uma rede neural é um sistema de processamento de dados inspirado na estrutura e função do cérebro humano. Elas são compostas por camadas de nós (ou neurônios) que são conectados uns aos outros. Cada nó recebe entradas, aplica uma transformação matemática (geralmente uma operação de multiplicação e soma) e envia a saída para os nós conectados.

O que é MNIST?

MNIST é um conjunto de dados de reconhecimento de dígitos manuscritos que vem com o PyTorch. Ele contém 60.000 exemplos de treinamento e 10.000 exemplos de teste de dígitos de 0 a 9 escritos à mão. Cada imagem tem 28x28 pixels.

Definição da arquitetura da rede

Neste exemplo, a rede neural usada é uma Multi Layer Perceptron (MLP) com uma camada escondida e uma camada de saída. A camada de entrada tem 28x28 = 784 neurônios, correspondentes aos pixels de cada imagem. A camada escondida tem 512 neurônios e a camada de saída tem 10 neurônios, correspondentes aos dígitos de 0 a 9.

Treinamento da rede

Para treinar a rede, usamos o algoritmo de otimização de descida estocástica (SGD) e uma função de perda de entropia cruzada. A função de perda mede a diferença entre as saídas previstas pelo modelo e as saídas desejadas (labels) e o otimizador atualiza os pesos da rede com base nessa diferença. O treinamento é realizado usando mini-batch com 100 imagens por vez.

Testando a rede

Após o treinamento, testamos a precisão da rede no conjunto de teste. A precisão é a proporção de imagens classificadas corretamente pelo modelo.

Visualização dos resultados

Para visualizar a evolução da perda durante o treinamento, salvamos a perda em cada it

## Etapas

Importar as bibliotecas necessárias: Começamos importando as bibliotecas necessárias, como PyTorch, Numpy e Matplotlib. PyTorch é usado para construir e treinar a rede neural, Numpy é usado para trabalhar com arrays e Matplotlib é usado para plotar gráficos.

Definição da classe da rede neural: Criamos uma classe chamada MLP que herda de nn.Module e define a arquitetura da rede neural. Essa classe tem dois métodos, o construtor (init) e o método de propagação para frente (forward). No construtor, definimos duas camadas completamente conectadas (fc1 e fc2), e no método forward, aplicamos a transformação linear e nós sigmoidais.

Carregamento dos dados de treinamento e teste: Usamos o torchvision para carregar o conjunto de dados MNIST e dividi-lo em conjuntos de treinamento e teste. Também usamos o DataLoader para carregar os dados em lotes.

Criação do modelo, loss e optimizer: Criamos uma instância da classe MLP para representar o modelo, usamos a entropia cruzada como função de perda e o otimizador de descida estocástica para atualizar os pesos do modelo.

Treinando a rede: Usamos a função train() para treinar a rede por um determinado número de épocas. Dentro dessa função, usamos um loop para passar por todos os lotes de treinamento e atualizar os pesos do modelo usando a função de perda e o otimizador.

Testando a rede: Usamos a função test() para testar a precisão do modelo no conjunto de teste. A precisão é calculada como a proporção de imagens classificadas corretamente.

Plotando a evolução da perda durante o treinamento: Usamos a função plot_loss_history() para plotar o gráfico da evolução da perda ao longo das iterações de treinamento.

Plotando exemplos de dígitos classificados incorretamente: Usamos a função plot_misclassified() para plotar exemplos de dígitos classificados incorretamente pelo modelo.

Chamando as funções de treinamento, teste, plotagem de evolução da perda e plotagem de exemplos classificados incorretamente no final do arquivo para que as funções sejam executadas e os resultados

## Como usar?

Para utilizar este código, é necessário ter o Python e a biblioteca NumPy instalados.

Faça o clone deste repositório para sua máquina:

Entre na pasta do repositório:

Execute o código:

python3 main.py

## Resultado
Para visualizar a evolução da perda durante o treinamento, salvamos a perda em cada iteração do loop de treinamento em uma lista e, em seguida, usamos essa lista para plotar o gráfico usando matplotlib. Também é possível visualizar exemplos de dígitos classificados incorretamente, comparando as labels reais com as labels previstas pelo modelo e usando matplotlib para plotar essas imagens. Isso pode nos dar uma ideia dos erros que o modelo está cometendo e como corrigi-los.


![alt text](https://github.com/marcus1298/MachineLearningBasics/blob/main/09%20-%20Digit%20recognition%20using%20an%20MLP/Pytorch.jpg)

![alt text](https://github.com/marcus1298/MachineLearningBasics/blob/main/09%20-%20Digit%20recognition%20using%20an%20MLP/sklearn9.jpg)

## Observação
Além disso, este exemplo mostra como usar PyTorch de forma interativa, o que significa que você pode facilmente modificar o código e experimentar com diferentes configurações e parâmetros para ver como eles afetam o desempenho do modelo. Por exemplo, você pode experimentar com o número de camadas e neurônios em sua rede, o tamanho do lote de treinamento, o algoritmo de otimização, e assim por diante.

É importante notar também que, embora este exemplo use uma rede neural simples e pequeno conjunto de dados, PyTorch também é capaz de lidar com redes neurais mais complexas e grandes conjuntos de dados. Isso inclui redes neurais profundas (deep learning) e outros tipos de redes neurais, como redes neurais convolucionais (CNNs) e redes neurais recorrentes (RNNs).

Em resumo, este exemplo fornece uma visão geral do uso básico de PyTorch para treinar e avaliar uma rede neural, bem como como visualizar os resultados do treinamento e teste. Ele também destaca a facilidade de uso e a flexibilidade de PyTorch, permitindo aos usuários experimentar com diferentes configurações e parâmetros para melhorar o desempenho do modelo.
