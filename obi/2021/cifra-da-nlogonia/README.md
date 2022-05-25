<p align="center">
  <img width="250px" src="../../../docs/imagens/obi/logo-obi.svg"/> 
</p>

 <h1 align="center" style="font-weight: bold">OBI 2021 - <span style="font-style: italic">Cifra da Nlogônia</span></h1>

O rei da Nlogônia ordenou que todos os documentos importantes sejam "cifrados", para que apenas quem tem conhecimento da cifra possa lê-los (cifrar um documento significa alterar o original modificando as letras de acordo com algum algoritmo de cifra).

O rei decretou que o seguinte algotimo deve ser usado para cifrar os documentos:

<ul>
<li>
Cada consoante deve ser substituída por exatamente três letras, na seguinte ordem:
<ol>
    <li>a própria consoante (vamos chamar de `consoante original`);</li>
    <li>a vogal mais próxima da consoante original no alfabeto, com a regra adicional de que se a consoante original está à mesma distância de duas vogais, então a vogal mais próxima do início do alfabeto é usada. Por exemplo, se a consoante original é `d`, a vogal que deve ser usada é `e`, pois esta é a vogal mais próxima; se a consoante original é `c`, a vogal que deve ser utilizada é `a`, porque `c` está à mesma distância de `a` e `e`, e `a` é mais próxima do início do alfabeto.</li>
    <li>a consoante que segue a consoante original, na ordem do início ao fim do alfabeto. Por exemplo, se a consoante original é `d`, a consoante a ser utilizada é `f`. No caso de a consoante original ser `z`, deve ser utilizada a própria letra `z`.</li>
</ol>
</li>
<li>
As vogais não são modificadas. 
</li>
</ul>
Nesta tarefa, o alfabeto é
<p align="center">a b c d e f g h i j k l m n o p q r s t u v x z</p>
e as vogais são
<p align="center">a e i o u</p>

Por exemplo, a cifra da palavra "ter" é "tuveros" (tuv-e-ros) e a cifra da palavra "paz" é "poqazuz" (poq-a-zuz).

O rei da Nlogônia procura por alguém que saiba escrever um programa que produza a cifra de uma palavra dada. Você pode ajudá-lo? 

## Entrada ⬅️ 
A primeira e única linha da entrada contém uma palavra P formada por letras minúsculas sem acentuação. 

## Saída ➡️
Seu programa deve produzir uma única linha, contendo a palavra cifrada. 

## Restrições
- A palavra P tem no mínimo uma e no máximo 30 letras, todas minúsculas e sem acentuação. 

---
## Exemplos:

- ### Primeiro Exemplo
  *Entrada*:
  ```
  ter
  ```
  *Saída*:
  ```
  tuveros
  ```
- ### Segundo Exemplo
  *Entrada*:
  ```
  rei
  ```
  *Saída*:
  ```
  rosei
  ```
- ### Terceiro Exemplo
  *Entrada*:
  ```
  arteiro
  ```
  *Saída*:
  ```
  arostuveiroso
  ```

<br/>

## Link para Online Judge:
- [NEPS Academy](https://neps.academy/br/exercise/1487)
- [Pratique OBI](https://olimpiada.ic.unicamp.br/pratique/p2/2021/f1/cifra/)

## Soluções adicionadas:
| Ícone | Linguagem | Tag | Nome |
|:---:|:---:|:---:|:---:|
| <img width="100px" alt="Python" src="../../../docs/recursos/ícones/python.svg"> | Python | [@Gvinfinity](https://github.com/Gvinfinity/) | Gabriel Soares |
