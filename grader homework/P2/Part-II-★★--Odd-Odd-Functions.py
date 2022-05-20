def is_odd(n):
    if n%2 != 0:
        return True
    return False

def has_odds(x):
    for i in x:
        if i%2 != 0:
            return True
    return False

def all_odds(x):
    for i in x:
        if i%2 == 0:
            return False
    return True

def no_odds(x):
    for i in x:
        if i%2 != 0:
            return False
    return True

def get_odds(x):
    l = []
    for i in x:
        if i%2 != 0:
            l.append(i)
    return l

def zip_odds(a,b):
    odda = get_odds(a)
    oddb = get_odds(b)
    for i in range(len(oddb)):
        odda.insert(2*i+1,oddb[i])
    return odda

exec(input().strip())