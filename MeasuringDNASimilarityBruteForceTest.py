import sys
from itertools import combinations_with_replacement

# 두 DNA 값을 입력 받는다.
dna1 = input()
dna2 = input()
a, b = len(dna1), len(dna2)

# 긴 것이 dna1, 짧은 것이 dna2
if b > a:
    a, b = b, a
    dna1, dna2 = dna2, dna1


# a - b 만큼  "-" 기호를 넣는다.
# "-" 기호는 dna2 문자열의 모든 부분에 들어갈 수 있다.
# "-" 기호가 들어갈 자리를 선택한다.
# combinations_with_replacement()를 이용하여
# 중복을 허락하며 b+1 개의 자리 중 a -b개의 자리를 선택한다.

result = -sys.maxsize
# a-b개 만큼 빈칸 삽입
for gap in combinations_with_replacement(range(b+1), a-b):
    dna3 = ""
    i = 0
    score = 0

    # gap = "-"가 들어갈 자리들의 집합
    # dna3 는 dna2 문자열에 "-"을 추가한 문자열이 된다.
    while i < b:
        if i in gap:
            dna3 += "-" * gap.count(i) + dna2[i]
            i += 1
        else:
            dna3 += dna2[i]
            i += 1

    dna3 += "-" * gap.count(b)

    # 각 자리에 같은 값이 있으면 score += 1
    # -가 있으면 score -= 1
    for j in range(a):
        if dna1[j] == dna3[j]:
            score += 1
        elif dna3[j] == "-":
            score -= 1

    # 최종 결과는 score의 최댓값
    result = max(result, score)

print(f"점수는 {result}점 입니다.")

