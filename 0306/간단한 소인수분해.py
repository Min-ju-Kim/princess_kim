T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 인수들 리스트 생성
    arr = [2, 3, 5, 7, 11]

    cnt = [0] * len(arr)


    for i in range(len(arr)):
        # N 인수로 나눌 수 있을때까지 계속 반복
        while N % arr[i] == 0:
            # N i의 인수로 나누기
            N //= arr[i]
            cnt[i] += 1

    print(f"#{tc}", *cnt)

    # a = 2가 몇 번 곱해져있는지
    # N을 2로 나눠진 횟수 = 곱해진 횟수
    # 2로 나누기 -> 몇 번 반복할지 모름 
    # => while문 사용하기
    # a -> 0으로 초기화
    # 1. 2로 나눠지는지 확인
    # 2. 나누어지면 -> a += 1
