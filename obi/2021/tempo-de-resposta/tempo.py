def main():
    n = int(input())

    dic = {}
    waitlist = []

    t = 0

    for i in range(n):
        row = input().split()

        if row[0] == "T":
            for e in waitlist:
                dic[e] += int(row[1]) - 1
        else:
            for e in waitlist:
                dic[e] += 1

        if row[0] == "E":
            waitlist.remove(row[1])
            if not dic.get(row[1]):
                dic[row[1]] = 0   
        
        if row[0] == "R":
            waitlist.append(row[1])
            if not dic.get(row[1]):
                dic[row[1]] = 0   
    
    for e in sorted(list(dic.keys())):
        if e in waitlist:
            print(e, "-1", sep = ' ')    
        else:
            print(e, dic[e], sep = ' ')
            

if __name__ == "__main__":
    main()
