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


DNA = ["A", "T", "G", "C"]
time_list = []

for x in range(1, 31):
    start_time = time.time()  # 측정 시작
    for _ in range(10):

        # dna1의 길이 = 100
        # dna2의 길이 = 50
        # 각 문자열은 A,T,G,C를 랜덤으로 배치하여 구성
        dna1 = "_"
        dna2 = "_"
        for i in range(100 * x):
            dna1 += random.choice(DNA)
        for j in range(50 * x):
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
        # 대각선에서 오는 것 -> match or mismatch : 1로 표현
        # 위에서 내려오는 것 -> gap : 2로 표현
        # 왼쪽에서 옆으로 오는 것 -> gap : 3으로 표현
        # 테이블에 (점수, 방향) 값을 넣는다.
        for i in range(1, b):
            for j in range(1, a):

                # 두 DNA가 같은 위치에 같은 값을 가진다면
                # (대각선 값+1, 1) 삽입
                if dna2[i] == dna1[j]:
                    table[i][j] = table[i - 1][j - 1] + 1

                # scoreAndVector 함수를 이용하여 (값, 방향) 삽입
                else:
                    table[i][j] = score(table[i - 1][j - 1], table[i - 1][j] - 1, table[i][j - 1] - 1)
    end_time = time.time()  # 측정 종료
    time_list.append((end_time - start_time) / 10)

# O(mn)을 나타내는 함수
def mn_func(mn, a, b):
    return a * mn + b


x_data = [100 * 50 * (x ** 2) for x in range(1, 31)]
y_data = time_list

# x_data, y_data를 출력
plt.scatter(x_data, y_data, label='mean_data')

x = np.array(x_data, dtype=float)
y = np.array(y_data, dtype=float)

# curve_fit를 이용하여 y_datd의 경향성 출력
popt, pcov = curve_fit(mn_func, x, y)
a, b = popt[0], popt[1]
curve_x = np.linspace(5000, 4500000, 100)
curve_y = mn_func(curve_x, a, b)
plt.plot(curve_x, curve_y, 'r', label='curve fitting')
plt.xlabel('m*n')
plt.ylabel('time')
plt.title("Measuring time complexity")
plt.legend()

plt.show()