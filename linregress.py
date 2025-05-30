M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]  
phi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]  

n = len(M)

sum_x2 = 0
sum_xy = 0
sum_y2 = 0

for i in range(n):
    x = phi[i]
    y = M[i]
    sum_x2 += x * x
    sum_xy += x * y
    sum_y2 += y * y

a = sum_xy / sum_x2

import math
sigma_a = math.sqrt((1/n) * (sum_y2 / sum_x2 - a ** 2))

print("Modul torzije Dt =", a, "Nm/rad")
print("Standardna devijacija σa =", sigma_a)