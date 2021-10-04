<p align="center">
  <img width="250px" src="../../../../docs/imagens/obi/logo-obi.svg"/> 
</p>

 <h1 align="center" style="font-weight: bold">OBI 2021 - <span style="font-style: italic">Idade de Camila</span></h1>

Seu chefe está ao telefone, nervoso. Ele quer que você compute a soma de uma sequência de números que ele vai falar para você ao telefone, para saber o total das vendas em sua mais recente viagem de negócios.

Infelizmente, de vez em quando seu chefe fala números errados para você ao telefone.

Felizmente, seu chefe rapidamente percebe que falou um número errado e diz “zero”, que como
combinado previamente quer dizer *ignore o último número corrente*.

Infelizmente, seu chefe pode cometer erros repetidos, e diz “zero” para cada erro.

Por exemplo, seu chefe pode falar ao telefone “Um, três, cinco, quatro, zero, zero, sete, zero, zero,
seis”, o que significa uma soma total igual a 7, conforme explicado na tabela abaixo:

|     **Fala do chefe**     | **Números correntes** |           **Explicação**          |
|:-------------------------:|:---------------------:|:---------------------------------:|
| “um, três, cinco, quatro” |        1,3,5,4        |     registre os quatro números    |
|        “zero, zero”       |          1,3          |   ignore os dois últimos números  |
|           “sete”          |         1,3,7         | registre o sete ao final da lista |
|        “zero, zero”       |           1           |   ignore os dois últimos números  |
|           “seis”          |          1,6          |  registre seis ao final da lista  |

Para não deixar seu chefe ainda mais nervoso, escreva um programa que determine a soma total
dos números falados por seu chefe ao telefone.

## Entrada ⬅️ 
A primeira linha da entrada contém um inteiro `N`, a quantidade de números inteiros (incluindo os “zeros”) que o seu chefe falou ao telefone. Cada uma das `N` linhas seguintes contém um número inteiro `X`<sub>i</sub>.

## Saída ➡️
Seu programa deve produzir uma única linha na saída, contendo um único inteiro, a soma correta dos números, levando em conta que o valor 0 significa erro, conforme descrito.

## Restrições
- `1 ≤ N ≤ 100 000`
- `0 ≤ Xi ≤ 100`, para (`1 ≤ i ≤ N`)
- `0 ≤ resultado ≤ 1 000 000`

---
## Exemplos:

- ### Primeiro Exemplo
  *Entrada*:
  ```
  4
  3
  0
  4
  0
  ```
  *Saída*:
  ```
  0
  ```
- ### Segundo Exemplo
  *Entrada*:
  ```
  10
  1
  3
  5
  4
  0
  0
  7
  0
  0
  6
  ```
  *Saída*:
  ```
  7
  ```

<br/>

## Soluções adicionadas:
| Ícone | Linguagem | Tag | Nome |
|:---:|:---:|:---:|:---:|
| <img width="100px" alt="Python" src="../../../docs/recursos/ícones/python.svg"> | Python | [@weltonfelix](https://github.com/weltonfelix/) | Welton |
