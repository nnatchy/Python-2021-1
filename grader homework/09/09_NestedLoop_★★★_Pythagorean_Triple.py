def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

def is_coprime(a,b,c):
    if gcd(a,b) == 1 or gcd(b,c) == 1 or gcd(c,a) == 1:
        return True
    return False

def primitive_Pythagorean_triples(max_len):
    triple = []
    for c in range(2,max_len+1):
        for b in range(2,c):
            for a in range(2,b):
                if c**2 == a**2 + b**2 and is_coprime(a,b,c) == True:
                    triple.append([c,a,b])
    triple.sort()
    return [[i[1],i[2],i[0]] for i in triple]

exec(input().strip())