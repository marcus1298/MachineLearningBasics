## Treinando Rede Neural com Neurônios de McCulloch-Pitts usando a regra de Hebb 
Rrede neural usando a regra de Hebb para encontrar os pesos das conexões entre os neurônios e aplicá-lo a todas as 14 funções lógicas que podem ser encontradas usando a representação bipolar.

Considerando as 16 funções lógicas que podem ser construídas a partir de 2 variáveis, 14 delas podem ser encontradas usando a representação bipolar e a regra de Hebb. As duas funções lógicas que não podem ser encontradas são a função NAND e a função NOR. Isso ocorre porque essas funções lógicas não podem ser representadas usando somente conexões positivas (ou seja, sem conexões negativas).

A representação bipolar é usada para representar as entradas e saídas de uma rede neural, onde 1 representa "verdadeiro" e -1 representa "falso". Isso permite a utilização de conexões negativas, o que é necessário para representar as funções lógicas NAND e NOR.

Em resumo, a regra de Hebb pode ser usada para encontrar os pesos das redes neurais correspondentes a 14 das 16 funções lógicas que podem ser construídas a partir de 2 variáveis quando é usada a representação bipolar.

## Requisitos
Python 3.x

## Como usar

Faça o download do código ou clone o repositório para o seu computador

Abra o arquivo "main.py" no seu editor de código

Execute o código usando o seu interpretador Python

## O que o código faz

O código acima faz uso da regra de Hebb para treinar uma rede neural com neurônios de McCulloch-Pitts para as 14 funções lógicas possíveis (usando representação bipolar).

A função generate_tables() gera a tabela verdade para todos os casos de teste.

A função train_hebb() realiza o treinamento da rede neural usando a regra de Hebb e retorna os pesos e bias finais.

Este código fornece uma representação visual dos resultados e permite verificar se a rede neural está funcionando corretamente para todas as funções lógicas.
    

## Resultado

Abaixo segue uma imagem do gráfico gerado pelos casos de teste do código:

![alt text](https://github.com/marcus1298/MachineLearningBasics/blob/main/03%20-%20Training%20neurons%20using%20Hebb's%20Rule/3Resultado.jpg)

Esse código é apenas um exemplo ilustrativo e pode ser modificado e aprimorado de acordo com suas necessidades. 
Espero que este código seja útil para você e qualquer dúvida ou sugestão, por favor não hesite em entrar em contato ou abrir uma issue no GitHub.

## Conclusão

Este código é uma ótima forma de entender como funcionam as redes neurais utilizando neurônios de McCulloch-Pitts e como a regra de Hebb pode ser utilizada para encontrar os pesos ideais para as conexões da rede. Além disso, é possível visualizar de forma clara e intuitiva os resultados obtidos pela rede.
