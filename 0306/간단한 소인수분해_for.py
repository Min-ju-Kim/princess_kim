T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [2, 3, 5, 7, 11]  # 소인수 리스트
    counts = [0] * 5  # 각 소인수의 개수

    for i in range(5):  # 소인수 5개에 대해 반복
        while N % arr[i] == 0:
            N //= arr[i]
            counts[i] += 1  # 해당 소인수의 개수 증가

    print(f"#{tc}", *counts)  # 리스트의 값을 한 줄로 출력