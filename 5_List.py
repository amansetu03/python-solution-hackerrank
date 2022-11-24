if __name__ == '__main__':
    N = int(input())
    L=[]
    for i in range(0,N):
        opt=input().split()
        if opt[0]=="insert":
            L.insert(int(opt[1]),int(opt[2]))
        elif opt[0] == "append":
            L.append(int(opt[1]))
        elif opt[0] == "pop":
            L.pop();
        elif opt[0] == "print":
            print(L)
        elif opt[0] == "remove":
            L.remove(int(opt[1]))
        elif opt[0] == "sort":
            L.sort();
        else:
            L.reverse();
