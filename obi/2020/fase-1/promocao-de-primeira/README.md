<p align="center">
<img width="250px" src="../../../../docs/imagens/obi/logo-obi.svg"/> </p>

 <h1 align="center" style="font-weight: bold">OBI 2020 - <span style="font-style: italic"> Promoção de Primeira</span></h1>

O reino da Linearlândia possui N cidades espalhadas por seu vasto território, sendo que N-1 pares distintos de cidades estão ligados diretamente por uma rodovia bi-direcional. Esses pares foram escolhidos de forma que existe exatamente um caminho entre qualquer par de cidades, possivelmente passando por outras cidades no meio do caminho. Cada rodovia da Linearlândia é servida por uma linha de ônibus, que faz viagens de ida e volta entre as duas cidades, operada por apenas uma empresa, como manda a lei determinada pelo Rei. O problema é que existem apenas duas empresas de ônibus: a RoyalBus e a ImperialBus.

Cada viagem entre duas cidades ligadas diretamente por uma rodovia custa uma passagem da empresa que opera aquela linha. Ao chegar numa cidade, se o passageiro quiser prosseguir viagem para outra cidade, ele tem que desembarcar, entrar em outro ônibus e pagar outra passagem. Só que o Rei determinou, para o feriadão anual de celebração da Linearidade Real, uma estranha promoção: sempre que o passageiro entrar no ônibus de uma empresa ele não precisa pagar a passagem se sua viagem imediatamente anterior foi pela outra empresa. Quer dizer, se o caminho alterna entre a RoyalBus e a ImperialBus, só é preciso pagar uma passagem, a primeira.

Neste problema, dada a descrição da malha de rodovias da Linearlândia, seu programa deve computar o número máximo de cidades num caminho, começando em qualquer cidade, para o qual é preciso pagar apenas uma passagem para ir da cidade inicial até a cidade final do caminho. O número de cidades no caminho inclui a cidade inicial e a cidade final.


## Entrada ⬅️ 
A primeira linha da entrada contém um inteiro N, representando o número de cidades da Linearlândia. As cidades são numeradas de 1 até N. As N-1 linhas seguintes contêm, cada uma, três inteiros A, B e E, indicando que existe uma rodovia entre as cidades A e B e que a linha de ônibus entre elas é operado pela empresa E (0 para RoyalBus, 1 para ImperialBus).

## Saída ➡️
Seu programa deve imprimir uma linha contendo um inteiro representando o número máximo de cidades num caminho para o qual é preciso pagar apenas uma passagem durante a celebração da Linearidade Real.

## Restrições
- 2 ≤ N ≤ 50000
- 1 ≤ A ≤ N
- 1 ≤ B ≤ N
- 0 ≤ E ≤ 1


---
## Exemplos:

- ### Primeiro Exemplo
  *Entrada*:
  ```
  8
  3 1 0
  2 7 0
  6 8 1
  1 4 1
  5 4 1
  4 7 1
  7 6 0
  ```
  *Saída*:
  ```
  4
  ```
- ### Segundo Exemplo
  *Entrada*:
  ```
  2
  1 2 0
  ```
  *Saída*:
  ```
  2
  ```
- ### Terceiro Exemplo
  *Entrada*:
  ```
  18
  13 16 0
  16 15 1
  16 12 0
  14 12 0
  12 8 1
  1 18 0
  1 3 0
  2 3 1
  3 8 1
  11 17 1
  17 10 1
  8 17 0
  6 7 0
  9 7 0
  5 7 1
  4 5 0
  8 5 1
  ```
  *Saída*:
  ```
  6
  ```

<br/>

## Link para Online Judge:
[NEPS Academy](https://neps.academy/br/exercise/823)

## Soluções adicionadas:
| Ícone | Linguagem | Tag | Nome |
|:---:|:---:|:---:|:---:|
|  |  |  |  |

