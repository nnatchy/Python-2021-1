import string
inp1 = input().strip()
inp2 = input().strip()
d1, d2 = {}, {}
l1, l2 = [], []
for i in inp1.lower():
    if i in string.ascii_letters:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
for i in inp2.lower():
    if i in string.ascii_letters:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1
if len(d2) > len(d1):
    for key in d2:
        if key not in d1:
            d1[key] = 0
elif len(d1) > len(d2):
    for key in d1:
        if key not in d2:
            d2[key] = 0
if len(d1) > len(d2):
    for key in d1:
        if key not in d2:
            d2[key] = 0
elif len(d2) > len(d1):
    for key in d2:
        if key not in d1:
            d1[key] = 0
for key, val in d1.items():
    l1.append([key, val])
    l1.sort()
for key, val in d2.items():
    l2.append([key, val])
    l2.sort()
count = 0
if l1 == l2:
    print(inp1)
    print('- None')
    print(inp2)
    print('- None')
else:
    print(inp1)
    deep = []
    for i in range(len(l1)):
        count = 0
        if l1[i][0] == l2[i][0]:
            if l1[i][1] > l2[i][1]:
                deep.append('c')
                count = l1[i][1] - l2[i][1]
                if count == 1:
                    print("- remove %d %s" % (count, l1[i][0]))
                else:
                    print("- remove %d %s's" % (count, l1[i][0]))
            
        else:
            deep.append('c')
            if l1[i][1] == 1:
                print("- remove %d %s" % (l1[i][1], l1[i][0]))
            else:
                print("- remove %d %s's" % (l1[i][1], l1[i][0]))
    if len(deep) == 0:
        print('- None')
    print(inp2)
    gay = []
    for i in range(len(l2)):
        count = 0
        if l2[i][0] == l1[i][0]:
            if l1[i][1] < l2[i][1]:
                gay.append('c')
                count = abs(l1[i][1] - l2[i][1])
                if count == 1:
                    print("- remove %d %s" % (count, l2[i][0]))
                else:
                    print("- remove %d %s's" % (count, l2[i][0]))
        else:
            gay.append('c')
            if l2[i][1] == 1:
                print("- remove %d %s" % (l2[i][1], l2[i][0]))
            else:
                print("- remove %d %s's" % (l2[i][1], l2[i][0]))
    if len(gay) == 0:
        print('- None')