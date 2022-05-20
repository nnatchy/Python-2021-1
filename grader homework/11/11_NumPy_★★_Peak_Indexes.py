import numpy as np


def peak_indexes(x):
    diff1 = np.sign(np.diff(x))
    diff2 = np.diff(diff1)
    # print(diff1)
    #print(diff2)
    pos = np.arange(1, len(x)-1)
    return pos[diff2 < -1]


def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")


exec(input().strip())  # Don't remove this line
