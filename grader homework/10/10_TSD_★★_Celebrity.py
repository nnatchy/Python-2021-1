def knows(R,x,y):
    for key in R:
        if key == x and y in R[key]:
            return True
    return False

def is_celeb(R,x):
    for key in R:
        if x not in R[key] and key != x:
            return False
    if len(R[x]) == 1 and x in R[x]:
        return True
    if len(R[x]) > 0:
        return False
    return True

def find_celeb(R):
    for person in R:
        if is_celeb(R,person) == True:
            return person

def read_relations():
    R = {}
    name = input().split()
    while name != ['q']:
        if name[0] not in R:
            R[name[0]] = {name[0],name[1]}
        else:
            R[name[0]].add(name[1])
        if name[1] not in R:
            R[name[1]] = {name[1]}
        name = input().split()
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)

exec(input().strip()) # do not remove this line