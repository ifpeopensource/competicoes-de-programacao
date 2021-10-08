def main():
    
    #Atribui o número de eventos para a variável n 
    n = int(input())

    #Intanciando o dicionário que armazena o tempo passado para cada amigo
    dic = {}
    #Intanciando a lista de amigos que estão esperando mensagem de resposta
    waitlist = []

    for i in range(n):
        
        #Separa a entrada do evento em uma lista de duas partes em que o Índice '0' será o tipo de operação e o índice '1' o valor
        row = input().split()

        #Verifica cada um dos casos e executa uma ação de acordo com as regras informadas na questão
        if row[0] == "T":
            for e in waitlist:
                dic[e] += int(row[1]) - 1
        else:
            for e in waitlist:
                dic[e] += 1

        if row[0] == "E":
            waitlist.remove(row[1])
        
        if row[0] == "R":
            waitlist.append(row[1])
            if not dic.get(row[1]):
                dic[row[1]] = 0   
    
    #Itera pelos elementos do dicionário em ordem crescente
    for e in sorted(list(dic.keys())):
        
        #Verifica se o elemento (remetente) ainda espera uma resposta, caso sim retorna o valor de "-1", caso não retorna o valor de tempo
        if e in waitlist:
            print(e, "-1", sep = ' ')    
        else:
            print(e, dic[e], sep = ' ')
            

if __name__ == "__main__":
    main()
