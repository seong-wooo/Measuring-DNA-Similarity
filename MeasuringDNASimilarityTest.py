#1 테스트
def scoreAndVector(a, b, c):
    if a >= b and a >= c:
        return a, 1
    elif b >= a and b >= c:
        return b, 2
    else:
        return c, 3

# dna1과 dna2가 주어졌을 때 점수 및 dna2를 어떻게 수정하면 될 지
dna1 = "_" + input()
dna2 = "_" + input()
a, b = len(dna1), len(dna2)

# 긴 것이 dna1, 짧은 것이 dna2
if b > a:
    a, b = b, a
    dna1, dna2 = dna2, dna1

table = [[0] * (a) for _ in range(b)]

for i in range(a):
    table[0][i] = (-i,0)

for j in range(1, b):
    table[j][0] = (-j,0)

# 방향 우선순위 : 대각선, 위, 왼쪽
# 대각선에서 오는 것 -> match or mismatch : 1로 표현
# 위에서 내려오는 것 -> gap : 2로 표현
# 왼쪽에서 옆으로 오는 것 -> gap : 3으로 표현
# (점수, 방향)
for i in range(1,b):
    for j in range(1,a):

        if dna2[i] == dna1[j]:
            table[i][j] = (table[i-1][j-1][0] + 1, 1)

        else:
            score, vector = scoreAndVector(table[i-1][j-1][0], table[i-1][j][0]-1, table[i][j-1][0]-1)
            table[i][j] = (score, vector)



print(f"점수는 {table[b-1][a-1][0]}점입니다.")

i,j = b-1, a-1
dna = ""
while i != 0 and j != 0:
    #대각선
    if table[i][j][1] == 1:
        dna = dna2[i] + dna
        i, j = i - 1, j - 1
    #위
    elif table[i][j][1] == 2:
        dna = "-" + dna
        i -= 1
    else:
        dna = "-" + dna
        j -= 1

print(dna1[1:])
print(dna)

