# 2072

T = int(input())

for tc in range(1, T + 1):
    N = list(map(int, input().split()))

    cnt = 0

    # 나머지가 1이면 출력 후 더하기
    for i in range(10):
        if N[i] % 2 == 1:
            cnt += N[i]

    print(f"#{tc} {cnt}")

    # 변수 만들기
    # 반복문 돌려서 조건에 맞는 거 찾아서 변수에 더해주기
    # 반복문 끝나면 변수에 다 더해져 있음
    # 변수 출력