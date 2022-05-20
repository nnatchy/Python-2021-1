def factor(n):
    f = []
    k = 2
    while k <= n:
        count = 0
        running = True
        while running:
            if n%k == 0:
                n = n/k
                count += 1
            else:
                break
        if count == 0:
            pass
        else:
            f.append([k,count])
        k += 1
    return f
exec(input().strip())