def pattern1(nrows, ncols):
    final = []
    row = []
    count = 0
    for i in range(nrows):
        for j in range(1, ncols+1):
            count += 1
            row.append(count)
        final.append(row)
        row = []
    return final


def pattern2(nrows, ncols):
    final = []
    templist = []
    k = 1
    for i in range(3):
        for j in range(k, nrows*ncols+1, 3):
            templist.append(j)
        final.append(templist)
        templist = []
        k += 1
    return final


def pattern3(N):
    k = 1
    final = [0]*N
    templist = [0]*N
    for i in range(0, N):
        for j in range(i, N):
            templist[j] = k
            k += 1
        final[i] = templist
        templist = [0]*N
    return final


def rowtocol(l):
    real = []
    tempreal = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            tempreal.append(l[j][i])
        real.append(tempreal)
        tempreal = []
    return real


def pattern4(N):
    k = 1
    final = []
    templist = [0]*N
    for i in range(0, N):
        for j in range(N-i-1, N):
            templist[j] = k
            k += 1
        final.append((templist[::-1]))
        templist = [0]*N
    return rowtocol(final)


def pattern5(N):
    k = 1
    final = []
    templist = [0]*N
    for i in range(0, N):
        gap = N-1
        for j in range(N-i-1, N):
            templist[j] = k
            k = k + gap
            gap = gap - 1
        final.append((templist[::-1]))
        templist = [0]*N
        k = i+1
        k += 1
    return rowtocol(final)

def pattern6(N):
    num = 1
    final = [[0 for i in range(N)] for j in range(N)]
    rnd = 0
    gap = 0
    for ind in range(N):
        if ind % 2 == 0:  # ind = 2
            for j in range(N-ind):  # 4-2 = 2
                if ind == 0:
                    final[j][j] = num
                    num += 1
                elif ind > 0:
                    final[j][j+gap] = num
                    num += 1
        elif ind % 2 == 1:
            for j in range(N-ind, 0, -1):
                final[j-1][j+gap-1] = num
                num += 1
        gap += 1
    return final


exec(input().strip())
