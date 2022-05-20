import math
W = float(input())
H = float(input())
Mos = (math.sqrt(W*H))/60
Hay = 0.024265 * (W**0.5378) * (H**0.3964)
Boyd = 0.0333 * W**(0.6157 - 0.0188*math.log(W,10)) * H**0.3
print(Mos)
print(Hay)
print(Boyd)