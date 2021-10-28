# Dynamic programming 방식 테스트

# 대각선, 위, 왼쪽 방향 중 제일 큰 값과 방향을 반환한다.
# 1 -> 대각선
# 2 -> 위
# 3 -> 왼쪽
def scoreAndVector(a, b, c):
    if a >= b and a >= c:
        return a, 1
    elif b >= a and b >= c:
        return b, 2
    else:
        return c, 3

# 두 DNA의 값을 입력받는다.
# 테이블 첫 행 첫 열에 초기 작업을 해야하므로
# "_" 를 붙여서 나타낸다.
dna1 = "_" + input()
dna2 = "_" + input()


a, b = len(dna1), len(dna2)

# 긴 것이 dna1, 짧은 것이 dna2라고 지정한다.
if b > a:
    a, b = b, a
    dna1, dna2 = dna2, dna1

# 테이블 생성
table = [[0] * (a) for _ in range(b)]

# 초기 작업
for i in range(a):
    table[0][i] = (-i,0)

for j in range(1, b):
    table[j][0] = (-j,0)



# 방향 우선순위 : 대각선, 위, 왼쪽
# 대각선에서 오는 것 -> match or mismatch : 1로 표현
# 위에서 내려오는 것 -> gap : 2로 표현
# 왼쪽에서 옆으로 오는 것 -> gap : 3으로 표현
# 테이블에 (점수, 방향) 값을 넣는다.
for i in range(1,b):
    for j in range(1,a):

        # 두 DNA가 같은 위치에 같은 값을 가진다면
        # (대각선 값+1, 1) 삽입
        if dna2[i] == dna1[j]:
            table[i][j] = (table[i-1][j-1][0] + 1, 1)

        # scoreAndVector 함수를 이용하여 (값, 방향) 삽입
        else:
            score, vector = scoreAndVector(table[i-1][j-1][0], table[i-1][j][0]-1, table[i][j-1][0]-1)
            table[i][j] = (score, vector)

print(f"점수는 {table[b-1][a-1][0]}점입니다.")

# 최고 점수를 갖게 되는 변경된 DNA를 출력한다.
# 맨 마지막 셀부터 차례대로 방향을 따라 값을 읽는다.
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
    #왼
    else:
        dna = "-" + dna
        j -= 1

if i > 0:
    dna = "-" * i + dna
else:
    dna = "-" * j + dna
print(dna1[1:])
print(dna)

for d in table:
    print(d)
