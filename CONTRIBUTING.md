# 🎯 Manual de Contribuição
Que ótimo que você deseja contribuir neste projeto! É assim que as comunidades se desenvolvem, com o desejo e empolgação de várias pessoas em construir algo que importe!

Caso fique em dúvida em algum passo, basta ver os exemplos de problemas, competições e soluções adicionadas no repositório, eles vão lhe ajudar neste processo!

Abaixo você pode conferir um resumo com todas as formas de contribuir neste repositório, dividias em seções e subseções:

- **Adicionar soluções**
  - [Quero adicionar uma solução *para um problema já adicionado*](#Adicionar-soluções)
  - <details>
      <summary>Quero adicionar uma solução <i>para um problema ainda não adicionado</i></summary>
        <ol>
          <li>Veja a seção "Adicionar problemas"</li>
          <li>Retorne para esta seção e veja "Quero adicionar uma solução para um problema já adicionado"</li>
        </ol>
    </details>  
- **Adicionar problemas**
- **Adicionar competições**

<br>

## Adicionar soluções
Em todos os casos, **basta colocar o arquivo da sua solução na pasta do problema que você resolveu**. Quando fizer o commit, por favor colocar uma **mensagem descritiva** (por exemplo, "*Adiciona solução em C++ do problema Colheita de Milho da OPEI 2019*"). Além de adicionar o seu arquivo, também é necessário adicionar sua solução no README.md do problema, para facilitar a visualização das outras pessoas.

A parte do README.md que deverá ser modificada é a tabela de "Soluções adicionadas" que fica no final dos READMEs de problemas. A sintaxe para fazer este tipo de tabelas é:
```Markdown
| Ícone | Linguagem | Tag | Nome |
|:---:|:---:|:---:|:---:|
| (consulte o README de ícones, disponível na pasta docs) | Nome da Linguagem | [@nome-de-usuario](https://github.com/nome-do-usuario) | Nome do Usuário |
```
Veja um exemplo e seu resultado:
```Markdown
| Ícone | Linguagem | Tag | Nome |
|:---:|:---:|:---:|:---:|
| <img width="100px" alt="Python" src="docs/recursos/ícones/python.svg"> | Python | [@fabiopapais](https://github.com/fabiopapais) | Fábio Papais |
```
| Ícone | Linguagem | Tag | Nome |
|:---:|:---:|:---:|:---:|
| <img width="100px" alt="Python" src="docs/recursos/ícones/python.svg"> | Python | [@fabiopapais](https://github.com/fabiopapais) | Fábio Papais |

</br>

Caso queira adicionar novas linguagens abaixo, basta adicionar uma nova linha:
```Markdown
| Ícone | Linguagem | Tag | Nome |
|:---:|:---:|:---:|:---:|
| <img width="100px" alt="Python" src="docs/recursos/ícones/python.svg"> | Python | [@fabiopapais](https://github.com/fabiopapais) | Fábio Papais |
| <img width="100px" alt="C++" src="docs/recursos/ícones/c++.svg"> | C++ | [@weltonfelix](https://github.com/weltonfelix) | Welton Felix |
```
| Ícone | Linguagem | Tag | Nome |
|:---:|:---:|:---:|:---:|
| <img width="100px" alt="Python" src="docs/recursos/ícones/python.svg"> | Python | [@fabiopapais](https://github.com/fabiopapais) | Fábio Papais |
| <img width="100px" alt="C++" src="docs/recursos/ícones/c++.svg"> | C++ | [@weltonfelix](https://github.com/weltonfelix) | Welton Felix |

## Adicionar problemas
Antes de adicionar um problema, certifique-se de que a competição/olimpíada da qual vocẽ retirou o problema já está adicionada (caso não esteja, basta ver a seção [Adicionar competições](#Adicionar-competições)) Atente-se também para a edição/ano da competição, separando as edições por pastas (ex.: "2019", "2020", "2021").

Para adicionar um novo problema é bem simples:

1) Dentro da pasta da competição, encontre a pasta com a edição em que o seu problema apareceu (caso não exista, crie uma), por exemplo, 2019, 2020, XVI. **Dentro desta pasta, crie uma nova com o nome do seu problema.** 
> Siga a formatação padrão, escrevendo os nomes em minúsculo, sem acentos e palavras separadas por travessões ("-"). *Por exemplo, se o nome do seu problema é "Colheita de Milho", o nome da pasta será "colheita-de-milho"*.
2) **Adicione seu arquivo com a solução dentro desta pasta.** O nome do arquivo deve ter o mesmo nome da pasta.
3) **Dentro da pasta do problema, crie um arquivo README.md**, é nele que ficará o enunciado do problema, além de outras informações relevantes para a comunidade.
4) Por fim, **preencha o seu README.md** com as informações do problema. **O template [NOVO_PROBLEMA.md](docs/recursos/templates/NOVO_PROBLEMA.md) está disponível neste repositório na pasta ```docs/recursos/templates```.** Basta copiar o conteúdo deste template e preencher com as informações do seu problema.

## Adicionar competições
Adicionar uma competição é bem simples, basta criar pastas e um README.md. Veja o passo a passo:

1) Na raiz do repositório, **crie uma pasta com o nome da competição**. *Siga a formatação padrão*, com letras em minúsculo e palavras separadas por travessão (ex.: "Code Jam" vira "code-jam").
2) Dentro da pasta da nova competição, *crie um arquivo README.md*
3) Por fim, **preencha o seu README.md** com as informações da competição. **O template [NOVA_COMPETIÇÃO.md](docs/recursos/templates/NOVA_COMPETIÇÃO.md) está disponível neste repositório na pasta ```docs/recursos/templates```.** Basta copiar o conteúdo deste template e preencher com as informações da sua competição.