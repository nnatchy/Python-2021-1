def m_sum(m,axis):
    l = []
    if axis == 0:
        for i in range(len(m[0])):
            t = []
            for j in range(len(m)):
                t.append(m[j][i])
            l.append(sum(t))
    elif axis == 1:
        for i in range(len(m)):
            l.append(sum(m[i]))
    return l

exec(input().strip())