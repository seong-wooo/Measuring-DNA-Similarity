from itertools import combinations_with_replacement
# dna1과 dna2가 주어졌을 때 점수 및 dna2를 어떻게 수정하면 될 지
dna1 = input()
dna2 = input()
a, b = len(dna1), len(dna2)

# 긴 것이 dna1, 짧은 것이 dna2
if b > a:
    a, b = b, a
    dna1, dna2 = dna2, dna1


# a - b 만큼  "-" 기호를 넣는다.
# "-" 기호는 dna2 문자열의 모든 부분에 들어갈 수 있다.



result = 0
# a-b개 만큼 빈칸 삽입
for blank in combinations_with_replacement(range(b+1), a-b):
    dna3 = ""
    i = 0
    score = 0
    while i < b:
        if i in blank:
            dna3 += "-" * blank.count(i) + dna2[i]
            i += 1
        else:
            dna3 += dna2[i]
            i += 1
    dna3 += "-" * blank.count(b)

    for j in range(a):
        if dna1[j] == dna3[j]:
            score += 1
        elif dna3[j] == "-":
            score -= 1


    result = max(result, score)
print(f"점수는 {result}점 입니다.")




