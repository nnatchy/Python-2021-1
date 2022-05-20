import numpy as np
def eq(A, B, p):
    count = len(A[A == B])
    return ((count*100)/A.size) == p

def closest_point_indexes(points, p):
    dist = np.sqrt((points[:,0]-p[0])**2 + (points[:,1]-p[1])**2)
    index = np.arange(points.shape[0])
    return index[dist == dist.min()]

def number_of_inversions(A):
    count = 0
    for i in range(A.size):
        count += np.less(A[i:], A[i]).sum()
    return count

exec(input().strip())