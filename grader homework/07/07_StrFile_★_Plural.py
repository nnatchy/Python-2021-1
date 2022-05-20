name = input()
es = ['s','x','ch']
ies = ['y']
saraa = ['a','e','i','o','u']
if name[-1] in es or name[-2:] in es:
    name = name + 'es'
    print(name)
elif name[-1] in ies:
    if name[-2] in saraa:
        name = name + 's'
        print(name)
    else:
        name = name[:-1] + 'ies'
        print(name)
else:
    name = name + 's'
    print(name)