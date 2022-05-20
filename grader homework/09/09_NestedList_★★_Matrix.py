def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m

def mult_c(c,A):
    for row in range(len(A)):
        for col in range(len(A[row])):
            A[row][col] *= c
    return A

def mult(A,B):
    c = []
    for i in range(len(A)): #row A
        l = []
        for j in range(len(B[0])): #col B
            total = 0
            for k in range(len(B)): #row B
                total += A[i][k] * B[k][j]
            l.append(total)
        c.append(l)
    return c

exec(input().strip())       



    