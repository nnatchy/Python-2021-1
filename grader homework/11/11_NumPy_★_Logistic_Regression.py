import numpy as np
def p(x):
    res = -3.98 + 0.1*x[:,0] + 0.5*x[:,1]
    return 1/(1+np.e**(-res))
exec(input().strip())