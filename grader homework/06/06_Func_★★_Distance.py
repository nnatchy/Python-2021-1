def distance1(x1,y1,x2,y2):
    import math
    dx = (x1-x2)**2
    dy = (y1-y2)**2
    distance = math.sqrt(dx+dy)
    return distance

def distance2(p1,p2):
    dx = (p1[0] - p2[0])**2
    dy = (p1[1] - p2[1])**2
    import math
    dist = math.sqrt(dx+dy)
    return dist

def distance3(c1,c2):
    dot1 = []
    dot2 = []
    for i in range(2):
        dot1.append(c1[i])
        dot2.append(c2[i])
    dist = distance2(dot1,dot2)
    if dist > float(c1[2]+c2[2]):
        Result = False
    else:
        Result = True
    return dist,Result

def perimeter(points):
    #[[1,2],[2,3],[3,4],[4,5]]
    total_dist = 0
    for i in range(len(points)-1):
        total_dist = total_dist + distance2(points[i],points[i+1])
    total_dist = total_dist + distance2(points[0],points[-1])
    return total_dist

exec(input().strip())
        




    
    
    

        

