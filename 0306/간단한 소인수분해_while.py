T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 2, 3, 5, 7, 11의 개수 저장할 변수
    a = b = c = d = e = 0

    # 각 소인수로 나누며 카운트 증가
    while N % 2 == 0:
        N //= 2
        a += 1
    while N % 3 == 0:
        N //= 3
        b += 1
    while N % 5 == 0:
        N //= 5
        c += 1
    while N % 7 == 0:
        N //= 7
        d += 1
    while N % 11 == 0:
        N //= 11
        e += 1

    print(f"#{tc} {a} {b} {c} {d} {e}")
