import random
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def score(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# dna1과 dna2가 주어졌을 때 점수 및 dna2를 어떻게 수정하면 될 지


DNA = ["A","T","G","C"]
time_list = []

for x in range(1,21):
    start_time = time.time()  # 측정 시작
    for _ in range(10):

        dna1 = "_"
        dna2 = "_"
        for i in range(100*x):
            dna1 += random.choice(DNA)
        for j in range(50*x):
            dna2 += random.choice(DNA)

        a, b = len(dna1), len(dna2)

        # 긴 것이 dna1, 짧은 것이 dna2
        if b > a:
            a, b = b, a
            dna1, dna2 = dna2, dna1

        table = [[0] * (a) for _ in range(b)]

        for i in range(a):
            table[0][i] = -i

        for j in range(1, b):
            table[j][0] = -j

        # 방향 우선순위 : 대각선, 위, 왼쪽
        for i in range(1,b):
            for j in range(1,a):

                if dna2[i] == dna1[j]:
                    table[i][j] = table[i-1][j-1] + 1

                else:
                    table[i][j] = score(table[i-1][j-1], table[i-1][j]-1, table[i][j-1]-1)
    end_time = time.time()  # 측정 종료
    time_list.append((end_time-start_time)/10)


def mn_func(mn, a, b):
    return a * mn + b

x_data = [100*50*(x**2) for x in range(1,21)]
y_data = time_list

plt.scatter(x_data, y_data, label = 'mean_data')

x = np.array(x_data, dtype=float)
y = np.array(y_data, dtype=float)

popt, pcov = curve_fit(mn_func,x,y)
a, b = popt[0], popt[1]
print(a,b)
curve_x = np.linspace(5000, 2000000,100)
curve_y = mn_func(curve_x, a, b)
plt.plot(curve_x, curve_y,'r',label='curve fitting')
plt.xlabel('m*n')
plt.ylabel('time')
plt.title("Measuring time complexity")
plt.legend()

plt.show()
