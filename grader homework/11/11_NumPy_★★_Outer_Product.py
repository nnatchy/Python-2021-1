import numpy as np
def mult_table(nrows,ncols):
    A = np.array(np.arange(1,nrows+1)).reshape(nrows,1)
    return A * np.arange(1,ncols+1)

exec(input().strip())