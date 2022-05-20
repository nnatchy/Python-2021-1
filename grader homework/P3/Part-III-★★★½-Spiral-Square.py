def spiral_square(n): #n is a positive odd number
    finallist = [[0 for i in range(n)] for j in range(n)]
    x = (n-1)//2
    y = (n-1)//2
    pos = [[x,y]]
    num = [i+1 for i in range(n**2)]
    for i in range(n//2):
        y += 1
        pos.append([x,y])
        for j in range((n//2)-i,x+1): #1 i = 0 x = 1 y = 2
            x -= 1
            pos.append([x,y])
        for j in range((n//2)-i,y+1): #2 i = 0 x = 0 y = 2
            y -= 1
            pos.append([x,y])
        for j in range(x,(n//2)+i+1): #2 i = 0 x = 0 y = 0
            x += 1
            pos.append([x,y])
        for j in range(y,(n//2)+i+1): #2 i = 0
            y += 1
            pos.append([x,y])
    for loc in pos:
        finallist[loc[0]][loc[1]] = num.pop(0)
    return finallist

def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
exec(input().strip())
