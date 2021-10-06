<p align="center">
<img width="250px" src="../../../../docs/imagens/obi/logo-obi.svg"/> </p>

 <h1 align="center" style="font-weight: bold">OBI 2020 - <span style="font-style: italic"> Pandemia</span></h1>

Um grupo de amigos, preocupados por ter que prestar o ENEM este ano, resolveu iniciar o ano fazendo reuniões de estudo. Mas eles não esperavam que uma epidemia com um novo vírus ocorresse na região em que moravam. Nessa epidemia específica, os sintomas da doença aparecem muitos dias depois do contágio, mas mesmo sem sintomas uma pessoa infectada infecta todos com quem tenha o mínimo contato.

O grupo de amigos também não sabia que um deles havia sido infectado, sem saber, por pessoas de fora do grupo, o que fez a infecção se espalhar pelos amigos do grupo. Felizmente todos os amigos infectados se recuperaram e passam bem.

Muitas reuniões de estudo aconteceram, mas nem todos os amigos participaram de todas as reuniões.

Você receberá a informação de quais amigos participaram de cada reunião. Além disso, você receberá também a informação de qual amigo participou de reunião do grupo após ter sido infectado por pessoas de fora do grupo, e em qual reunião isso ocorreu. Você deve assumir que:

- todos os amigos que participaram de reunião em que ao menos um deles estava infectado também foram infectados.
- o único amigo infectado por pessoas de fora do grupo é o que foi informado. No caso de todos os outros amigos que foram infectados a infecção aconteceu em reunião do grupo.
- Escreva um programa para determinar quantos amigos, ao final da sequência de reuniões, foram infectados.


## Entrada ⬅️ 
A primeira linha da entrada contém dois números inteiros N, M, respectivamente o total de amigos do grupo e o total de dias em que houve reunião. Os amigos são identificados por números inteiros de 1 a N, as reuniões são identificadas por números inteiros de 1 (primeira reunião) a M (última reunião). A segunda linha contém dois números inteiros I e R, respectivamente o identificador do amigo que foi infectado por pessoas de fora do grupo e o número da primeira reunião em que ele participou infectado. Cada uma das M linhas seguintes contém a informação dos participantes de uma reunião, em sequência; ou seja, a primeira linha descreve os participantes da reunião 1, a segunda linha descreve os participantes da reunião 2 e assim por diante. Cada uma dessas linhas inicia com um número A, o total de amigos que participaram dessa reunião, seguido de A inteiros Pi identificando cada amigo participante da reunião.

## Saída ➡️
Seu programa deve produzir uma única linha, contendo um inteiro, o número total de amigos infectados ao final do mês.

## Restrições
<li>2 ≤ N ≤ 1000</li>
<li>2 ≤ M ≤ 1000</li>
<li>1 ≤ I ≤ N</li>
<li>1 ≤ R ≤ M</li>
<li>1 ≤ A ≤ N</li>
<li>1 ≤ Pi ≤ N para 1 ≤ i ≤ A</li>

---
## Exemplos:

- ### Primeiro Exemplo
  *Entrada*:
  ```
  4 3
  2 1
  2 1 2
  3 3 1 2
  2 2 1
  ```
  *Saída*:
  ```
  5 6
  3 4
  2 1 3
  4 1 2 3 5
  2 1 3
  2 1 3
  2 4 5
  2 2 4
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
  2
  ```
- ### Terceiro Exemplo
  *Entrada*:
  ```
  10 5
  2 1
  6 7 5 1 9 6 2
  3 9 4 6
  3 2 9 5
  3 8 5 7
  2 8 9
  ```
  *Saída*:
  ```
  8
  ```

<br/>

## Soluções adicionadas:
| Ícone | Linguagem | Tag | Nome |
|:---:|:---:|:---:|:---:|
|  |  |  |  |

