def reverse(d):
    d1 = {}
    for key in d:
        d1[d[key]] = key
    return d1

def keys(d, v):
    l = []
    for key in d:
        if v == d[key]:
            l.append(key)
    return l

exec(input().strip())

