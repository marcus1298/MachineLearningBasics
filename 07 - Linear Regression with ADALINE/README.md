## Regressão Linear com Adaline
Esse código implementa a Regressão Linear usando o algoritmo Adaline (Adaptive Linear Neuron) em Python.
Este código é um exemplo de como treinar uma ADALINE (Adaptive Linear Neuron) sem usar a biblioteca scikit-learn's LinearRegression, usando somente NumPy e Matplotlib. Ele segue os seguintes passos:

## Requisitos
Python 3.x

NumPy

Matplotlib

## Como usar

Faça o download do código ou clone o repositório para o seu computador

Abra o arquivo "main.py" no seu editor de código

Execute o código usando o seu interpretador Python

## O que o código faz

1.Importação das bibliotecas necessárias: NumPy e Matplotlib.

2.Construção da base de observações: uma amostra de 100 pontos de dados geradas aleatoriamente é criada, onde x é gerado aleatoriamente e y é calculado como 2 + 3 * x + ruído gaussiano.

3.Inicialização dos pesos: os pesos são inicializados aleatoriamente com valores entre 0 e 1.

4.Taxa de aprendizado e número de iterações: a taxa de aprendizado é definida como 0.01 e o número de iterações é definido como 1000.

5.Treinamento da ADALINE com a base de observações: um loop é executado por 1000 iterações, onde cada iteração realiza as seguintes etapas:

Adicionando uma coluna de 1's para x, para representar o viés.

Fazendo a predição y_predict usando x_bias e os pesos atuais.

Calculando o erro entre y_predict e y.

Calculando o custo como a soma do erro ao quadrado dividido por 2 * o número de amostras.

Armazenando o custo.

Atualizando os pesos usando o gradiente descendente.


6. Tracando uma linha de regressão linear: com os pesos treinados, fazemos a previsão de y usando x_bias e os pesos atuais.

7. Plotando os resultados de regressão: os dados reais são plotados como pontos azuis e a linha de regressão linear é plotada como uma linha preta.

8. Comparando os resultados de regressão com os obtidos utilizando as equações de a e b: imprime a equação da linha obtida da ADALINE.

9. Encontrando o coeficiente de correlação de Pearson: usando a função corrcoef do NumPy, calcula e imprime o coeficiente de correlação de Pearson entre x e y.

10. Encontrando o coeficiente de determinação: usando os valores de y_pred e y, calcula e imprime o coeficiente de determinação (R^2).


## Resultado

Abaixo segue uma imagem do gráfico gerado pelo código mostrando a linha de regressão linear obtida através do algoritmo Adaline:
Regressão Linear com Adaline

Esse código é apenas um exemplo ilustrativo e pode ser modificado e aprimorado de acordo com suas necessidades. O algoritmo Adaline pode ser aplicado em diversos problemas de regressão linear e é uma boa opção quando se deseja trabalhar com grandes conjuntos de dados ou quando há necessidade de atualização contínua dos pesos.

Espero que este código seja útil para você e qualquer dúvida ou sugestão, por favor não hesite em entrar em contato ou abrir uma issue no GitHub.
