def row_number(t,e): # return row number of t containing e (top row is row #0)
    for row in range(len(t)):
        if e in t[row]:
            return row

def flatten(t):
    l = []
    for i in range(len(t)):
        for j in t[i]:
            if j != 0:
                l.append(j)
    return l

def inversions(x):
    count = 0
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            if x[i] > x[j]:
                count += 1
    return count

def solvable(t):
    if len(t)%2 == 1 and inversions(flatten(t))%2 == 0:
        return True
    elif len(t)%2 == 0:
        if inversions(flatten(t))%2 == 1 and row_number(t,0)%2 == 0:
            return True
        elif inversions(flatten(t))%2 == 0 and row_number(t,0)%2 == 1:
            return True
        return False
    return False

exec(input().strip()) # do not remove this line