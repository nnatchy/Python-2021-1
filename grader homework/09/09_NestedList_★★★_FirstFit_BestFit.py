def first_fit(L,e):
    for i in range(len(L)):
        if sum(L[i]) + e > 100:
            pass
        else:
            L[i].append(e)
            return L
    L.append([e])
    return L
    
def best_fit(L,e):
    temp = []
    for i in range(len(L)):
        if sum(L[i]) + e < 100:
            temp.append([sum(L[i]),i])
        elif sum(L[i]) + e == 100:
            return L[i].append(e)
    if temp == []:
        return L.append([e])
    temp.sort()
    temp = temp[::-1]
    index = temp[0][1]
    L[index].append(e)
    return L

def partition_FF(D):
    l = [[D[0]]]
    for i in range(1,len(D)):
        first_fit(l,D[i])
    return l

def partition_BF(D):
    BF= [[D[0]]]
    for i in range(1,len(D)):
        best_fit(BF,D[i])
    return(BF)

exec(input().strip())
