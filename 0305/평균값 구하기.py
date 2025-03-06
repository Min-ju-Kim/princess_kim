# 2071

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    cnt = 0

    for i in range(10):
        cnt += arr[i] / 10

        # / int // float 구분하기

    print(f"#{tc} {round(cnt)}")