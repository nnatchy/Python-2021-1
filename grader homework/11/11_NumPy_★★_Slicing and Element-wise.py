import numpy as np

def sum_2_rows(M):
    return M[::2] + M[1::2]

def sum_left_right(M):
    return M[:,:M.shape[1]//2] + M[:,M.shape[1]//2:]

def sum_upper_lower(M):
    return M[:M.shape[0]//2,] + M[M.shape[0]//2:]

def sum_4_quadrants(M):
    A = M[:M.shape[0]//2,:M.shape[1]//2]
    B = M[:M.shape[0]//2,M.shape[1]//2:]
    C = M[M.shape[0]//2:,:M.shape[1]//2]
    D = M[M.shape[0]//2:,M.shape[1]//2:]
    return np.sum(np.array([A,B,C,D]),axis = 0)

def sum_4_cells(M):
    return M[::2,::2] + M[::2,1::2] + M[1::2,::2] + M[1::2,1::2]


def count_leap_years(years):
    y = years-543
    b = ((y % 4 == 0) & (y % 100 != 0)) | ((y % 4 == 0) & (y % 100 == 0) & (y % 400 == 0))
    return np.sum(b)

exec(input().strip()) 