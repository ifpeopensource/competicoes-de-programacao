<p align="center">
  <img width="250px" src="../../../docs/imagens/obi/logo-obi2021.svg"/> 
</p>

 <h1 align="center" style="font-weight: bold">OBI 2020 - <span style="font-style: italic"> Camisetas da Olimpíada</span></h1>

A Olimpíada Municipal de Programação vai distribuir camisetas para os melhores colocados, e por isso solicitou que os premiados informassem o tamanho preferido da camiseta, entre os tamanhos pequeno e médio.

A empresa que confeccionou as camisetas, por uma falha, pode ter se enganado na quantidade de camisetas para cada tamanho. Foram produzidas camisetas em número suficiente para todos os premiados, mas talvez não do tamanho preferido.

Dadas a lista com os tamanhos preferidos pelos premiados e a quantidade de camisetas de cada tamanho produzidas pela empresa, escreva um programa para determinar se todos os premiados receberão camisetas do tamanho escolhido.

## Entrada ⬅️ 
A primeira linha contém um inteiro N, o número de premiados. A segunda linha contém N inteiros Ti, indicando os tamanhos solicitados pelos premiados, sendo que Ti = 1 representa o tamanho pequeno e Ti = 2 representa o tamanho médio. A terceira linha contém um inteiro P, o número de camisetas de tamanho pequeno produzidas. A quarta e última contém um inteiro M, o número de camisetas de tamanho médio produzidas.

## Saída ➡️
Seu programa deve produzir uma única linha, contendo um único caractere, que deve ser a letra maiúscula 'S' se todos os premiados serão atendidos com a camiseta do tamanho que escolheram, ou a letra maiúscula 'N' caso contrário.

## Restrições ➡️
<li> 1 ≤ N ≤ 1000</li>
<li> 0 ≤ P ≤ 1000</li>
<li> 0 ≤ M ≤ 1000</li>
<li> N ≤ P + M</li>
<li> 1 ≤ Xi ≤ 2 para 1 ≤ i ≤ N</li>

---
## Exemplos:

- ### Primeiro Exemplo
  *Entrada*:
  ```
  5
  1 1 2 1 2
  3
  2
  ```
  *Saída*:
  ```
  S
  ```
- ### Segundo Exemplo
  *Entrada*:
  ```
  4
  2 2 2 2
  1
  3
  ```
  *Saída*:
  ```
  N
  ```
- ### Terceiro Exemplo
  *Entrada*:
  ```
  6
  1 1 1 2 1 1
  4
  4
  ```
  *Saída*:
  ```
  N
  ```

<br/>

## Soluções adicionadas:
| Ícone | Linguagem | Tag | Nome |
|:---:|:---:|:---:|:---:|
| <img width="100px" alt="Python" src="../../../docs/recursos/ícones/python.svg"> | Python | [@ryangpaiva](https://github.com/ryangpaiva) | Ryan Paiva |

