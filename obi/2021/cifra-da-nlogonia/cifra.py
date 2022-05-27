def main():
    
    # String de entrada
    s = input()

    # Define strings com letras do alfabeto 
    alphabet = "abcdefghijklmnopqrstuvxz"
    consonants = "bcdfghjklmnpqrstvxz"
    vowels = "aeiou"
    
    # Lista com os índices das vogais no alfabeto em ordem
    ivowels = [0,4,8,14,20]
    
    out = ""    

    # Loop para cada letra na entrada
    for l in s:

        # Se vogal adiciona para o output e pula para a próxima letra
        if l in vowels: 
            out += l
            continue

        # 1° Passo para consoantes
        out += l

        # 2° Passo para consoantes

        # Calcula a distâncias para cada uma das vogais
        dist = [abs(i-alphabet.index(l)) for i in ivowels]
        
        # Calcula a menor distância e adiciona para o output 
        mindist = min(dist)
        out += vowels[dist.index(mindist)]
        
        # 3° Passo para consoantes
        if l == 'z':
            out += 'z'
        else:
            out += consonants[consonants.index(l)+1]

    print(out)

if __name__ == "__main__":
    main()
