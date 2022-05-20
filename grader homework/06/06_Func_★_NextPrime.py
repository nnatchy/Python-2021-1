def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(N):
    running = True
    k = N
    while running:
        for i in range(k,k+1):
            if is_prime(i+1) == True:
                return i+1
            else:
                k = k+1

def next_twin_prime(N):
    k = N
    running = True
    while running:
        for i in range(k,k+1):
            if is_prime(i+1) == True and is_prime(i+3) == True:
                a = '(' + str(i+1)+','+' '+str(i+3)+ ')'
                return a
            else:
                k = k+1

exec(input().strip())


