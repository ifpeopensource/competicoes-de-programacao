<p align="center">
<img width="250px" src="../../../../docs/imagens/obi/logo-obi.svg"/> </p>

 <h1 align="center" style="font-weight: bold">OBI 2020 - <span style="font-style: italic"> Fissura Perigosa</span></h1>

A erupção do vulcão Kilauea em 2018 no Havaí atraiu a atenção de todo o mundo. Inicialmente a força da erupção era menor e a lava avançou para o sul com relativamente poucos danos. Após algumas semanas, porém, a fissura 8 começou a jorrar com mais força e a lava avançou também para o norte trazendo muita destruição.

Você está ajudando na implementação de um sistema para simular a área por onde a lava avançaria, em função da força da erupção. O mapa será representado simplificadamente por uma matriz quadrada de caracteres, de 1 a 9, indicando a altitude do terreno em cada posição da matriz. Vamos considerar que a fissura 8, por onde a erupção se inicia, está sempre na posição do canto superior esquerdo da matriz. Dada a força da erupção, que será um valor inteiro, de 0 a 9, seu programa deve imprimir a matriz de caracteres representando o avanço final da lava. Se a lava consegue invadir uma posição da matriz, o caractere naquela posição deve ser trocado por um asterisco ('*'). Uma posição será invadida pela lava se seu valor for menor ou igual à força da erupção e

- for a posição inicial; ou
<li>estiver adjacente, ortogonalmente (abaixo, acima, à esquerda ou à direita), a uma posição invadida.</li>

A figura abaixo mostra um exemplo de mapa e o avanço final da lava para quatro forças de erupção: 1, 3, 6 e 8, respectivamente da esquerda para a direita.

```
27755478     *7755478     *7755478     ********
29985439     *9985439     *9985439     *99****9
34899989     *4899989     **899989     ***999*9
22115569     ****5569     *******9     *******9
66736689     667*6689     **7***89     *******9
99886555     99886555     9988****     99******
44433399     44433399     ******99     ******99
99986991     99986991     9998*991     999**991

```


## Entrada ⬅️ 
A primeira linha da entrada contém dois inteiros N e F representando, respectivamente o número de linhas (que é igual ao de colunas) da matriz e a força da erupção. Cada uma das N linhas seguintes contém uma string de N caracteres, entre 1 e 9, indicando o mapa de entrada.

## Saída ➡️
Seu programa deve imprimir N linhas contendo, cada uma, N caracteres representando o avanço final da lava de acordo com o enunciado.

## Restrições
- 1 ≤ N ≤ 500
- 0 ≤ F ≤ 9



---
## Exemplos:

- ### Primeiro Exemplo
  *Entrada*:
  ```
    8 6
    27755478
    29985439
    34899989
    22115569
    66736689
    99886555
    44433399
    99986991
  ```
  *Saída*:
  ```
    *7755478
    *9985439
    **899989
    *******9
    **7***89
    9988****
    ******99
    9998*991
  ```
- ### Segundo Exemplo
  *Entrada*:
  ```
    65 4
    25679
    35234
    17182
    39993
    11223
  ```
  *Saída*:
  ```
    *5679
    *5***
    *7*8*
    *999*
    *****
  ```
- ### Terceiro Exemplo
  *Entrada*:
  ```
    2 8
    91
    11
  ```
  *Saída*:
  ```
    91
    11
  ```

<br/>

## Soluções adicionadas:
| Ícone | Linguagem | Tag | Nome |
|:---:|:---:|:---:|:---:|
|  |  |  |  |
