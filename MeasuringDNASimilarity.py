import random
import sys
import time
from itertools import combinations_with_replacement

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


DNA = ["A","T","G","C"]
dp_time_list = []
bf_time_list = []

for x in range(1,10):


    start_time = time.time()  # 측정 시작
    for _ in range(5):

        dna1 = "_"
        dna2 = "_"
        for i in range(3*x):
            dna1 += random.choice(DNA)
        for j in range(1*x):
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
    dp_time_list.append((end_time-start_time)/5)



for x in range(1,10):

   # brute force
    start_time = time.time()  # 측정 시작
    for _ in range(5):
        dna3 = ""
        dna4 = ""
        for i in range(3 * x):
            dna3 += random.choice(DNA)
        for j in range(1 * x):
            dna4 += random.choice(DNA)

        a, b = len(dna3), len(dna4)
        result = -sys.maxsize
        # a-b개 만큼 빈칸 삽입
        for gap in combinations_with_replacement(range(b + 1), a - b):
            dna5 = ""
            i = 0
            score = 0
            while i < b:
                if i in gap:
                    dna5 += "-" * gap.count(i) + dna4[i]
                    i += 1
                else:
                    dna5 += dna4[i]
                    i += 1
            dna5 += "-" * gap.count(b)

            for j in range(a):
                if dna3[j] == dna5[j]:
                    score += 1
                elif dna3[j] == "-":
                    score -= 1

            result = max(result, score)
    end_time = time.time()  # 측정 종료
    bf_time_list.append((end_time-start_time)/5)



def mn_func(mn, a, b):
    return a * mn + b

x_data = [3*1*(x**2) for x in range(1,10)]
y_dp_data = dp_time_list
y_bf_data = bf_time_list
plt.scatter(x_data, y_dp_data, label = 'DP_data')
plt.scatter(x_data, y_bf_data, edgecolors="b", label = 'BF_data')

# x = np.array(x_data, dtype=float)
# y = np.array(y_dp_data, dtype=float)
# popt, pcov = curve_fit(mn_func,x,y)
# a, b = popt[0], popt[1]
# curve_x = np.linspace(1, 300,10)
# curve_y = mn_func(curve_x, a, b)
# plt.plot(curve_x, curve_y,'r',label='curve fitting')
plt.xlabel('m*n')
plt.ylabel('time')
plt.title("Measuring time complexity")
plt.legend()
plt.show()
